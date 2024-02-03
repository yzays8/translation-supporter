import tkinter as tk

from tkinter import ttk
from tkinter import filedialog

class SaveOriginalLyricsButton(ttk.Button):
    def __init__(self, parent) -> None:
        super().__init__(parent, text='保存', command=self._handle_click)
        self.parent = parent

    def _handle_click(self, event: tk.Event = None) -> None:
        file = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('テキストファイル', '.txt')], initialdir='./')
        if file == () or file == '':
            return
        with open(file, 'w') as f:
            f.write(self.parent.text_box.get(1.0, tk.END))
