from tkinter import ttk

class CustomScale(ttk.Scale):
    """
    A custom Scale (slider) widget.
    - when the slider is dragged and then released, the "command" callback is called
    - when the slider is not being dragged, "get_pos" callback is called. The return value of "get_pos" is used to set the slider's position.
    """

    def __init__(self, master=None, **kwargs):
        self._command = kwargs.pop("command", None)
        self._get_pos = kwargs.pop("get_pos", None)
        super().__init__(master, **kwargs)

        self.bind("<ButtonRelease-1>", self._on_slider_released)
        self.bind("<B1-Motion>", self._on_slider_dragged)
        self._being_dragged = False
        self._update_slider()

    def _on_slider_released(self, event):
        self._being_dragged = False
        if self._command is not None:
            self._command()

    def _on_slider_dragged(self, event):
        self._being_dragged = True

    def _update_slider(self):
        if not self._being_dragged and self._get_pos is not None:
            self.set(self._get_pos())
            print(f"slider updated from music, to {self.get()}")
        self.after(100, self._update_slider)


    