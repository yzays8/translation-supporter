import tkinter as tk

from tkinter import ttk

from .log_window import LogWindow
from .text_box import CommandInputBox

class IOArea(ttk.Frame):
    def __init__(self, parent=None) -> None:
        super().__init__(parent, width=540, height=100, borderwidth=3)
        self.parent = parent
        self.root = parent.root

        self._log_window = LogWindow(self)
        self._command_input_box = CommandInputBox(self)

        self._create_widgets()

    def handle_enter(self, event: tk.Event = None) -> None:
        self.parent.fetch_lyrics()

    def _create_widgets(self) -> None:
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self._log_window.grid(column=0, row=0, sticky=tk.W+tk.E+tk.N+tk.S)
        self._command_input_box.grid(column=0, row=1, pady=5, sticky=tk.W+tk.E)
