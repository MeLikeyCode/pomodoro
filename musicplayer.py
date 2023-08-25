import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import customtkinter as ctk
import pygame
import os
from youtube_audio import YouTubeAudioPlayer
import tempfile


class LocalMusicPlayer:
    def __init__(self, filepath):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(filepath)

    def play(self, loops):
        pygame.mixer.music.play(loops)

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    def stop(self):
        pygame.mixer.music.stop()

    def seek(self, value):
        pygame.mixer.music.set_pos(value)


class YouTubeMusicPlayer:
    def __init__(self, url):
        self._url = url
        self._player = YouTubeAudioPlayer(url)
        self._paused = False 
        self._playing = False
        self._paused_at = 0  # in seconds

    def play(self, loops):
        # TODO handle looping (if -1 loop forever)
        self._paused = False
        self._playing = True
        self._player.play(self._paused_at)

    def pause(self):
        if not self._paused:
            self._paused = True
            self._paused_at = self._player.position_seconds
            self._player.stop()

    def unpause(self):
        if self._paused:
            self._paused = False
            self._player.play(self._paused_at)

    def stop(self):
        self._player.stop()
        self._paused = False

    def seek(self, value):
        duration = self._player.duration
        seek_time_seconds = (value / 100) * duration
        self._paused_at = seek_time_seconds
        if self._playing:
            self._player.play(seek_time_seconds)


class MusicPlayer(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self._paused = False
        self._seek = 0 # 0 to 100
        self._music_player = None
        
        self._recently_played = []
        # load from file if it exists
        if os.path.isfile(os.path.join(tempfile.gettempdir(), "pom_music_player.txt")):
            with open(os.path.join(tempfile.gettempdir(), "pom_music_player.txt"), "r") as f:
                self._recently_played = f.read().split("\n")

        self._create_widgets()

    def _create_widgets(self):
        # unicode buttons
        unicode_play = "\u25B6"
        unicode_pause = "\u23F8"
        unicode_open = "📂"

        self._play_button = ctk.CTkButton(
            self, text=f"Play {unicode_play}", command=self.play
        )
        self._pause_button = ctk.CTkButton(
            self, text=f"Pause {unicode_pause}", command=self.pause
        )

        self._filepath_stringvar = tk.StringVar()
        self._filepath = ttk.Combobox(
            self, textvariable=self._filepath_stringvar, values=self._recently_played
        )
        self._filepath_stringvar.trace("w", self._on_filepath_changed)

        self._seek_slider = ctk.CTkSlider(
            self, from_=0, to=100, orient=tk.HORIZONTAL, command=self.seek
        )
        self._seek_slider.set(0)

        self._load_button = ctk.CTkButton(
            self, text=f"Browse {unicode_open}", command=self._load_local_track
        )

        self._pack_widgets("play")

    def _pack_widgets(self, play_or_pause):
        # remove all widgets
        self._play_button.grid_forget()
        self._filepath.grid_forget()
        self._seek_slider.grid_forget()
        self._load_button.grid_forget()

        # add them back in the correct order
        if play_or_pause == "pause":
            self._play_button.grid_forget()
            self._pause_button.grid(row=0, column=0, rowspan=2, sticky="nsew")
        elif play_or_pause == "play":
            self._pause_button.grid_forget()
            self._play_button.grid(row=0, column=0, rowspan=2, sticky="nsew")
        self._filepath.grid(row=0, column=1, sticky="nsew")
        self._seek_slider.grid(row=1, column=1, sticky="nsew")
        self._load_button.grid(row=0, column=2, rowspan=2, sticky="nsew")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def _on_filepath_changed(self, *args):
        self._paused = False
        self._seek_slider.set(0)
        self._pack_widgets("play")
        if self._music_player is not None:
            self._music_player.stop()

    def play(self):
        filepath = self._filepath_stringvar.get()

        if filepath == "":
            return

        if self._paused:
            self._music_player.seek(self._seek)
            self._music_player.unpause()
        else:
            if self._music_player is not None:
                self._music_player.stop()
            if os.path.isfile(filepath): # local file
                self._music_player = LocalMusicPlayer(filepath)
            else: # assume it's a youtube url
                self._music_player = YouTubeMusicPlayer(filepath)
            
            self._music_player.play(-1)  # -1 means loop indefinitely

            # add to recently played
            if filepath not in self._recently_played:
                self._recently_played.append(filepath)
                # limit to 10 recently played items
                if len(self._recently_played) > 10:
                    self._recently_played.pop(0)
                self._filepath["values"] = self._recently_played
                with open(os.path.join(tempfile.gettempdir(), "pom_music_player.txt"), "w") as f:
                    f.write("\n".join(self._recently_played))
                
        self._pack_widgets("pause")

    def pause(self):
        self._paused = True
        self._music_player.pause()
        self._pack_widgets("play")

    def stop(self):
        self._music_player.stop()

    def seek(self, value):
        self._seek = value
        self._music_player.seek(value)

    def _load_local_track(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Audio Files", "*.mp3;*.wav;*.ogg")]
        )
        if file_path:
            self._filepath_stringvar.set(file_path)

# manually test the widget
if __name__ == "__main__":
    pygame.mixer.init()
    root = tk.Tk()
    root.title("Music Player")
    music_player = MusicPlayer(root)
    music_player.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
