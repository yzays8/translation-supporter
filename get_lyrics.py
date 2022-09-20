from urllib.error import HTTPError
from lyricsgenius import Genius
import requests.exceptions

class GetLyrics():
    def __init__(self):
        self.token = ''
        self.lyrics = ''

    def get_lyrics(self, console, artist, name, output_form, limit=1):
        try:
            genius = Genius(self.token)
            genius.verbose = False
            genius.remove_section_headers = True

            if (song_list:=genius.search_artist(artist, max_songs=limit)) is None :
                console.write('search artist error\n\nEnter artist name: ')
            if (song:=song_list.song(name)) is None:
                print('Failed to retrieve lyrics!\n')
                console.write('Failed to retrieve lyrics!\n\nEnter artist name: ')
            else:
                print('Retrieved lyrics!\n')
                console.write('Retrieved lyrics!\n\nEnter artist name: ')
                output_form.insert('end', song.lyrics)
        except requests.exceptions.HTTPError as e:
            console.write('Token is expired...\n\nEnter artist name: ')

    def set_token(self, token):
        self.token = token

    def get_token(self):
        return self.token