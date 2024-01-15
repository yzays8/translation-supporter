import tkinter as tk

from tkinter import ttk

class CommandInputBox(ttk.Entry):
    def __init__(self, parent):
        self.string_var = tk.StringVar(parent)
        self.default_text = 'アーティスト名を入力してください'
        self.string_var.set(self.default_text)
        super().__init__(parent, textvariable=self.string_var, foreground='gray')
        self.parent = parent
        self.root = parent.root

        self.bind('<Button-1>', self.handle_click)
        self.bind('<Return>', self.handle_enter)

    def handle_click(self, event):
        self.config(foreground='black')
        if self.get() == self.default_text:
            event.widget.delete(0, tk.END)
        else:
            self.config(foreground='black')

    def handle_enter(self, event):
        self.parent.handle_enter()