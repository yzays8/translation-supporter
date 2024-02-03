import tkinter as tk

from tkinter import ttk

from .original_lyrics.frame import OriginalLyricsFrame
from .translated_lyrics.frame import TranslatedLyricsFrame

class LyricsArea(ttk.Frame):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.parent = parent
        self.root = parent.root

        self.original_lyrics_frame = OriginalLyricsFrame(self)
        self.translated_lyrics_frame = TranslatedLyricsFrame(self)

        self._create_widgets()

    def _create_widgets(self) -> None:
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.original_lyrics_frame.grid(column=0, row=0, padx=10, pady=5, sticky=tk.W+tk.E+tk.N+tk.S)
        self.translated_lyrics_frame.grid(column=1, row=0, padx=10, pady=5, sticky=tk.W+tk.E+tk.N+tk.S)
