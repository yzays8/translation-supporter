from tkinter import INSERT
from tkinter.scrolledtext import ScrolledText

class TranslatedLyricsTextBox(ScrolledText):
    HIGHLIGHT_COLOR = '#7cc7e8'

    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.parent = parent
        self.root = parent.root

        # Highlight current line
        self.tag_configure('highlight', background=self.HIGHLIGHT_COLOR)
        self.tag_configure('highlight', background=self.HIGHLIGHT_COLOR)
        self.bind("<KeyRelease>", self._highlight_current_line)
        self.bind("<ButtonRelease-1>", self._highlight_current_line)

    def _highlight_current_line(self) -> None:
        cursor_pos = self.index(INSERT)
        line_number = int(cursor_pos.split('.')[0])
        line_start = f'{line_number}.0'
        line_end = f'{line_number + 1}.0'
        self.tag_remove('highlight', '1.0', 'end')
        self.tag_add('highlight', line_start, line_end)

        # Sync the highlighted line with the original lyrics
        self.parent.parent.original_lyrics_frame.text_box.tag_remove('highlight', '1.0', 'end')
        self.parent.parent.original_lyrics_frame.text_box.tag_add('highlight', line_start, line_end)
