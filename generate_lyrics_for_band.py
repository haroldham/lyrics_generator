import markovify
import sys
from artist_lyrics_objects import *


band_name = sys.argv[1]

band = Band(band_name)

all_band_lyrics = ""
for song in band.songs:
    all_band_lyrics = "{}\n{}".format(all_band_lyrics, song.lyrics)

band_lyrics_model = markovify.Text(all_band_lyrics)

print(band_lyrics_model.make_sentence().capitalize())
