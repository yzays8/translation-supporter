import tkinter as tk
from tkinter import ttk

class TranslatedLyricsLabel(ttk.Label):
    def __init__(self, parent):
        super().__init__(parent, text='翻訳文')
        self.parent = parent
        self.root = parent.root
