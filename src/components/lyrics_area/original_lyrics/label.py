import tkinter as tk
from tkinter import ttk

class OriginalLyricsLabel(ttk.Label):
    def __init__(self, parent):
        super().__init__(parent, text='原文')
        self.parent = parent
        self.root = parent.root
