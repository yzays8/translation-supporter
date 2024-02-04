import tkinter as tk

from tkinter import ttk
from configparser import ConfigParser

from .label import SearchLabel
from .text_box import SearchTextBox

class SearchArea(ttk.Frame):
    def __init__(self, parent, config: ConfigParser) -> None:
        super().__init__(parent)
        self.parent = parent
        self.root = parent.root
        self._config = config

        self._label = SearchLabel(self)
        self.text_box = SearchTextBox(self, self._config)

        self._create_widgets()

    def _create_widgets(self) -> None:
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self._label.grid(row=0, column=0, padx=5, pady=5)
        self.text_box.grid(row=0, column=1, padx=5, pady=5)
