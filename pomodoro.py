import customtkinter as ctk

class Pomodoro(ctk.CTkFrame):
    """Pomodoro widget."""
    def __init__(self,master):
        super().__init__(master)
        
        session_label = ctk.CTkLabel(self,text="test")
        start_button = ctk.CTkButton(self,text="start")

        session_label.grid(row=0,column=0)
        start_button.grid(row=1,column=0)

        self['borderwidth'] = 1
        self['relief'] = ctk.SOLID

        self.grid_columnconfigure(0,weight=1)

        self.periodic()

    def periodic(self):
        print("test")
        self.after(1000,self.periodic)


