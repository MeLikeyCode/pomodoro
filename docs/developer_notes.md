# Dependencies
- **python 3**
- **customtkinter** (provides a more modern looking GUI than vanilla tkinter)
- **PIL** (used for image objects for tkinter)
- **pystray** (allows placing interactable icons in the system tray)
- **plyer** (allows poping up notifications)
- **pygame** (used to play audio)

# Building an Installer
Prereqs:
- python environment with all the dependent packages
- **pyinstaller** (used to package the python interpretter, dependent .py files, .dlls, etc)
- **pip** (used to find location of customtkinter)
- NSIS (nullsoft scriptable install system)

Run `build.py` with your python environment that meets all the required prereqs/dependencies. Pyinstaller output (the python interpretter, dependent .py files, .dlls, etc all packaged up in a folder) will be at `<project root>/dist/pomodoro`. The actual NSIS installer (this is the installer that needs to be distributed to end users) will be at `<project root>/pomodoro_installer.exe`.

# Conventions
- the Pomodoro class (pomodoro.py) uses *seconds* for work length, break length, and long break length, where as all the gui related classes (TimerScreen, StartScreen, etc) use *minutes*

# CustomTkinter
Since we are using customtkinter, be sure to create the widgets provided by the customtkinter package instead of the regular tkinter widgets.

~~~~~~~~~~~~~~~~~~~~~~~~~~~
import customtkinter as ctk
button = ctk.CTkButton(parent, text=f"hello")
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Take ~1 minute to read the [main page of customtkinter](https://github.com/TomSchimansky/CustomTkinter). Just read the main description up at the top and the "example program" section.