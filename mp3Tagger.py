import os


def readDirectory(path):
    return os.listdir(path)

def filterMP3(list):
    mp3List = []
    for element in list:
        if ".mp3" in element:
            mp3List.append(element)
    return mp3List
