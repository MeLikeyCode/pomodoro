import customtkinter as ctk
import pystray
from PIL import Image, ImageTk

from startscreen import StartScreen
from timerscreen import TimerScreen
from pomodoro import Pomodoro


class PomodoroApp:
    """Represents the pomodoro application as a whole.

    Example:
        p = PomodoroApp()
        p.start()
    """

    def __init__(self) -> None:
        self.root = ctk.CTk()
        ctk.set_appearance_mode("system")  # modes: system (default), light, dark
        ctk.set_default_color_theme("green")  # themes: blue (default), dark-blue, green
        self.root.title("pomodoro")
        self.root.geometry("720x480")
        self.root.protocol("WM_DELETE_WINDOW", self._trayize_window)
        self.root.wm_iconphoto(False, ImageTk.PhotoImage(file="tomato.png"))

        # set up start screen
        self._start_screen = StartScreen(self.root)
        self._start_screen.pack(fill=ctk.BOTH, expand=True)
        self._start_screen.on_start = self.on_start_timer

        # set up timer screen
        self._timer_screen = TimerScreen(self.root)
        self._timer_screen.on_stop = self.on_stop_timer

    def start(self):
        self.root.mainloop()

    def on_start_timer(self):
        """Executed when the start screen's start button is pressed."""
        # hide start screen
        self._start_screen.pack_forget()

        # show timer screen
        self._timer_screen.pack(fill=ctk.BOTH, expand=True)

        self._timer_screen.work_length = self._start_screen.work_length
        self._timer_screen.break_length = self._start_screen.break_length
        self._timer_screen.long_break_length = self._start_screen.long_break_length
        self._timer_screen.num_works_before_long_break = (
            self._start_screen.num_works_before_long_break
        )

        self._timer_screen.start_timer()

    def on_stop_timer(self):
        """Executed when the timer screen's stop button is pressed."""
        # hide timer screen
        self._timer_screen.pack_forget()

        # show start screen
        self._start_screen.pack(fill=ctk.BOTH, expand=True)

    def _on_tray_quit(self, icon, item):
        """Executed when the "quit" option of the tray is selected."""
        icon.stop()
        self._timer_screen.stop_timer()
        self.root.destroy()

    def _on_tray_show(self, icon, item):
        """Executed when the "show" option of the tray is selected."""
        icon.stop()
        self.root.after(0, self.root.deiconify)

    def _trayize_window(self):
        """Hide the window and show the tray icon."""
        self.root.withdraw()
        image = Image.open("tomato.png")
        menu = (
            pystray.MenuItem("Quit", self._on_tray_quit),
            pystray.MenuItem("Show", self._on_tray_show, default=True),
        )
        icon = pystray.Icon("pomodoro", image, "pomodoro", menu)
        icon.run()
