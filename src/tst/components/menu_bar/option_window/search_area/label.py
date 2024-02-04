import tkinter as tk

from tkinter import ttk

class SearchLabel(ttk.Label):
    def __init__(self, parent) -> None:
        super().__init__(parent, text='曲リストの検索数         :')
