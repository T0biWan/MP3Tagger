import os
from mutagen.easyid3 import EasyID3


def readDirectory(path):
    return os.listdir(path)


def filterMP3(list):
    mp3List = []
    for element in list:
        if ".mp3" in element:
            mp3List.append(element)
    return mp3List


def getTitle(song):
    song = EasyID3(song)
    return song["title"][0]

def getArtist(song):
    song = EasyID3(song)
    return song["artist"][0]

def getAlbum(song):
    song = EasyID3(song)
    return song["album"][0]

def getTrack(song):
    song = EasyID3(song)
    return song["tracknumber"][0]

def getYear(song):
    song = EasyID3(song)
    return song["date"][0]

def getGenre(song):
    song = EasyID3(song)
    return song["genre"][0]

def setTitle(song, title):
    song = EasyID3(song)
    song["title"] = title
    song.save()
    return song

def setArtist(song, artist):
    song = EasyID3(song)
    song["artist"] = artist
    song.save()
    return song

def setAlbum(song, album):
    song = EasyID3(song)
    song["album"] = album
    song.save()
    return song

def setTrack(song, track):
    song = EasyID3(song)
    song["tracknumber"] = track
    song.save()
    return song

def setYear(song, year):
    song = EasyID3(song)
    song["date"] = year
    song.save()
    return song

def setGenre(song, genre):
    song = EasyID3(song)
    song["genre"] = genre
    song.save()
    return song

