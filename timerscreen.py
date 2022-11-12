import customtkinter as ctk
from PIL import ImageTk, Image

class TimerScreen(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        stop_image = ImageTk.PhotoImage(Image.open("stop.png").resize((100, 100)))

        activity = ctk.CTkLabel(self,text="work",text_font=("Helvetica", 25))
        time_remaining = ctk.CTkLabel(self, text="13:58",text_font=("Helvetica", 40))
        stop_button = ctk.CTkButton(self, text="stop", image=stop_image, compound=ctk.TOP)

        activity.pack(padx=10, pady=10, fill=ctk.X)
        time_remaining.pack(padx=10, pady=10, fill=ctk.X)
        stop_button.pack(padx=10, pady=10, fill=ctk.X)

        works_done_frame = ctk.CTkFrame(self)
        rounds_done_frame = ctk.CTkFrame(self)
        
        works_done = ctk.CTkLabel(works_done_frame, text="works done: ",anchor=ctk.E)
        works_done_value = ctk.CTkLabel(works_done_frame, text="0",anchor=ctk.W)
        rounds_done = ctk.CTkLabel(rounds_done_frame, text="rounds done: ",anchor=ctk.E)
        rounds_done_value = ctk.CTkLabel(rounds_done_frame, text="0",anchor=ctk.W)

        works_done.pack(side=ctk.LEFT)
        works_done_value.pack(side=ctk.LEFT)
        rounds_done.pack(side=ctk.LEFT)
        rounds_done_value.pack(side=ctk.LEFT)

        works_done_frame.pack()
        rounds_done_frame.pack()

