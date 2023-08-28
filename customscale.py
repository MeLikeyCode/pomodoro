from tkinter import ttk
import time

class CustomScale(ttk.Scale):
    """
    A custom Scale (slider) widget.
    - when the slider is dragged and then *released*, the "command" callback is called
    - when the slider is not being dragged, it will constantly increment its position at a certain rate (client specified)
        - rate is specified in percentage (of the whole slider) per second
    - when the slider reaches the end, it will call the "on_end" callback and stop moving
    """

    def __init__(self, master=None, **kwargs):
        self._command = kwargs.pop("command", None)
        self.rate = kwargs.pop("rate", 0)
        self.on_end = kwargs.pop("on_end", None)
        super().__init__(master, **kwargs)

        self._MOVE_PERIOD = 50  # ms, how often the slider moves
        self._move_slider = False # should the slider move at the moment?

        self.bind("<ButtonRelease-1>", self._on_slider_released)
        self.bind("<B1-Motion>", self._on_slider_dragged)
        self._being_dragged = False
        self._last_time = None
        self._on_move_slider()

    def _on_slider_released(self, event):
        self._being_dragged = False
        if self._command is not None:
            self._command()

    def _on_slider_dragged(self, event):
        self._being_dragged = True

    def _on_move_slider(self):
        """Executed periodically to move the slider."""
        if not self._being_dragged and self._move_slider == True:
            now = time.time()
            if self._last_time is None:
                self._last_time = now

            dt = now - self._last_time
            current_percentage = self.get() / self["to"]
            new_percentage = current_percentage + (self.rate * dt)
            new_pos = new_percentage * self["to"]
            self.set(new_pos)
            self._last_time = now

            if new_pos >= self["to"]:
                self.move_slider = False
                if self.on_end is not None:
                    self.on_end()

        self.after(self._MOVE_PERIOD, self._on_move_slider)

    @property
    def move_slider(self):
        """Determines if the slider should move at the moment or not."""
        return self._move_slider
    
    @move_slider.setter
    def move_slider(self, value):
        self._move_slider = value
        self._last_time = None