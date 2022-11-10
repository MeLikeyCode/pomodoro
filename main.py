from pomodoroapp import PomodoroApp

from pomodoro import Pomodoro

import time

if __name__ == "__main__":
    # app = PomodoroApp()
    # app.start()

    p = Pomodoro()
    p.work_length = 20
    p.break_length = 5
    p.long_break_length = 10

    a = 3
    