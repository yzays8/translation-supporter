import tkinter as tk

from typing import Callable
from tkinter import ttk

class CancelButton(ttk.Button):
    def __init__(self, parent, destroy_window: Callable[[], None]) -> None:
        super().__init__(parent, text='キャンセル', command=destroy_window)
