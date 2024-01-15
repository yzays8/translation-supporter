import tkinter as tk

from tkinter import filedialog

class FileMenu(tk.Menu):
    def __init__(self, parent):
        super().__init__(parent, tearoff=0)
        self.parent = parent
        self.root = parent.root

        self.add_command(label='ファイルを開く', command=self.handle_open_file, accelerator='Ctrl+O')
        self.bind_all('<Control-o>', self.handle_open_file)

        self.add_command(label='原文を保存', command=self.handle_save_orig_lyrics, accelerator='Ctrl+W')
        self.bind_all('<Control-w>', self.handle_save_orig_lyrics)

        self.add_command(label='翻訳文を保存', command=self.handle_save_trans_lyrics, accelerator='Ctrl+S')
        self.bind_all('<Control-s>', self.handle_save_trans_lyrics)

        self.add_separator()   # 仕切り線
        self.add_command(label='終了', command=self.root.destroy)

    def handle_open_file(self, event=None):
        file = filedialog.askopenfilename(filetypes=[('テキストファイル', '.txt')], initialdir='./')
        if file == () or file == '':
            return
        with open(file, 'r') as f:
            self.textbox_frame_right.insert(tk.END, f.read())

    def handle_save_orig_lyrics(self, event=None):
        file = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('テキストファイル', '.txt')], initialdir='./')
        if file == () or file == '':
            return
        with open(file, 'w') as f:
            f.write(self.textbox_frame_left.get(1.0, tk.END))

    def handle_save_trans_lyrics(self, event=None):
        file = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('テキストファイル', '.txt')], initialdir='./')
        if file == () or file == '':
            return
        with open(file, 'w') as f:
            f.write(self.textbox_frame_right.get(1.0, tk.END))