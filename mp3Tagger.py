import os
import mutagen


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
    return audio['TIT2'].text[0]


def getArtist(song):
    audio = mutagen.File(song)
    return audio['TPE1'].text[0]