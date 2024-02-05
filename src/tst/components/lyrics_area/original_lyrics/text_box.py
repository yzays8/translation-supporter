import tkinter as tk

from tkinter.scrolledtext import ScrolledText
from collections.abc import Callable

class OriginalLyricsTextBox(ScrolledText):
    HIGHLIGHT_COLOR = '#7cc7e8'

    def __init__(self, parent, highlight: Callable[[int, int], None]) -> None:
        super().__init__(parent)
        self.parent = parent
        self.highlight = highlight

        # Highlight current line
        self.tag_configure('highlight', background=self.HIGHLIGHT_COLOR)
        self.tag_configure('highlight', background=self.HIGHLIGHT_COLOR)
        self.bind("<KeyRelease>", self._highlight_current_line)
        self.bind("<ButtonRelease-1>", self._highlight_current_line)

    def _highlight_current_line(self, event: tk.Event = None) -> None:
        cursor_pos = self.index(tk.INSERT)
        line_number = int(cursor_pos.split('.')[0])
        line_start = f'{line_number}.0'
        line_end = f'{line_number + 1}.0'

        # Sync the highlighted line with the translated lyrics
        self.highlight(line_start, line_end)
