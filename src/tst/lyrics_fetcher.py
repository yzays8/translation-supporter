import logging
import requests.exceptions

from lyricsgenius import Genius
from tkinter.scrolledtext import ScrolledText

from .components.io_area.log_window import LogWindow

class LyricsFetcher():
    def __init__(self, token: str = '') -> None:
        self._token = token
        self._logger = logging.getLogger(__name__)
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self._logger.setLevel(logging.DEBUG)
        self._logger.addHandler(handler)

    def get_lyrics(
            self,
            log_window: LogWindow,
            artist_name: str,
            song_name: str,
            output_form: ScrolledText,
            limit: int = 1
        ) -> None:
        try:
            genius = Genius(self._token)
            genius.verbose = False
            genius.remove_section_headers = True

            # Search for the artist
            song_list = genius.search_artist(artist_name, max_songs=limit)
            if song_list is None:
                self._logger.error('search artist error')
                log_window.write('search artist error\n\nEnter artist name: ')
                return

            # Search for the song
            if (song := song_list.song(song_name)) is None:
                self._logger.error('Failed to retrieve lyrics')
                log_window.write('Failed to retrieve lyrics!\n\nEnter artist name: ')
            else:
                self._logger.info('Retrieved lyrics')
                log_window.write('Retrieved lyrics!\n\nEnter artist name: ')
                output_form.insert('end', song.lyrics)

        except requests.exceptions.HTTPError as e:
            self._logger.error('HTTPError exception')
            log_window.write('Token is expired...\n\nEnter artist name: ')
        except requests.exceptions.ConnectionError as e:
            self._logger.error('ConnectionError exception')
            log_window.write('Connection Error...\n\nEnter artist name: ')
        except requests.exceptions.Timeout as e:
            self._logger.error('Timeout exception')
            log_window.write('Timeout Error...\n\nEnter artist name: ')
        except Exception as e:
            self._logger.error(f'Unknown Exception: {e}')
            log_window.write(f'Unknown Error: {e}\n\nEnter artist name: ')

    def set_token(self, token: str) -> None:
        self._token = token

    def get_token(self) -> str:
        return self._token
