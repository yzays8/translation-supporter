import tkinter as tk

from configparser import ConfigParser

from .file_menu import FileMenu
from .option_menu import OptionMenu

class MenuBar(tk.Menu):
    def __init__(self, parent, config: ConfigParser):
        super().__init__(parent)
        self.parent = parent
        self.root = parent.root

        self.file_menu = FileMenu(self)
        self.add_cascade(label='ファイル', menu=self.file_menu)

        self.option_menu = OptionMenu(self, config)
        self.add_cascade(label='オプション', menu=self.option_menu)