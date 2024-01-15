import threading
import configparser

import tkinter as tk

import components

from tkinter import ttk
from lyrics_fetcher import LyricsFetcher

class App(ttk.Frame):
    HIGHLIGHT_COLOR = '#7cc7e8'
    CONFIG_PATH = 'option.ini'

    def __init__(self, master=None):
        super().__init__(master, borderwidth=3)
        self.root = master
        self.root.title('Translation Support Tool')
        self.root.geometry('600x900')

        self.pack(fill=tk.BOTH, expand=True)
        self.pack_propagate(0)

        self.is_waiting_song_name = False
        self.artist_name = ''
        self.config = configparser.ConfigParser()

        # Menu bar
        self.menu_bar = components.MenuBar(self, config=self.config)
        self.root.config(menu=self.menu_bar)

        self.lyrics_fetcher = LyricsFetcher()
        self.lyrics_area = components.LyricsArea(self)
        self.io_area = components.IOArea(self)

        self.create_widgets()

    def create_widgets(self) -> None:
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.lyrics_area.grid(column=0, row=0, padx=10, pady=5, sticky=tk.W+tk.E+tk.N+tk.S)
        self.io_area.grid(column=0, row=1, columnspan=2, padx=10, pady=5, sticky=tk.W+tk.E+tk.N+tk.S)

    def fetch_lyrics(self) -> None:
        for th in threading.enumerate():
            if th.name == 'fetching_lyrics':
                break
        else:
            self.config.read(self.CONFIG_PATH)
            self.lyrics_fetcher.set_token(self.config['CLIENT']['CLIENT_ACCESS_TOKEN'])

            # Wait for the artist name to be entered
            if (artist_name := self.io_area.command_input_box.get()) != '' and not self.is_waiting_song_name:
                self.artist_name = artist_name
                self.io_area.log_window.write(f'{artist_name}\n')
                self.io_area.log_window.write('Enter song name: ')
                self.io_area.command_input_box.delete(0, tk.END)
                self.is_waiting_song_name = True

            # Wait for the song name to be entered
            if (song_name := self.io_area.command_input_box.get()) != '' and self.is_waiting_song_name:
                self.is_waiting_song_name = False
                self.io_area.command_input_box.delete(0, tk.END)
                self.io_area.log_window.write(f'{song_name}\n')
                self.connection_thread = threading.Thread(name='fetching_lyrics', target=lambda:
                    self.lyrics_fetcher.get_lyrics(self.io_area.log_window, self.artist_name, song_name, self.lyrics_area.original_lyrics_frame.text_box
                )).start()

def start_app() -> None:
    root = tk.Tk()
    app = App(master=root)
    app.mainloop()
