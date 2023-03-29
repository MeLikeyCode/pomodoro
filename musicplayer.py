import os
import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog
import pygame

class MusicPlayer(tk.Frame):
    """A simple music player GUI. Uses pygame to play audio."""
    
    def __init__(self, master=None):
        super().__init__(master)
        self.paused = False
        self._create_widgets()

    def _create_widgets(self):
        # unicode buttons
        unicode_play = "\u25B6"
        unicode_pause = "\u23F8"
        unicode_open = "📂"
        
        self._play_button = ctk.CTkButton(self, text=f"Play {unicode_play}", command=self.play)
        self._pause_button = ctk.CTkButton(self, text=f"Pause {unicode_pause}", command=self.pause)

        self._seek_scale = ctk.CTkSlider(self, from_=0, to=100, orient=tk.HORIZONTAL, command=self.seek)
        self._seek_scale.set(0) # set the slider to 0 initially

        self._title_label = ctk.CTkLabel(self, text="No track loaded",wraplength=200)

        self._load_button = ctk.CTkButton(self, text=f"Load {unicode_open}", command=self.load_track)

        self._pack_widgets("play")

        pygame.mixer.init()


    def _pack_widgets(self, play_or_pause):
        """Pack the widgets of the music player. `play_or_pause` determines whether the play or pause button is shown."""

        # remove all widgets
        self._play_button.pack_forget()
        self._seek_scale.pack_forget()
        self._title_label.pack_forget()
        self._load_button.pack_forget()
        self._pause_button.pack_forget()

        # add them back in the correct order
        if play_or_pause == "pause":
            self._play_button.pack_forget()
            self._pause_button.pack(side="left")
        elif play_or_pause == "play":
            self._pause_button.pack_forget()
            self._play_button.pack(side="left")
        self._seek_scale.pack(side="left", fill=tk.X, expand=True)
        self._title_label.pack(side="left")
        self._load_button.pack(side="left")


    def play(self):
        if self.paused:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.play()

        self._pack_widgets("pause")

    def pause(self):
        self.paused = True
        pygame.mixer.music.pause()
        self._pack_widgets("play")

    def stop(self):
        pygame.mixer.music.stop()

    def seek(self, position):
        pygame.mixer.music.set_pos(int(position))

    def load_track(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav;*.ogg")])
        if file_path:
            pygame.mixer.music.stop()
            self.paused = False
            pygame.mixer.music.load(file_path)
            self._title_label.config(text=os.path.basename(file_path))