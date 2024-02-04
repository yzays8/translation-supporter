import threading
import configparser

import tkinter as tk

from tkinter import ttk

from .lyrics_fetcher import LyricsFetcher
from . import components

class App(ttk.Frame):
    CONFIG_PATH = 'option.ini'

    def __init__(self, master=None) -> None:
        super().__init__(master, borderwidth=3)
        self.root = master
        self.root.title('Translation Support Tool')
        self.root.geometry('600x900')

        self.pack(fill=tk.BOTH, expand=True)
        self.pack_propagate(0)

        self._is_waiting_song_name = False
        self._artist_name = ''
        self.config = configparser.ConfigParser()

        self._lyrics_fetcher = LyricsFetcher()
        self._lyrics_area = components.LyricsArea(self, self.highlight)
        self._io_area = components.IOArea(self)

        # Menu bar
        ot = self._lyrics_area.original_lyrics_frame.text_box
        tt = self._lyrics_area.translated_lyrics_frame.text_box
        self.menu_bar = components.MenuBar(self, self.config, ot, tt)
        self.root.config(menu=self.menu_bar)

        self._create_widgets()

    def _create_widgets(self) -> None:
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self._lyrics_area.grid(column=0, row=0, padx=10, pady=5, sticky=tk.W+tk.E+tk.N+tk.S)
        self._io_area.grid(column=0, row=1, columnspan=2, padx=10, pady=5, sticky=tk.W+tk.E+tk.N+tk.S)

    def highlight(self, line_start: str, line_end: str) -> None:
        self._lyrics_area.original_lyrics_frame.text_box.tag_remove('highlight', '1.0', 'end')
        self._lyrics_area.original_lyrics_frame.text_box.tag_add('highlight', line_start, line_end)
        self._lyrics_area.translated_lyrics_frame.text_box.tag_remove('highlight', '1.0', 'end')
        self._lyrics_area.translated_lyrics_frame.text_box.tag_add('highlight', line_start, line_end)

    def fetch_lyrics(self) -> None:
        for th in threading.enumerate():
            if th.name == 'fetching_lyrics':
                break
        else:
            self.config.read(self.CONFIG_PATH)
            self._lyrics_fetcher.set_token(self.config['CLIENT']['CLIENT_ACCESS_TOKEN'])

            # Wait for the artist name to be entered
            if (artist_name := self._io_area._command_input_box.get()) != '' and not self._is_waiting_song_name:
                self._artist_name = artist_name
                self._io_area._log_window.write(f'{artist_name}\n')
                self._io_area._log_window.write('Enter song name: ')
                self._io_area._command_input_box.delete(0, tk.END)
                self._is_waiting_song_name = True

            # Wait for the song name to be entered
            if (song_name := self._io_area._command_input_box.get()) != '' and self._is_waiting_song_name:
                self._is_waiting_song_name = False
                self._io_area._command_input_box.delete(0, tk.END)
                self._io_area._log_window.write(f'{song_name}\n')
                self.connection_thread = threading.Thread(name='fetching_lyrics', target=lambda:
                    self._lyrics_fetcher.get_lyrics(self._io_area._log_window, self._artist_name, song_name, self._lyrics_area.original_lyrics_frame.text_box)
                ).start()

def start_app() -> None:
    root = tk.Tk()
    app = App(master=root)
    app.mainloop()
