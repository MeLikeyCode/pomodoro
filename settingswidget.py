import customtkinter as ctk
import tkinter as tk
import tkinter.ttk as ttk


class SettingsWidget(ctk.CTkFrame):
    """Widget that has GUI elements that can be used to configure pomodoro timer parameters."""

    def __init__(self, master):
        super().__init__(master)
        self._initialize_gui()

    def _initialize_gui(self):
        self._work_length_var = tk.IntVar(value=25)
        self._break_length_var = tk.IntVar(value=5)
        self._long_break_length_var = tk.IntVar(value=20)
        self._num_works_before_long_break_var = tk.IntVar(value=4)

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
