import tkinter as tk

from tkinter import ttk

class ClearTranslatedLyricsButton(ttk.Button):
    def __init__(self, parent) -> None:
        super().__init__(parent, text='クリア', command=lambda: parent.text_box.delete(1.0, tk.END))
