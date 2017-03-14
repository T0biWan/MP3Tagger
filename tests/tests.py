import unittest
import mp3Tagger


class MP3TaggerShould(unittest.TestCase):
    def test_readDirectorySucceeds(self):
        expected = ["folder.png",
                    "Ray Parker, Jr. - Ghostbusters - Ghostbusters - Mr. Metal +.mp3",
                    "Slayer - Raining Blood - Soundtrack To The Apocalypse - Best Of - Mr. Metal +.mp3",
                    "Sodom - Agent Orange - Agent Orange - Mr. Metal +.mp3"]
        actual = mp3Tagger.readDirectory("exampleData")
        self.assertEqual(expected, actual)

    def test_readDirectoryFails(self):
        expected = ["Slayer - Raining Blood - Soundtrack To The Apocalypse - Best Of - Mr. Metal +.mp3",
                    "Sodom - Agent Orange - Agent Orange - Mr. Metal +.mp3"]
        actual = mp3Tagger.readDirectory("exampleData")
        self.assertNotEqual(expected, actual)

    def test_filterMP3(self):
        expected = ["Ray Parker, Jr. - Ghostbusters - Ghostbusters - Mr. Metal +.mp3",
                    "Slayer - Raining Blood - Soundtrack To The Apocalypse - Best Of - Mr. Metal +.mp3",
                    "Sodom - Agent Orange - Agent Orange - Mr. Metal +.mp3"]
        actual = mp3Tagger.filterMP3(mp3Tagger.readDirectory("exampleData"))
        self.assertEqual(expected, actual)

    def test_getTitle(self):
        expected = "Raining Blood"
        actual = mp3Tagger.readDirectory("exampleData")
        actual = mp3Tagger.filterMP3(actual)
        actual = mp3Tagger.getTitle("exampleData/" + actual[1])
        self.assertEqual(expected, actual)

    def test_getArtist(self):
        expected = "Slayer"
        actual = mp3Tagger.readDirectory("exampleData")
        actual = mp3Tagger.filterMP3(actual)
        actual = mp3Tagger.getArtist("exampleData/" + actual[1])
        self.assertEqual(expected, actual)

    def test_getAlbum(self):
        expected = "Soundtrack To The Apocalypse - Best Of"
        actual = mp3Tagger.readDirectory("exampleData")
        actual = mp3Tagger.filterMP3(actual)
        actual = mp3Tagger.getAlbum("exampleData/" + actual[1])
        self.assertEqual(expected, actual)

    def test_getTrack(self):
        expected = "01"
        actual = mp3Tagger.readDirectory("exampleData")
        actual = mp3Tagger.filterMP3(actual)
        actual = mp3Tagger.getTrack("exampleData/" + actual[1])
        self.assertEqual(expected, actual)

    def test_getYear(self):
        expected = "2003"
        actual = mp3Tagger.readDirectory("exampleData")
        actual = mp3Tagger.filterMP3(actual)
        actual = mp3Tagger.getYear("exampleData/" + actual[1])
        self.assertEqual(expected, str(actual))

    def test_getGenre(self):
        expected = "Thrash Metal"
        actual = mp3Tagger.readDirectory("exampleData")
        actual = mp3Tagger.filterMP3(actual)
        actual = mp3Tagger.getGenre("exampleData/" + actual[1])
        self.assertEqual(expected, actual)

    def test_setTitle(self):
        expected = "Title"
        song = mp3Tagger.filterMP3(mp3Tagger.readDirectory("exampleData"))[2]
        mp3Tagger.setTitle("exampleData/" + song, "Title")

        actual = mp3Tagger.getTitle("exampleData/" + song)
        self.assertEqual(expected, actual)

    def test_setArtist(self):
        expected = "Artist"
        song = mp3Tagger.filterMP3(mp3Tagger.readDirectory("exampleData"))[2]
        mp3Tagger.setArtist("exampleData/" + song, "Artist")
        actual = mp3Tagger.getArtist("exampleData/" + song)
        self.assertEqual(expected, actual)

    def test_setAlbum(self):
        expected = "Album"
        song = mp3Tagger.filterMP3(mp3Tagger.readDirectory("exampleData"))[2]
        mp3Tagger.setAlbum("exampleData/" + song, "Album")
        actual = mp3Tagger.getAlbum("exampleData/" + song)
        self.assertEqual(expected, actual)

    def test_setTrack(self):
        expected = "Track"
        song = mp3Tagger.filterMP3(mp3Tagger.readDirectory("exampleData"))[2]
        mp3Tagger.setTrack("exampleData/" + song, "Track")
        actual = mp3Tagger.getTrack("exampleData/" + song)
        self.assertEqual(expected, actual)

    def test_setYear(self):
        expected = "1000"
        song = mp3Tagger.filterMP3(mp3Tagger.readDirectory("exampleData"))[2]
        mp3Tagger.setYear("exampleData/" + song, "1000")
        actual = mp3Tagger.getYear("exampleData/" + song)
        self.assertEqual(expected, str(actual))

    def test_setGenre(self):
        expected = "Genre"
        song = mp3Tagger.filterMP3(mp3Tagger.readDirectory("exampleData"))[2]
        mp3Tagger.setGenre("exampleData/" + song, "Genre")
        actual = mp3Tagger.getGenre("exampleData/" + song)
        self.assertEqual(expected, actual)


# Was ist mit Verzeichnissen in verzeichnissen oder Dateien die nicht .mp3 sind?
# Am besten womöglich rekursiv reingehen
# Funktion um Dateinamen zu ändern
# Operationen entwede rmit verschiedenen Skripten oder über config datei anbieten
# https://martin-thoma.com/configuration-files-in-python/
# Skript um Titel = Track zu machen
# Exception schrieben falls ein feld leer ist!
# Beispieldateien umbenennen...erster song: testFileForGetter, zweiter song: testFileForSetter usw.
# alles auf EasyMP3 umbauen
# Am Ende der Tests müssen die Datein in ihren Ausgangszustand zurück getaggt und benannt werden!

def main():
    unittest.main()

if __name__ == '__main__':
    main()