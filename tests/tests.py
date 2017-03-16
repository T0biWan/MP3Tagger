import unittest
import mp3Tagger


class MP3TaggerShould(unittest.TestCase):
    def setUp(self):
        songs = mp3Tagger.filterMP3(mp3Tagger.readDirectory("exampleData"))

        mp3Tagger.setTitle("exampleData/" + songs[0], "testFileForGetter")
        mp3Tagger.setArtist("exampleData/" + songs[0], "testFile")
        mp3Tagger.setAlbum("exampleData/" + songs[0], "audioSample")
        mp3Tagger.setTrack("exampleData/" + songs[0], "01")
        mp3Tagger.setYear("exampleData/" + songs[0], "2017")
        mp3Tagger.setGenre("exampleData/" + songs[0], "sample")
        mp3Tagger.setComment("exampleData/" + songs[0], "comment")

        mp3Tagger.setTitle("exampleData/" + songs[1], "audioSample")
        mp3Tagger.setArtist("exampleData/" + songs[1], "testFile")
        mp3Tagger.setAlbum("exampleData/" + songs[1], "audioSample")
        mp3Tagger.setTrack("exampleData/" + songs[1], "02")
        mp3Tagger.setYear("exampleData/" + songs[1], "2017")
        mp3Tagger.setGenre("exampleData/" + songs[1], "sample")
        mp3Tagger.setComment("exampleData/" + songs[1], "comment")

    def test_readDirectorySucceeds(self):
        expected = ["folder.png",
                    "testFile - testFileForGetter - audioSample - comment.mp3",
                    "testFile - testFileForSetter - audioSample - comment.mp3"]
        actual = mp3Tagger.readDirectory("exampleData")
        self.assertEqual(expected, actual)

    def test_readDirectoryFails(self):
        expected = []
        actual = mp3Tagger.readDirectory("exampleData")
        self.assertNotEqual(expected, actual)

    def test_filterMP3(self):
        expected = ["testFile - testFileForGetter - audioSample - comment.mp3",
                    "testFile - testFileForSetter - audioSample - comment.mp3"]
        actual = mp3Tagger.filterMP3(mp3Tagger.readDirectory("exampleData"))
        self.assertEqual(expected, actual)

    def test_getTitle(self):
        expected = "testFileForGetter"
        actual = mp3Tagger.readDirectory("exampleData")
        actual = mp3Tagger.filterMP3(actual)
        actual = mp3Tagger.getTitle("exampleData/" + actual[0])
        self.assertEqual(expected, actual)

    def test_getArtist(self):
        expected = "testFile"
        actual = mp3Tagger.readDirectory("exampleData")
        actual = mp3Tagger.filterMP3(actual)
        actual = mp3Tagger.getArtist("exampleData/" + actual[0])
        self.assertEqual(expected, actual)

    def test_getAlbum(self):
        expected = "audioSample"
        actual = mp3Tagger.readDirectory("exampleData")
        actual = mp3Tagger.filterMP3(actual)
        actual = mp3Tagger.getAlbum("exampleData/" + actual[0])
        self.assertEqual(expected, actual)

    def test_getTrack(self):
        expected = "01"
        actual = mp3Tagger.readDirectory("exampleData")
        actual = mp3Tagger.filterMP3(actual)
        actual = mp3Tagger.getTrack("exampleData/" + actual[0])
        self.assertEqual(expected, actual)

    def test_getYear(self):
        expected = "2017"
        actual = mp3Tagger.readDirectory("exampleData")
        actual = mp3Tagger.filterMP3(actual)
        actual = mp3Tagger.getYear("exampleData/" + actual[0])
        self.assertEqual(expected, str(actual))

    def test_getGenre(self):
        expected = "sample"
        actual = mp3Tagger.readDirectory("exampleData")
        actual = mp3Tagger.filterMP3(actual)
        actual = mp3Tagger.getGenre("exampleData/" + actual[0])
        self.assertEqual(expected, actual)

    def test_getComment(self):
        expected = "comment"
        actual = mp3Tagger.readDirectory("exampleData")
        actual = mp3Tagger.filterMP3(actual)
        actual = mp3Tagger.getComment("exampleData/" + actual[0])
        self.assertEqual(expected, actual)

    def test_setTitle(self):
        expected = "Title"
        song = mp3Tagger.filterMP3(mp3Tagger.readDirectory("exampleData"))[1]
        mp3Tagger.setTitle("exampleData/" + song, "Title")

        actual = mp3Tagger.getTitle("exampleData/" + song)
        self.assertEqual(expected, actual)

    def test_setArtist(self):
        expected = "Artist"
        song = mp3Tagger.filterMP3(mp3Tagger.readDirectory("exampleData"))[1]
        mp3Tagger.setArtist("exampleData/" + song, "Artist")
        actual = mp3Tagger.getArtist("exampleData/" + song)
        self.assertEqual(expected, actual)

    def test_setAlbum(self):
        expected = "Album"
        song = mp3Tagger.filterMP3(mp3Tagger.readDirectory("exampleData"))[1]
        mp3Tagger.setAlbum("exampleData/" + song, "Album")
        actual = mp3Tagger.getAlbum("exampleData/" + song)
        self.assertEqual(expected, actual)

    def test_setTrack(self):
        expected = "Track"
        song = mp3Tagger.filterMP3(mp3Tagger.readDirectory("exampleData"))[1]
        mp3Tagger.setTrack("exampleData/" + song, "Track")
        actual = mp3Tagger.getTrack("exampleData/" + song)
        self.assertEqual(expected, actual)

    def test_setYear(self):
        expected = "1000"
        song = mp3Tagger.filterMP3(mp3Tagger.readDirectory("exampleData"))[1]
        mp3Tagger.setYear("exampleData/" + song, "1000")
        actual = mp3Tagger.getYear("exampleData/" + song)
        self.assertEqual(expected, str(actual))

    def test_setGenre(self):
        expected = "Genre"
        song = mp3Tagger.filterMP3(mp3Tagger.readDirectory("exampleData"))[1]
        mp3Tagger.setGenre("exampleData/" + song, "Genre")
        actual = mp3Tagger.getGenre("exampleData/" + song)
        self.assertEqual(expected, actual)

    def test_setComment(self):
        expected = "Comment"
        song = mp3Tagger.filterMP3(mp3Tagger.readDirectory("exampleData"))[1]
        mp3Tagger.setComment("exampleData/" + song, "Comment")
        actual = mp3Tagger.getComment("exampleData/" + song)
        self.assertEqual(expected, actual)


def main():
    unittest.main()

if __name__ == '__main__':
    main()