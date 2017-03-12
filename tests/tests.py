import unittest
import mp3Tagger


class MP3TaggerShould(unittest.TestCase):
    def test_readDirectorySucceeds(self):
        expected = ["folder.png",
                    "Ray Parker, Jr. - Ghostbusters - Ghostbusters - Mr. Metal +.mp3",
                    "Slayer - Raining Blood - Soundtrack To The Apocalypse - Best Of - Mr. Metal +.mp3",
                    "Sodom - Agent Orange - Agent Orange - Mr. Metal +.mp3"]
        actual = mp3Tagger.readDirectory("exampleData")
        self.assertEqual(actual, expected)

    def test_readDirectoryFails(self):
        expected = ["Slayer - Raining Blood - Soundtrack To The Apocalypse - Best Of - Mr. Metal +.mp3",
                    "Sodom - Agent Orange - Agent Orange - Mr. Metal +.mp3"]
        actual = mp3Tagger.readDirectory("exampleData")
        self.assertNotEqual(actual, expected)

    def test_filterMP3(self):
        expected = ["Ray Parker, Jr. - Ghostbusters - Ghostbusters - Mr. Metal +.mp3",
                    "Slayer - Raining Blood - Soundtrack To The Apocalypse - Best Of - Mr. Metal +.mp3",
                    "Sodom - Agent Orange - Agent Orange - Mr. Metal +.mp3"]
        actual = mp3Tagger.filterMP3(mp3Tagger.readDirectory("exampleData"))
        self.assertEqual(actual, expected)

    def test_getTitle(self):
        expected = "Raining Blood"
        actual = mp3Tagger.readDirectory("exampleData")
        actual = mp3Tagger.filterMP3(actual)
        actual = mp3Tagger.getTitle("exampleData/" + actual[1])

        self.assertEqual(actual, expected)

    def test_getArtist(self):
        expected = "Slayer"
        actual = mp3Tagger.readDirectory("exampleData")
        actual = mp3Tagger.filterMP3(actual)
        actual = mp3Tagger.getArtist("exampleData/" + actual[1])

        self.assertEqual(actual, expected)

    def test_getAlbum(self):
        expected = "Soundtrack To The Apocalypse - Best Of"
        actual = mp3Tagger.readDirectory("exampleData")
        actual = mp3Tagger.filterMP3(actual)
        actual = mp3Tagger.getAlbum("exampleData/" + actual[1])

        self.assertEqual(actual, expected)

# Was ist mit Verzeichnissen in verzeichnissen oder Dateien die nicht .mp3 sind?
# Am besten womöglich rekursiv reingehen
# Informationen mit Mutagen geben lassen
# Methoden anbieten um dinge zu verändern
# Operationen entwede rmit verschiedenen Skripten oder über config datei anbieten
# https://martin-thoma.com/configuration-files-in-python/

# Tracks = Titel

def main():
    unittest.main()

if __name__ == '__main__':
    main()