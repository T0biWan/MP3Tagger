import unittest
import mp3Tagger


class MP3TaggerShould(unittest.TestCase):
    def testReadDataSucced(self):
        expected = ["Ray Parker, Jr. - Ghostbusters - Ghostbusters - Mr. Metal +.mp3",
                    "Slayer - Raining Blood - Soundtrack To The Apocalypse - Best Of - Mr. Metal +.mp3",
                    "Sodom - Agent Orange - Agent Orange - Mr. Metal +.mp3"]
        actual = mp3Tagger.readData("exampleData")
        self.assertEqual(actual, expected)

    def testReadDataFails(self):
        expected = ["Slayer - Raining Blood - Soundtrack To The Apocalypse - Best Of - Mr. Metal +.mp3",
                    "Sodom - Agent Orange - Agent Orange - Mr. Metal +.mp3"]
        actual = mp3Tagger.readData("exampleData")
        self.assertNotEqual(actual, expected)

# Was ist mit Verzeichnissen in verzecihnissen oder Dateien die nicht .mp3 sind?

def main():
    unittest.main()

if __name__ == '__main__':
    main()