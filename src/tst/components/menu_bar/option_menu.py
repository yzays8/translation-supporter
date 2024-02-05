import tkinter as tk

from configparser import ConfigParser

from .option_window import OptionWindow

class OptionMenu(tk.Menu):
    def __init__(self, parent, config: ConfigParser) -> None:
        super().__init__(parent, tearoff=0)
        self.parent = parent
        self.root = parent.root

        self._config = config
        self.add_command(label='設定', command=self._handle_open_option)

    def _handle_open_option(self, event: tk.Event = None) -> None:
        OptionWindow(self.parent, self._config).open()
