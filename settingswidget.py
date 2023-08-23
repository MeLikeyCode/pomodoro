import customtkinter as ctk
import tkinter as tk
import yaml


class SettingsWidget(ctk.CTkFrame):
    """Widget that has GUI elements that can be used to configure pomodoro timer parameters."""

    def __init__(self, master):
        super().__init__(master)
        self._initialize_gui()

    def _initialize_gui(self):
        # load initial param values from settings.yaml
        with open("settings.yaml", "r") as f:
            settings = yaml.safe_load(f)

            self._work_length_var = tk.IntVar(value=settings["work_length"])
            self._break_length_var = tk.IntVar(value=settings["break_length"])
            self._long_break_length_var = tk.IntVar(value=settings["long_break_length"])
            self._num_works_before_long_break_var = tk.IntVar(value=settings["num_works_before_long_break"])

        # listen for changes to params
        self._work_length_var.trace_id = self._work_length_var.trace("w", self._on_value_changed)
        self._break_length_var.trace_id = self._break_length_var.trace("w", self._on_value_changed)
        self._long_break_length_var.trace_id = self._long_break_length_var.trace("w", self._on_value_changed)
        self._num_works_before_long_break_var.trace_id = self._num_works_before_long_break_var.trace("w", self._on_value_changed)

        self.grid_columnconfigure(1, weight=1)

        l1 = ctk.CTkLabel(self, text="work length (minutes): ")
        l2 = ctk.CTkLabel(self, text="short break length (minutes): ")
        l3 = ctk.CTkLabel(self, text="long break length (minutes): ")
        l4 = ctk.CTkLabel(self, text="number of works before long break: ")

        e1 = tk.Spinbox(self, from_=1, to=120, textvariable=self._work_length_var)
        e2 = tk.Spinbox(self, from_=1, to=30, textvariable=self._break_length_var)
        e3 = tk.Spinbox(self, from_=1, to=60, textvariable=self._long_break_length_var)
        e4 = tk.Spinbox(
            self, from_=1, to=10, textvariable=self._num_works_before_long_break_var
        )

        l1.grid(row=0, column=0, sticky=ctk.W)
        l2.grid(row=1, column=0, sticky=ctk.W)
        l3.grid(row=2, column=0, sticky=ctk.W)
        l4.grid(row=3, column=0, sticky=ctk.W)

        e1.grid(row=0, column=1, sticky=ctk.EW)
        e2.grid(row=1, column=1, sticky=ctk.EW)
        e3.grid(row=2, column=1, sticky=ctk.EW)
        e4.grid(row=3, column=1, sticky=ctk.EW)

    def _on_value_changed(self, *args):
        """Executed when any of the timer parameters (work length, break length, etc) are changed. Will
        write the new values to the settings file."""

        with open("settings.yaml", "w") as f:
            settings_dict = {
                "work_length": self.work_length,
                "break_length": self.break_length,
                "long_break_length": self.long_break_length,
                "num_works_before_long_break": self.num_works_before_long_break,
            }
            f.write(yaml.dump(settings_dict))

    @property
    def work_length(self):
        return self._work_length_var.get()

    @property
    def break_length(self):
        return self._break_length_var.get()

    @property
    def long_break_length(self):
        return self._long_break_length_var.get()

    @property
    def num_works_before_long_break(self):
        return self._num_works_before_long_break_var.get()
