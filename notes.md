# Dependencies
- **python 3**
- **customtkinter** (provides a more modern looking GUI than vanilla tkinter)
- **PIL** (used for image objects for tkinter)
- **pystray** (allows placing interactable icons in the system tray)
- **pyler** (allows poping up notifications)

# Building an Executable
Prereqs:
- **pip** (used to find location of customtkinter)
- **pyinstaller** (used to create the executable/dependent stuff)
- python environment with all the dependent packages

Run `build.py`. Output will be the folder `<project root>/dist/pomodor`. Just distribute that folder to end users. They will just need to run `pomodoro.exe` located within that folder.

# Conventions
- the Pomodoro class (pomodoro.py) uses *seconds* for work length, break length, and long break length, where as all the gui related classes (TimerScreen, StartScreen, etc) use *minutes*