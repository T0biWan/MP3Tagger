import os
import mutagen

# Dictionary for ID3v2.4.0 tags
ID3v24 = {"title": "TIT2", "artist": "TPE1", "album": "TALB"}

def readDirectory(path):
    return os.listdir(path)


def filterMP3(list):
    mp3List = []
    for element in list:
        if ".mp3" in element:
            mp3List.append(element)
    return mp3List


def getTitle(song):
    audio = mutagen.File(song)
    return audio[ID3v24['title']].text[0]


def getArtist(song):
    audio = mutagen.File(song)
    return audio[ID3v24['artist']].text[0]

def getAlbum(song):
    audio = mutagen.File(song)
    return audio[ID3v24['album']].text[0]
