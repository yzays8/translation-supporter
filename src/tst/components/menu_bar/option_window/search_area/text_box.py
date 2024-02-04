import tkinter as tk

from tkinter import ttk
from configparser import ConfigParser

class SearchTextBox(ttk.Entry):
    def __init__(self, parent, config: ConfigParser) -> None:
        super().__init__(parent, width=70)
        self._config = config
        self.insert(0, self._config['DEFAULT']['Search'])
