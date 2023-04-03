from pomodoroapp import PomodoroApp
import msvcrt
import tempfile
from win32gui import FindWindow, ShowWindow, SetForegroundWindow
from win32con import SW_RESTORE
import os

if __name__ == "__main__":
    # check if another instance of Pomodoro is already running
    lock_file_path = tempfile.gettempdir() + "/pomodoro.lock"
    lock_file = open(lock_file_path, 'w') # create the lock file if it doesn't exist
    try:
        # try locking the "lock" file
        msvcrt.locking(lock_file.fileno(), msvcrt.LK_NBLCK, 1)
    except IOError:
        # failed to lock it, thus another instance locked it (and is thus running)
        print("An instance of Pomodoro is already running")
        # show the window of the running instance, and exit
        hwnd = FindWindow(None, "pomodoro")
        ShowWindow(hwnd, SW_RESTORE)
        SetForegroundWindow(hwnd)
        os._exit(0)

    app = PomodoroApp()
    app.start()
    