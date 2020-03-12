import sys
sys.path.append("..")

import unittest

from classes.song import Song

class TestGuest(unittest.TestCase):

    def test_song_has_title(self):
        song = Song("Highway To Hell", "AC/DC")
        self.assertEqual("Highway To Hell", song.get_title())

    def test_song_has_artist(self):
        song = Song("Highway To Hell", "AC/DC")
        self.assertEqual("AC/DC", song.get_artist())

if __name__ == '__main__':
    unittest.main()
