import customtkinter as ctk

class Settings(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        self.grid_columnconfigure(1,weight=1)

        l1 = ctk.CTkLabel(self, text="work length (minutes): ")
        l2 = ctk.CTkLabel(self, text="short break length (minutes): ")
        l3 = ctk.CTkLabel(self, text="long break length (minutes): ")
        l4 = ctk.CTkLabel(self, text="number of works before long break: ")

        e1 = ctk.CTkEntry(self)
        e2 = ctk.CTkEntry(self)
        e3 = ctk.CTkEntry(self)
        e4 = ctk.CTkEntry(self)

        l1.grid(row=0,column=0,sticky=ctk.W)
        l2.grid(row=1,column=0,sticky=ctk.W)
        l3.grid(row=2,column=0,sticky=ctk.W)
        l4.grid(row=3,column=0,sticky=ctk.W)

        e1.grid(row=0,column=1,sticky=ctk.EW)
        e2.grid(row=1,column=1,sticky=ctk.EW)
        e3.grid(row=2,column=1,sticky=ctk.EW)
        e4.grid(row=3,column=1,sticky=ctk.EW)

        buttons_frame = ctk.CTkFrame(self)
        buttons_frame.grid(row=4,columnspan=2,sticky=ctk.E)
        
        ok_button = ctk.CTkButton(buttons_frame,text="Save",command=self._on_save)
        cancel_button = ctk.CTkButton(buttons_frame,text="Cancel",command=self._on_cancel)

        ok_button.pack(side=ctk.LEFT)
        cancel_button.pack(side=ctk.LEFT)

    def _on_save(self):
        pass # TODO implement

    def _on_cancel(self):
        pass # TODO implement
        
