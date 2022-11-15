# Dependencies
- python 3
- customtkinter (provides a better looking GUI than vanilla tkinter)
- pystray (allows placing interactable icons in the system tray)
- pyler (allows poping up notifications)

# Building Executable
Prereqs:
- fish shell (build script written in fish)
- pyinstaller
- python environment with all the dependent packages

Run `build.fish`. Output will be the folder `<project root>/dist/pomodor`. Just distribute that folder to end users. They will just need to run `pomodoro.exe` located within that folder.

# Conventions
- the Pomodoro class (pomodoro.py) uses *seconds* for work length, break length, and long break length, where as all the gui related classes (TimerScreen, StartScreen, etc) use *minutes*