import customtkinter as ctk
import pystray
from PIL import Image

from settings import Settings
from pomodoro import Pomodoro

class PomodoroApp:
    """Represents the pomodoro application as a whole."""

    def __init__(self) -> None:
        self.root = ctk.CTk()
        self.root.title("pomodoro")
        self.root.geometry("800x600")
        self.root.protocol("WM_DELETE_WINDOW", self._trayize_window)

    def start(self):
        p = Pomodoro(self.root)
        p.pack(fill=ctk.BOTH,expand=True)

        self.root.mainloop()

    def _on_tray_quit(self, icon, item):
        icon.stop()
        self.root.destroy()

    def _on_tray_show(self, icon, item):
        icon.stop()
        self.root.after(0, self.root.deiconify)

    def _trayize_window(self):
        self.root.withdraw()
        image = Image.open("icon.png")
        menu = (
            pystray.MenuItem("Quit", self._on_tray_quit),
            pystray.MenuItem("Show", self._on_tray_show, default=True),
        )
        icon = pystray.Icon("pomodoro", image, "pomodoro", menu)
        icon.run()
