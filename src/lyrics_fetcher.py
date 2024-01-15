import requests.exceptions

from lyricsgenius import Genius
from tkinter.scrolledtext import ScrolledText

from components.io_area.log_window import LogWindow

class LyricsFetcher():
    def __init__(self, token: str = ''):
        self.token = token

    def get_lyrics(self, log_window: LogWindow, artist_name: str, song_name: str, output_form: ScrolledText, limit=1) -> None:
        try:
            genius = Genius(self.token)
            genius.verbose = False
            genius.remove_section_headers = True

            # Search for the artist
            if (song_list := genius.search_artist(artist_name, max_songs=limit)) is None:
                log_window.write('search artist error\n\nEnter artist name: ')

            # Search for the song
            if (song := song_list.song(song_name)) is None:
                print('Failed to retrieve lyrics!')
                log_window.write('Failed to retrieve lyrics!\n\nEnter artist name: ')
            else:
                print('Retrieved lyrics!')
                log_window.write('Retrieved lyrics!\n\nEnter artist name: ')
                output_form.insert('end', song.lyrics)

        except requests.exceptions.HTTPError as e:
            log_window.write('Token is expired...\n\nEnter artist name: ')
        except requests.exceptions.ConnectionError as e:
            log_window.write('Connection Error...\n\nEnter artist name: ')
        except requests.exceptions.Timeout as e:
            log_window.write('Timeout Error...\n\nEnter artist name: ')
        except Exception as e:
            log_window.write(f'Unknown Error: {e}\n\nEnter artist name: ')

    def set_token(self, token: str) -> None:
        self.token = token

    def get_token(self) -> str:
        return self.token
