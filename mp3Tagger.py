import os
import mutagen
from mutagen.easyid3 import EasyID3


def readDirectory(path):
    return os.listdir(path)


def filterMP3(list):
    mp3List = []
    for element in list:
        fileExtension = os.path.splitext(element)[1]
        if fileExtension == ".mp3":
            mp3List.append(element)
    return mp3List


def formatTracknumbersWithLeadingZeros(audio, maxRequiredDigits):
    tracknumber = getTrack(audio)
    numberOfLeadingZeros = maxRequiredDigits - len(str(tracknumber))
    trackNumberWithLeadingZeros = "0" * numberOfLeadingZeros + str(tracknumber)
    setTrack(audio, trackNumberWithLeadingZeros)
    return


def getTitle(audio):
    audio = EasyID3(audio)
    return audio["title"][0]


def getArtist(audio):
    audio = EasyID3(audio)
    return audio["artist"][0]


def getAlbum(audio):
    audio = EasyID3(audio)
    return audio["album"][0]


def getTrack(audio):
    audio = EasyID3(audio)
    return audio["tracknumber"][0]


def getYear(audio):
    audio = EasyID3(audio)
    return audio["date"][0]


def getGenre(audio):
    audio = EasyID3(audio)
    return audio["genre"][0]

def getComment(audio):
    audio = mutagen.File(audio)
    return audio["COMM::eng"].text[0]


def setTitle(audio, title):
    audio = EasyID3(audio)
    audio["title"] = title
    audio.save()
    return audio


def setArtist(audio, artist):
    audio = EasyID3(audio)
    audio["artist"] = artist
    audio.save()
    return audio


def setAlbum(audio, album):
    audio = EasyID3(audio)
    audio["album"] = album
    audio.save()
    return audio


def setTrack(audio, track):
    audio = EasyID3(audio)
    audio["tracknumber"] = track
    audio.save()
    return audio


def setYear(audio, year):
    audio = EasyID3(audio)
    audio["date"] = year
    audio.save()
    return audio


def setGenre(audio, genre):
    audio = EasyID3(audio)
    audio["genre"] = genre
    audio.save()
    return audio


def setComment(audio, comment):
    audio = mutagen.File(audio)
    audio["COMM::eng"].text[0] = comment
    audio.save()
    return audio


def setFileName(file, newName):
    os.rename(file, newName)
    return


def buildFileNameFromSomeID3Tags(audio, extension):
    # Artist - Title - Album - CommentExtension

    separator = " - "
    fileName = ""

    fileName += getArtist(audio) + separator
    fileName += getTitle(audio) + separator
    fileName += getAlbum(audio) + separator
    fileName += getComment(audio)
    fileName += extension

    return fileName


def setTrackNumberAsTitle(audio):
    setTitle(audio, getTrack(audio))
    return


