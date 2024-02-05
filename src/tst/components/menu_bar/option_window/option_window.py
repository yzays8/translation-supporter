import os
import sys
import tkinter as tk

from tkinter import ttk
from configparser import ConfigParser

from .token_area import TokenArea
from .search_area import SearchArea
from .button_area import ButtonArea

class OptionWindow(tk.Toplevel):
    CONFIG_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../option.ini'))
    sys.path.append(CONFIG_PATH)

    def __init__(self, parent, config: ConfigParser) -> None:
        super().__init__(parent)
        self.parent = parent
        self.root = parent.root
        self.title('設定')
        self.geometry('800x200')
        self.resizable(False, False)

        self._config = config
        self._setup_config()

        self._token_area = TokenArea(self, self._config)
        self._search_area = SearchArea(self, self._config)
        tt = self._token_area.text_box
        st = self._search_area.text_box
        self._button_area = ButtonArea(self, self._config, tt, st, self.destroy)

        self._create_widgets()

    def open(self) -> None:
        self.mainloop()

    def _setup_config(self) -> None:
        if os.path.exists(self.CONFIG_PATH):
            self._config.read(self.CONFIG_PATH)
        else:
            self._config['CLIENT'] = {
                'CLIENT_ID' : 'default',
                'CLIENT_SECRET' : 'default',
                'CLIENT_ACCESS_TOKEN' : 'default'
            }
            self._config['DEFAULT']['Search'] = '0'
            with open(self.CONFIG_PATH, 'w') as configfile:
                self._config.write(configfile)

    def _create_widgets(self) -> None:
        self.grid_rowconfigure(0, weight=1)

        self._token_area.grid(row=0, column=0, padx=5, pady=5)
        self._search_area.grid(row=1, column=0, padx=5, pady=5)
        self._button_area.grid(row=2, column=0, padx=5, pady=5)
