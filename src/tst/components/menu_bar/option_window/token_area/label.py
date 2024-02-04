import tkinter as tk

from tkinter import ttk

class TokenLabel(ttk.Label):
    def __init__(self, parent) -> None:
        super().__init__(parent, text='Client Access Token :')
