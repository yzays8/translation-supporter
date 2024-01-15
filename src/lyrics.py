import requests.exceptions

from lyricsgenius import Genius

class LyricsFetcher():
    def __init__(self):
        self.token = ''

    def get_lyrics(self, console, artist, name, output_form, limit=1) -> None:
        try:
            genius = Genius(self.token)
            genius.verbose = False
            genius.remove_section_headers = True

            if (song_list := genius.search_artist(artist, max_songs=limit)) is None :
                console.write('search artist error\n\nEnter artist name: ')
            if (song := song_list.song(name)) is None:
                print('Failed to retrieve lyrics!\n')
                console.write('Failed to retrieve lyrics!\n\nEnter artist name: ')
            else:
                print('Retrieved lyrics!\n')
                console.write('Retrieved lyrics!\n\nEnter artist name: ')
                output_form.insert('end', song.lyrics)
        except requests.exceptions.HTTPError as e:
            console.write('Token is expired...\n\nEnter artist name: ')
        except requests.exceptions.ConnectionError as e:
            console.write('Connection Error...\n\nEnter artist name: ')
        except requests.exceptions.Timeout as e:
            console.write('Timeout Error...\n\nEnter artist name: ')
        except Exception as e:
            console.write(f'Unknown Error: {e}\n\nEnter artist name: ')

    def set_token(self, token: str) -> None:
        self.token = token

    def get_token(self) -> str:
        return self.token
