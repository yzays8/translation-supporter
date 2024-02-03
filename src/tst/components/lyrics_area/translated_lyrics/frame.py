import tkinter as tk

from tkinter import ttk

from .label import TranslatedLyricsLabel
from .save_button import SaveTranslatedLyricsButton
from .clear_button import ClearTranslatedLyricsButton
from .text_box import TranslatedLyricsTextBox

class TranslatedLyricsFrame(ttk.Frame):
    def __init__(self, parent=None) -> None:
        super().__init__(parent, width=280, height=500, borderwidth=3)
        self.parent = parent
        self.root = parent.root

        self.label = TranslatedLyricsLabel(self)
        self.save_button = SaveTranslatedLyricsButton(self)
        self.clear_button = ClearTranslatedLyricsButton(self)
        self.text_box = TranslatedLyricsTextBox(self)

        self._create_widgets()

    def _create_widgets(self) -> None:
        self.grid_propagate(0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.label.grid(column=0, row=0)
        self.text_box.grid(column=0, row=1, sticky=tk.W+tk.E+tk.N+tk.S)
        self.clear_button.grid(column=0, row=2, pady=5)
        self.save_button.grid(column=0, row=3, pady=5)
