import unittest
import mp3Tagger


class MP3TaggerShould(unittest.TestCase):
    def setUp(self):
        audios = mp3Tagger.filterMP3(mp3Tagger.readDirectory("exampleData"))

        mp3Tagger.setTitle("exampleData/" + audios[0], "testFileForGetter")
        mp3Tagger.setArtist("exampleData/" + audios[0], "testFile")
        mp3Tagger.setAlbum("exampleData/" + audios[0], "audioSample")
        mp3Tagger.setTrack("exampleData/" + audios[0], "01")
        mp3Tagger.setYear("exampleData/" + audios[0], "2017")
        mp3Tagger.setGenre("exampleData/" + audios[0], "sample")
        mp3Tagger.setComment("exampleData/" + audios[0], "comment")

        mp3Tagger.setTitle("exampleData/" + audios[1], "testFileForSetter")
        mp3Tagger.setArtist("exampleData/" + audios[1], "testFile")
        mp3Tagger.setAlbum("exampleData/" + audios[1], "audioSample")
        mp3Tagger.setTrack("exampleData/" + audios[1], "02")
        mp3Tagger.setYear("exampleData/" + audios[1], "2017")
        mp3Tagger.setGenre("exampleData/" + audios[1], "sample")
        mp3Tagger.setComment("exampleData/" + audios[1], "comment")

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
        audio = mp3Tagger.filterMP3(mp3Tagger.readDirectory("exampleData"))[1]
        mp3Tagger.setTitle("exampleData/" + audio, "Title")

        actual = mp3Tagger.getTitle("exampleData/" + audio)
        self.assertEqual(expected, actual)

    def test_setArtist(self):
        expected = "Artist"
        audio = mp3Tagger.filterMP3(mp3Tagger.readDirectory("exampleData"))[1]
        mp3Tagger.setArtist("exampleData/" + audio, "Artist")
        actual = mp3Tagger.getArtist("exampleData/" + audio)
        self.assertEqual(expected, actual)

    def test_setAlbum(self):
        expected = "Album"
        audio = mp3Tagger.filterMP3(mp3Tagger.readDirectory("exampleData"))[1]
        mp3Tagger.setAlbum("exampleData/" + audio, "Album")
        actual = mp3Tagger.getAlbum("exampleData/" + audio)
        self.assertEqual(expected, actual)

    def test_setTrack(self):
        expected = "Track"
        audio = mp3Tagger.filterMP3(mp3Tagger.readDirectory("exampleData"))[1]
        mp3Tagger.setTrack("exampleData/" + audio, "Track")
        actual = mp3Tagger.getTrack("exampleData/" + audio)
        self.assertEqual(expected, actual)

    def test_setYear(self):
        expected = "1000"
        audio = mp3Tagger.filterMP3(mp3Tagger.readDirectory("exampleData"))[1]
        mp3Tagger.setYear("exampleData/" + audio, "1000")
        actual = mp3Tagger.getYear("exampleData/" + audio)
        self.assertEqual(expected, str(actual))

    def test_setGenre(self):
        expected = "Genre"
        audio = mp3Tagger.filterMP3(mp3Tagger.readDirectory("exampleData"))[1]
        mp3Tagger.setGenre("exampleData/" + audio, "Genre")
        actual = mp3Tagger.getGenre("exampleData/" + audio)
        self.assertEqual(expected, actual)

    def test_setComment(self):
        expected = "Comment"
        audio = mp3Tagger.filterMP3(mp3Tagger.readDirectory("exampleData"))[1]
        mp3Tagger.setComment("exampleData/" + audio, "Comment")
        actual = mp3Tagger.getComment("exampleData/" + audio)
        self.assertEqual(expected, actual)


def main():
    unittest.main()

if __name__ == '__main__':
    main()