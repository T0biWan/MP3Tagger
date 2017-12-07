# MP3Tagger
A simple application to change ID3-tags using [Mutagen](https://github.com/quodlibet/mutagen).  
Also an exercise for me to practice test-driven development and Python.

## Tests
Unit tests enabled through Python's unittest-module.

## Functionality
- Convenient wrapper for Mutagen
- Reads files from directory
- Filters for mp3-data
- Gets and sets title, artist, album, track, year, genre and comment
- Renames files according to their ID3-tags
- Formats Tracknumbers with leading zeros

## TagAudioBooks
Use case of my own where I want the titles of audiobooks to be equal to the tracknumbers.
To solve this I use functions of MP3Tagger and Python's os-module.
