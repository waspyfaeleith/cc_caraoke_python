import sys
sys.path.append("..")

import unittest

from classes.guest import Guest
from classes.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self._song_1 = Song("Highway to Hell", "AC/DC")
        self._song_2 = Song("The Clansman", "Iron Maiden")
        self._song_3 = Song("Ace of Spades", "Motorhead")

        self._songs = [self._song_1, self._song_2, self._song_3]

        song = Song("Ace of Spades", "Motorhead")
        self._guest = Guest("Jack", 20, song)

    def test_guest_has_name(self):
        self.assertEqual("Jack", self._guest.get_name())

    def test_guest_has_cash(self):
        self.assertEqual(20, self._guest.get_cash())

    def test_guest_has_favourite_song(self):
        self.assertEqual("Ace of Spades", self._guest.get_favourite_song().get_title())

    def test_guest_can_change_favourite_song(self):
        song = Song("The Clansman", "Iron Maiden")
        self._guest.set_favourite_song(song)
        self.assertEqual("The Clansman", self._guest.get_favourite_song().get_title())

    def test_guest_can_afford_10(self):
        self.assertEqual(True, self._guest.can_afford(10))

    def test_guest_can_afford_20(self):
        self.assertEqual(True, self._guest.can_afford(20))

    def test_guest_cannot_afford_30(self):
        self.assertEqual(False, self._guest.can_afford(30))

    def test_guest_can_pay_amount(self):
        self._guest.pay(10)
        self.assertEqual(10, self._guest.get_cash())

    def test_guest_cheers_when_fave_song_in_list(self):
        result = self._guest.cheer(self._songs)
        self.assertEqual("Whoo Hoo!", result)

    def test_guest_does_not_cheer_when_fave_song_not_in_list(self):
        song = Song("Back in Black", "AC/DC")
        guest = Guest("Tam", 2, song)
        self.assertEqual(None, guest.cheer(self._songs))

if __name__ == '__main__':
    unittest.main()
