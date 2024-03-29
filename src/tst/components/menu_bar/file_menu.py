import tkinter as tk

from tkinter import filedialog
from ..lyrics_area.translated_lyrics.text_box import TranslatedLyricsTextBox
from ..lyrics_area.original_lyrics.text_box import OriginalLyricsTextBox

class FileMenu(tk.Menu):
    def __init__(
            self,
            parent,
            original_lyrics_text_box: OriginalLyricsTextBox,
            translated_lyrics_text_box: TranslatedLyricsTextBox
        ) -> None:
        super().__init__(parent, tearoff=0)
        self.parent = parent
        self.root = parent.root

        self._original_lyrics_text_box = original_lyrics_text_box
        self._translated_lyrics_text_box = translated_lyrics_text_box

        self.add_command(label='ファイルを開く', command=self._handle_open_file, accelerator='Ctrl+O')
        self.bind_all('<Control-o>', self._handle_open_file)

        self.add_command(label='原文を保存', command=self._handle_save_orig_lyrics, accelerator='Ctrl+W')
        self.bind_all('<Control-w>', self._handle_save_orig_lyrics)

        self.add_command(label='翻訳文を保存', command=self._handle_save_trans_lyrics, accelerator='Ctrl+S')
        self.bind_all('<Control-s>', self._handle_save_trans_lyrics)

        self.add_separator()   # 仕切り線
        self.add_command(label='終了', command=self.root.destroy)

    def _handle_open_file(self, event: tk.Event = None) -> None:
        file = filedialog.askopenfilename(filetypes=[('テキストファイル', '.txt')], initialdir='./')
        if file == () or file == '':
            return
        with open(file, 'r') as f:
            self._original_lyrics_text_box.insert(tk.END, f.read())

    def _handle_save_orig_lyrics(self, event: tk.Event = None) -> None:
        file = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('テキストファイル', '.txt')], initialdir='./')
        if file == () or file == '':
            return
        with open(file, 'w') as f:
            f.write(self._original_lyrics_text_box.get(1.0, tk.END))

    def _handle_save_trans_lyrics(self, event: tk.Event = None) -> None:
        file = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('テキストファイル', '.txt')], initialdir='./')
        if file == () or file == '':
            return
        with open(file, 'w') as f:
            f.write(self._translated_lyrics_text_box.get(1.0, tk.END))
