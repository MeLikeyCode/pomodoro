import customtkinter as ctk
import pystray
from PIL import Image, ImageTk
import pygame

from startscreen import StartScreen
from timerscreen import TimerScreen
from pomodoro import Pomodoro
from musicplayer import MusicPlayer


class PomodoroApp:
    """Represents the pomodoro application as a whole.

    Example:
        p = PomodoroApp()
        p.start()

    Be careful, some of the methods of this class are called by worker threads, so they should not access things
    directly, should just add events to the event queue. Methods that are called by worker threads say so
    in their docstrings.
    """

    def __init__(self) -> None:
        # Initialize pygame mixer.
        # We use pygame's mixer module to play sounds.
        # The module needs to be "initialized" before it can be used.
        # Since multiple classes use the mixer, we initialize it here (when the application's "main" class is constructed) once, and all
        # subsequent classes can use it.
        # We also set the number of channels to 3, so that we can play up to 3 sounds at the same time (i.e. simultaneously).
        pygame.mixer.init()
        pygame.mixer.set_num_channels(3)

        self.root = ctk.CTk()
        ctk.set_appearance_mode("system")  # modes: system (default), light, dark
        ctk.set_default_color_theme("green")  # themes: blue (default), dark-blue, green
        self.root.title("pomodoro")
        self.root.geometry("720x480")
        self.root.protocol("WM_DELETE_WINDOW", self._trayize_window)
        self.root.wm_iconphoto(False, ImageTk.PhotoImage(file="images/tomato.png"))

        self._tray: pystray.Icon = None
        self._tray_image = Image.open("images/tomato.png")
        self._set_tray((("quit", self._on_tray_quit),))

        self.root.bind("<<Quit>>", lambda e: self.root.destroy())
        self.root.bind("<<Show>>", self._on_show)

        top_frame = ctk.CTkFrame(self.root)
        top_frame.pack(fill=ctk.BOTH, expand=True)
        bot_frame = ctk.CTkFrame(self.root)
        bot_frame.pack(fill=ctk.BOTH, expand=True)

        # set up start screen
        self._start_screen = StartScreen(top_frame)
        self._start_screen.pack(fill=ctk.BOTH, expand=True)
        self._start_screen.on_start = self.on_start_timer

        # set up timer screen
        self._timer_screen = TimerScreen(top_frame)
        self._timer_screen.on_stop = self.on_stop_timer

        # set up music player
        self._music_player = MusicPlayer(bot_frame)
        self._music_player.pack(fill=ctk.BOTH, expand=True)

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

    def _on_show(self, e):
        """Executed in response to the <<Show>> event."""
        self.root.deiconify()
        self._set_tray((("quit", self._on_tray_quit),))

    def _set_tray(self, menu_items, default=None):
        if self._tray:
            self._tray.stop()

        menu = []
        for item in menu_items:
            if item[0] == default:
                menu.append(pystray.MenuItem(item[0], item[1], default=True))
            else:
                menu.append(pystray.MenuItem(item[0], item[1]))

        self._tray = pystray.Icon("pomodoro", self._tray_image, "pomodoro", menu)
        self._tray.run_detached()

    def _on_tray_quit(self, icon, item):
        """Executed when the "quit" option of the tray is selected.
        
        This is executed by a daemon thread (pystray run_detached thread), so we add a quit event to the event queue of tk (which is thread safe probably???)
        """
        icon.stop()
        self._timer_screen.stop_timer()
        self.root.event_generate("<<Quit>>")

    def _on_tray_show(self, icon, item):
        """Executed when the "show" option of the tray is selected.
        
        This is executed by a daemon thread (pystray run_detached thread), so we just add an event to event queue.
        """
        self.root.event_generate("<<Show>>")

    def _trayize_window(self):
        """Hide the window and add "show" option to the tray."""
        self.root.withdraw()
        self._set_tray((("show", self._on_tray_show), ("quit", self._on_tray_quit)),default="show")

