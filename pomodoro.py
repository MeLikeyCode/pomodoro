import threading
import time

OFF = "off"
WORK = "work"
BREAK = "break"
LONG_BREAK = "long break"


class Pomodoro:
    """A pomodoro timer.

    p = Pomodoro() # default is 25 minutes of work, 5 minutes of break, 4 works before long break (but can be customized via attributes before starting)
    p.start() # start the pomodoro timer
    p.state() # returns "work", "break", or "long break"
    p.time_remaining() # returns time remaining in seconds for the current state

    IMPORTANT: Do not access private members directly. They are not thread safe. Use only the public API.

    This class creates/uses a worker thread to keep updating the remaining time and other variables.
    Thus, this class has attributes that both its worker thread and the calling thread (the thread that
    constructs/uses this class) need/want to access. Accessing these attributes through the public API
    uses a mutex to ensure thread safety between the calling thread and the worker thread.
    """

    def __init__(self) -> None:
        self._mutex = threading.Lock()  # guards all attributes except _start_time

        self._state: str = OFF
        self._time_remaining: int = None  # seconds

        self._num_works_before_long_break: int = 4
        self._num_works_done: int = 0
        self._num_rounds_done: int = (
            0  # a "round" is when max num works before long break are done
        )

        self._work_length = 25 * 60  # seconds
        self._break_length = 5 * 60
        self._long_break_length = 20 * 60

        self._start_time: float = None  # in "since epoc" format
        self._started = False

    @property
    def state(self):
        with self._mutex:
            return self._state

    @property
    def time_remaining(self):
        with self._mutex:
            return self._time_remaining

    @property
    def num_works_before_long_break(self):
        with self._mutex:
            return self._num_works_before_long_break

    @num_works_before_long_break.setter
    def num_works_before_long_break(self, new_value):
        with self._mutex:
            self._num_works_before_long_break = new_value

    @property
    def num_works_done(self):
        with self._mutex:
            return self._num_works_done

    @property
    def num_rounds_done(self):
        with self._mutex:
            return self._num_rounds_done

    @property
    def started(self):
        with self._mutex:
            return self._started

    @property
    def work_length(self):
        with self._mutex:
            return self._work_length

    @work_length.setter
    def work_length(self, new_value):
        with self._mutex:
            self._work_length = new_value

    @property
    def break_length(self):
        with self._mutex:
            return self._break_length

    @break_length.setter
    def break_length(self, new_value):
        with self._mutex:
            self._break_length = new_value

    @property
    def long_break_length(self):
        with self._mutex:
            return self._long_break_length

    @long_break_length.setter
    def long_break_length(self, new_value):
        with self._mutex:
            self._long_break_length = new_value

    def start(self):
        with self._mutex:
            if self._started:
                return  # do nothing if already started
            self._started = True
            self._change_state(WORK)
        self._worker = threading.Thread(target=self._worker_thread_method)
        self._worker.start()

    def stop(self):
        with self._mutex:
            self._change_state(OFF)
        # self._worker.join() # thread will exit on its own; no need to join unless we want the calling thread to wait for it to finish

    def _worker_thread_method(self):
        while True:
            self._mutex.acquire()

            # check if worker needs to stop
            if not self._started:
                self._mutex.release()
                return

            if self._state == WORK:
                self._handle_work_state()
            elif self._state == BREAK:
                self._handle_break_state()
            elif self._state == LONG_BREAK:
                self._handle_long_break_state()
            else:
                raise RuntimeError("did not expect to reach here")

            self._mutex.release()
            time.sleep(1)

    def _handle_work_state(self):
        self._update_time_remaining(self._work_length)
        if self._time_remaining <= 0:
            self._num_works_done += 1
            if self._num_works_done >= self._num_works_before_long_break:
                self._num_rounds_done += 1
                self._num_works_done = 0
                self._change_state(LONG_BREAK)
            else:
                self._change_state(BREAK)

    def _handle_break_state(self):
        self._update_time_remaining(self._break_length)
        if self._time_remaining <= 0:
            self._change_state(WORK)

    def _handle_long_break_state(self):
        self._update_time_remaining(self._long_break_length)
        if self._time_remaining <= 0:
            self._change_state(WORK)

    def _change_state(self, new_state):
        """Sets the attributes to appropriate values for the new state. Handles coming from any state to the new state."""
        
        self._start_time = time.time()
        self._state = new_state
        if new_state == WORK:
            self._time_remaining = self._work_length
        elif new_state == BREAK:
            self._time_remaining = self._break_length
        elif new_state == LONG_BREAK:
            self._time_remaining = self._long_break_length
        elif new_state == OFF:
            self._time_remaining = None
            self._num_works_done = 0
            self._num_rounds_done = 0
            self._start_time = None
            self._started = False
            self._start_time = None

    def _update_time_remaining(self, time_required):
        current_time = time.time()
        time_elapsed = current_time - self._start_time
        time_remaining = time_required - time_elapsed
        self._time_remaining = int(time_remaining)

    def __repr__(self) -> str:
        return {
            "state": self.state,
            "time remaining": self.time_remaining,
            "num works done": self.num_works_done,
            "num rounds done": self.num_rounds_done,
        }.__repr__()
