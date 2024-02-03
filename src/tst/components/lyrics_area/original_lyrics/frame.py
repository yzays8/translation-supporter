import tkinter as tk

from tkinter import ttk

from .label import OriginalLyricsLabel
from .save_button import SaveOriginalLyricsButton
from .clear_button import ClearOriginalLyricsButton
from .text_box import OriginalLyricsTextBox

class OriginalLyricsFrame(ttk.Frame):
    def __init__(self, parent=None) -> None:
        super().__init__(parent, width=280, height=500, borderwidth=3)
        self.parent = parent
        self.root = parent.root

        self.label = OriginalLyricsLabel(self)
        self.save_button = SaveOriginalLyricsButton(self)
        self.clear_button = ClearOriginalLyricsButton(self)
        self.text_box = OriginalLyricsTextBox(self)

        self._create_widgets()

    def _create_widgets(self) -> None:
        self.grid_propagate(0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.label.grid(column=0, row=0)
        self.text_box.grid(column=0, row=1, sticky=tk.W+tk.E+tk.N+tk.S)
        self.clear_button.grid(column=0, row=2, pady=5)
        self.save_button.grid(column=0, row=3, pady=5)
