import tkinter as tk

from configparser import ConfigParser

from .file_menu import FileMenu
from .option_menu import OptionMenu
from ..lyrics_area.translated_lyrics.text_box import TranslatedLyricsTextBox
from ..lyrics_area.original_lyrics.text_box import OriginalLyricsTextBox

class MenuBar(tk.Menu):
    def __init__(
            self,
            parent,
            config: ConfigParser,
            original_lyrics_text_box: OriginalLyricsTextBox,
            translated_lyrics_text_box: TranslatedLyricsTextBox
        ) -> None:
        super().__init__(parent)
        self.parent = parent
        self.root = parent.root

        self._file_menu = FileMenu(self, original_lyrics_text_box, translated_lyrics_text_box)
        self.add_cascade(label='ファイル', menu=self._file_menu)

        self._option_menu = OptionMenu(self, config)
        self.add_cascade(label='オプション', menu=self._option_menu)