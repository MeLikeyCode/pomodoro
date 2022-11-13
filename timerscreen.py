import customtkinter as ctk
from PIL import ImageTk, Image

from pomodoro import Pomodoro


class TimerScreen(ctk.CTkFrame):
    """Represents the screen where the pomodoro timer counts down."""

    def __init__(self, master):
        super().__init__(master)

        self._initialize_gui()

        self._pomodoro_timer = Pomodoro()

        self.after_idle(self.on_idle)

    def _initialize_gui(self):
        stop_image = ImageTk.PhotoImage(Image.open("stop.png").resize((100, 100)))

        title_label = ctk.CTkLabel(self, text="pomodoro", text_font=("Helvetica", 25))

        stop_button = ctk.CTkButton(
            self, text="stop", image=stop_image, compound=ctk.TOP, command=self._on_stop, fg_color="#D2686E", hover_color="#680C07"
        )
        self._activity_label = ctk.CTkLabel(self, text_font=("Helvetica", 25))
        self._time_remaining_label = ctk.CTkLabel(self, text_font=("Helvetica", 40))


        title_label.pack(padx=10, pady=10, fill=ctk.X)
        stop_button.pack(padx=10, pady=10, fill=ctk.X)
        self._activity_label.pack(padx=10, pady=10, fill=ctk.X)
        self._time_remaining_label.pack(padx=10, pady=10, fill=ctk.X)

        works_done_frame = ctk.CTkFrame(self)
        rounds_done_frame = ctk.CTkFrame(self)

        works_done = ctk.CTkLabel(works_done_frame, text="works done: ", anchor=ctk.E)
        self._works_done_value_label = ctk.CTkLabel(works_done_frame, anchor=ctk.W)
        rounds_done = ctk.CTkLabel(
            rounds_done_frame, text="rounds done: ", anchor=ctk.E
        )
        self._rounds_done_value_label = ctk.CTkLabel(rounds_done_frame, anchor=ctk.W)

        works_done.pack(side=ctk.LEFT)
        self._works_done_value_label.pack(side=ctk.LEFT)
        rounds_done.pack(side=ctk.LEFT)
        self._rounds_done_value_label.pack(side=ctk.LEFT)

        works_done_frame.pack()
        rounds_done_frame.pack()

    def _on_stop(self):
        self._pomodoro_timer.stop()
        self.on_stop()

    def start_timer(self):
        self._pomodoro_timer.start()

    def on_stop(self):
        pass  # expecting client to assign this; gives client a chance to do something when stop button is clicked

    def on_idle(self):
        # update GUI to reflect the underlying timer
        if self._pomodoro_timer.started:
            # update time remaining
            mins_remaining = int(self._pomodoro_timer.time_remaining / 60)
            secs_remaining = int(self._pomodoro_timer.time_remaining % 60)
            time_remaining = "{:02d}:{:02d}".format(mins_remaining, secs_remaining)
            self._time_remaining_label.configure(text=time_remaining)

            # update status
            self._activity_label.configure(text=self._pomodoro_timer.state)

            # update works done
            works_done = self._pomodoro_timer.num_works_done
            self._works_done_value_label.configure(text=works_done)

            # update rounds done
            rounds_done = self._pomodoro_timer.num_rounds_done
            self._rounds_done_value_label.configure(text=rounds_done)

        self.after(1000,self.on_idle)  # call every second

    @property
    def work_length(self):
        return self._pomodoro_timer.work_length * 60

    @work_length.setter
    def work_length(self, value):
        self._pomodoro_timer.work_length = value * 60

    @property
    def break_length(self):
        return self._pomodoro_timer.break_length * 60

    @break_length.setter
    def break_length(self, value):
        self._pomodoro_timer.break_length = value * 60

    @property
    def long_break_length(self):
        return self._pomodoro_timer.long_break_length * 60

    @long_break_length.setter
    def long_break_length(self, value):
        self._pomodoro_timer.long_break_length = value * 60

    @property
    def num_works_before_long_break(self):
        return self._pomodoro_timer.num_works_before_long_break

    @num_works_before_long_break.setter
    def num_works_before_long_break(self, value):
        self._pomodoro_timer.num_works_before_long_break = value
