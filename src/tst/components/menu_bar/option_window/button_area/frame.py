from typing import Callable
from configparser import ConfigParser
from tkinter import ttk

from .save_button import SaveButton
from .cancel_button import CancelButton
from ..token_area.text_box import TokenTextBox
from ..search_area.text_box import SearchTextBox

class ButtonArea(ttk.Frame):
    def __init__(
            self,
            parent,
            config: ConfigParser,
            text_box_token: TokenTextBox,
            text_box_search: SearchTextBox,
            destroy_window: Callable[[], None]
        ) -> None:
        super().__init__(parent)
        self._parent = parent
        self._config = config

        self._save_button = SaveButton(self, self._config, text_box_token, text_box_search, destroy_window)
        self._cancel_button = CancelButton(self, destroy_window)

        self._create_widgets()

    def _create_widgets(self) -> None:
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self._save_button.grid(row=0, column=0, padx=5, pady=5)
        self._cancel_button.grid(row=0, column=1, padx=5, pady=5)
