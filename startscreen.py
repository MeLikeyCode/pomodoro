import customtkinter as ctk
from PIL import ImageTk, Image
from settingswidget import SettingsWidget


class StartScreen(ctk.CTkFrame):
    """Widget that represents the starting screen of the app. This is the screen
    with the logo, start button, and settings widget."""

    def __init__(self, master):
        super().__init__(master)
        self._initialize_gui()

    def _initialize_gui(self):
        play_image = ImageTk.PhotoImage(Image.open("images/play.png").resize((100, 100)))

        title_label = ctk.CTkLabel(self, text="pomodoro", font=("Helvetica", 25))
        start_button = ctk.CTkButton(
            self,
            text="start",
            image=play_image,
            compound=ctk.TOP,
            command=self._on_start,
        )

        title_label.pack(padx=10, pady=10, fill=ctk.X)
        start_button.pack(padx=10, pady=10, fill=ctk.X)

        self._settings = SettingsWidget(self)
        self._settings.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

    def _on_start(self):
        self.on_start()

    def on_start(self):
        pass  # expecting client to assign this, gives client a chance to do something when the start button is pressed

    @property
    def work_length(self):
        return self._settings.work_length

    @property
    def break_length(self):
        return self._settings.break_length

    @property
    def long_break_length(self):
        return self._settings.long_break_length

    @property
    def num_works_before_long_break(self):
        return self._settings.num_works_before_long_break