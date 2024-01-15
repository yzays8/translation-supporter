import tkinter as tk

class LogWindow():
    def __init__(self, widget, autoscroll=True):
        self.widget = widget
        self.autoscroll = autoscroll

    def write(self, text: str) -> None:
        self.widget.configure(state='normal')
        self.widget.insert(tk.END, text)
        #self.widget.insert(tk.END, '\n')
        if self.autoscroll:
            self.widget.see(tk.END)
        self.widget.configure(state='disabled')

    def delete(self) -> None:
        self.widget.delete(1.0, tk.END)