import tkinter as tk

from tkinter.scrolledtext import ScrolledText

class LogWindow(ScrolledText):
    def __init__(self, parent):
        super().__init__(parent)

        # Prevents the user from editing the log
        self.configure(state='disabled')

        self.write('Enter artist name: ')

    def write(self, text: str) -> None:
        self.configure(state='normal')
        self.insert(tk.END, text)

        # Autoscrolls to the bottom of the log
        self.see(tk.END)
        self.configure(state='disabled')

    def delete(self) -> None:
        self.delete(1.0, tk.END)
