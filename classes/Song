import time
import requests


class Song:
    def __init__(self, url):
        self.url = url
        self.lyrics = self._get_lyrics()

    def _get_lyrics(self):
        lyrics_start = "<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->"
        lyrics_end = "</div>"
        lyrics_page_html = requests.get(self.url).text
        time.sleep(0.5)

        lyrics = lyrics_page_html.split(lyrics_start)[1].split(lyrics_end)[0]
        for tag in ["<br>", "\\", "<i>", "</i>", ")", "("]:
            lyrics = lyrics.replace(tag, "")
        return lyrics
