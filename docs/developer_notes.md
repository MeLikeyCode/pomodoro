# Dependencies
- **python 3**
- **customtkinter** (provides a more modern looking GUI than vanilla tkinter)
- **PIL** (used for image objects for tkinter)
- **pystray** (allows placing interactable icons in the system tray)
- **plyer** (allows poping up notifications)
- **pygame** (used to play music)

# Building an Installer
Prereqs:
- **pip** (used to find location of customtkinter)
- **pyinstaller** (used to package the python interpretter, dependent .py files, .dlls, etc)
- python environment with all the dependent packages
- NSIS (nullsoft scriptable install system)

Run `build.py`. Pyinstaller output (the python interpretter, dependent .py files, .dlls, etc all packaged up in a folder) will be at `<project root>/dist/pomodoro`. The actual NSIS installer (this is the installer that needs to be distributed to end users) will be at `<project root>/pomodoro_installer.exe`.

# Conventions
- the Pomodoro class (pomodoro.py) uses *seconds* for work length, break length, and long break length, where as all the gui related classes (TimerScreen, StartScreen, etc) use *minutes*