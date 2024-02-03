import tkinter as tk

from configparser import ConfigParser

from .file_menu import FileMenu
from .option_menu import OptionMenu

class MenuBar(tk.Menu):
    def __init__(self, parent, config: ConfigParser) -> None:
        super().__init__(parent)
        self.parent = parent
        self.root = parent.root

        self._file_menu = FileMenu(self)
        self.add_cascade(label='ファイル', menu=self._file_menu)

        self._option_menu = OptionMenu(self, config)
        self.add_cascade(label='オプション', menu=self._option_menu)