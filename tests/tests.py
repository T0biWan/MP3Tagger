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


# Was ist mit Verzeichnissen in verzeichnissen oder Dateien die nicht .mp3 sind?
# Am besten womöglich rekursiv reingehen
# Filtern auf mp3-Dateien
# Informationen mit Mutagen geben lassen
# Methoden anbieten um dinge zu verändern
# Tracks = Titel

def main():
    unittest.main()

if __name__ == '__main__':
    main()