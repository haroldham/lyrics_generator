from artist_lyrics_objects.song import Song
from bs4 import BeautifulSoup
import requests


class Band:
    def __init__(self, name):
        self.name = name
        self._band_first_letter = self.name[0].lower()
        self._url = self._format_url()
        self.songs = self._get_band_songs()

    def _format_url(self):
        return "https://www.azlyrics.com/{first_letter}/{band}.html" \
               "".format(first_letter=self._band_first_letter, band=self.name.lower().replace(" ", ""))

    def _get_band_songs(self):
        band_songs = []
        song_urls = self._get_band_song_urls()
        for song_url in song_urls:
            band_songs.append(Song(song_url))

        return band_songs

    def _get_band_song_urls(self):
        band_page_html = requests.get(self._url).text
        lyrics_page_soup = BeautifulSoup(band_page_html, 'html.parser')
        lyrics_page_links = lyrics_page_soup.find_all('a')

        lyrics_page_urls = []
        for lyrics_page_link in lyrics_page_links:
            if lyrics_page_link.has_attr('href'):
                if "/lyrics/" in lyrics_page_link['href']:
                    band_song_lyrics_url = lyrics_page_link['href'].replace("..", "https://www.azlyrics.com")
                    lyrics_page_urls.append(band_song_lyrics_url)
        return lyrics_page_urls
