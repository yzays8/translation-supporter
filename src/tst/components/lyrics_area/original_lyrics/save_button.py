import tkinter as tk

from tkinter import ttk
from tkinter import filedialog

class SaveOriginalLyricsButton(ttk.Button):
    def __init__(self, parent):
        super().__init__(parent, text='保存', command=self.handle_click)
        self.parent = parent
        self.root = parent.root

    def handle_click(self, event=None) -> None:
        file = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('テキストファイル', '.txt')], initialdir='./')
        if file == () or file == '':
            return
        with open(file, 'w') as f:
            f.write(self.parent.text_box.get(1.0, tk.END))
