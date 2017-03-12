import os
import mutagen

# Dictionary for ID3v2.4.0 tags
ID3v24 = {"title": "TIT2", "artist": "TPE1", "album": "TALB", "track": "TRCK", "year": "TDRC", "genre": "TCON",
          "comment": "COMM"}

def readDirectory(path):
    return os.listdir(path)


def filterMP3(list):
    mp3List = []
    for element in list:
        if ".mp3" in element:
            mp3List.append(element)
    return mp3List


def getTitle(song):
    song = mutagen.File(song)
    return song[ID3v24['title']].text[0]


def getArtist(song):
    song = mutagen.File(song)
    return song[ID3v24['artist']].text[0]

def getAlbum(song):
    song = mutagen.File(song)
    return song[ID3v24['album']].text[0]

def getTrack(song):
    song = mutagen.File(song)
    return song[ID3v24['track']].text[0]

def getYear(song):
    song = mutagen.File(song)
    return song[ID3v24['year']].text[0]

def getGenre(song):
    song = mutagen.File(song)
    return song[ID3v24['genre']].text[0]