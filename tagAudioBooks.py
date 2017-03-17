import os
import mp3Tagger


path = "data/"
fileExtension = ".mp3"
genre = "audio"
comment = "comment"

for root, dirs, files in os.walk(path):                                                 # root = directory or subdirectory within path
    counter = 0
    for file in files:                                                                  # EVERY file in path and subdirs of path
        counter += 1
        extension = os.path.splitext(file)[1]                                           # get extension of file
        if extension == fileExtension:                                                  # filter for desired files
            audio = os.path.relpath(os.path.join(root, file))                           # relative path to file

            mp3Tagger.setGenre(audio, genre)
            mp3Tagger.setComment(audio, comment)

            maxRequiredDigits = len(str(len(files)))                                    # Calculate required digits, in this loop-iteration 'files' contains all files of one root
            mp3Tagger.formatTracknumbersWithLeadingZeros(audio, maxRequiredDigits)
            mp3Tagger.setTrackNumberAsTitle(audio)

            newFileName = mp3Tagger.buildFileNameFromSomeID3Tags(audio, fileExtension)  # Build filename: Artist - Title - Album - CommentExtension
            newFileName = os.path.relpath(os.path.join(root, newFileName))              # relative path to file with new filename
            mp3Tagger.setFileName(audio, newFileName)

#            mp3Tagger.setTrack(audio, "")                                               # Delete Tracknumber


            print("%4d/" % (counter) + str(len(files)) + "\t" + os.path.basename(audio) + "\t --> \t" + os.path.basename(newFileName))
