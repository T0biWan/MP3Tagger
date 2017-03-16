import mp3Tagger


path = "data/"
fileExtension = ".mp3"
comment = "comment"

directory = mp3Tagger.readDirectory(path)
directory = mp3Tagger.filterMP3(directory)

for audio in directory:
    mp3Tagger.setComment(path + audio, comment)
    mp3Tagger.formatTracknumbersWithLeadingZeros(path + audio, len(str(len(directory))))
    mp3Tagger.setTrackNumberAsTitle(path + audio)
    newFileName = mp3Tagger.buildFileNameFromSomeID3Tags(path + audio) + fileExtension
    #mp3Tagger.setTrack(path + audio, "")
    mp3Tagger.setFileName(path + audio, path + newFileName)
    print(audio + "\t --> \t" + newFileName)


