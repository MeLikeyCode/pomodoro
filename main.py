from pomodoroapp import PomodoroApp
import psutil

def process_exists(process_name):
    """Returns true if a process with the specified name is running."""
    for process in psutil.process_iter(['name']):
        if process.info['name'] == process_name:
            return True
    return False

if __name__ == "__main__":
    # if app is already running, untray it and quit
    if process_exists("pomodoro.exe"):
        from win32gui import FindWindow, ShowWindow, SetForegroundWindow
        from win32con import SW_RESTORE, SW_SHOW
        hwnd = FindWindow(None, "Pomodoro")
        ShowWindow(hwnd, SW_RESTORE)
        SetForegroundWindow(hwnd)
        exit(0)

    app = PomodoroApp()
    app.start()
    