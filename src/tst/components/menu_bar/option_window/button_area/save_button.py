import os
import sys
import tkinter as tk

from collections.abc import Callable
from configparser import ConfigParser
from tkinter import ttk

from ..token_area.text_box import TokenTextBox
from ..search_area.text_box import SearchTextBox

class SaveButton(ttk.Button):
    CONFIG_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../../option.ini'))
    sys.path.append(CONFIG_PATH)

    def __init__(
            self,
            parent,
            config: ConfigParser,
            text_box_token: TokenTextBox,
            text_box_search: SearchTextBox,
            destroy_window: Callable[[], None]
        ) -> None:
        super().__init__(parent, text='保存', command=lambda: self._handle_save(config))
        self._parent = parent
        self._config = config
        self.text_box_token = text_box_token
        self.text_box_search = text_box_search
        self.destroy_window = destroy_window

    def _handle_save(self, event: tk.Event = None) -> None:
        self._config['CLIENT']['CLIENT_ACCESS_TOKEN'] = self.text_box_token.get()
        self._config['DEFAULT']['Search'] = self.text_box_search.get()
        with open(self.CONFIG_PATH, 'w') as configfile:
            self._config.write(configfile)
        self.destroy_window()
