import tkinter as tk

from tkinter import ttk

class ClearOriginalLyricsButton(ttk.Button):
    def __init__(self, parent):
        super().__init__(parent, text='クリア', command=lambda: parent.text_box.delete(1.0, tk.END))
        self.parent = parent
        self.root = parent.root
