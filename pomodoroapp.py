import customtkinter as ctk
import pystray
from PIL import Image, ImageTk

from startscreen import StartScreen
from timerscreen import TimerScreen

class PomodoroApp:
    """Represents the pomodoro application as a whole."""

    def __init__(self) -> None:
        self.root = ctk.CTk()
        ctk.set_appearance_mode("system")  # modes: system (default), light, dark
        ctk.set_default_color_theme("green")  # themes: blue (default), dark-blue, green
        self.root.title("pomodoro")
        self.root.geometry("720x480")
        self.root.protocol("WM_DELETE_WINDOW", self._trayize_window)

        self.root.wm_iconphoto(False, ImageTk.PhotoImage(file="tomato.png"))

        self._start_screen = StartScreen(self.root)
        self._start_screen.pack(fill=ctk.BOTH, expand=True)
        self._start_screen.on_start = self.on_start_button

        self._timer_screen = TimerScreen(self.root)

    def start(self):
        self.root.mainloop()

    def on_start_button(self):
        # hide start screen
        self._start_screen.pack_forget()

        # show timer screen
        self._timer_screen.pack(fill=ctk.BOTH, expand=True)

    def _on_tray_quit(self, icon, item):
        icon.stop()
        self.root.destroy()

    def _on_tray_show(self, icon, item):
        icon.stop()
        self.root.after(0, self.root.deiconify)

    def _trayize_window(self):
        self.root.withdraw()
        image = Image.open("tomato.png")
        menu = (
            pystray.MenuItem("Quit", self._on_tray_quit),
            pystray.MenuItem("Show", self._on_tray_show, default=True),
        )
        icon = pystray.Icon("pomodoro", image, "pomodoro", menu)
        icon.run()
