import sys
sys.path.append("..")

import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self._room = Room("The Metal Room")

    def test_room_has_name(self):
        self.assertEqual("The Metal Room", self._room.get_name())

    def test_room_has_no_guests_at_start(self):
        self.assertEqual(0, self._room.number_of_guests())

    def test_room_has_no_songs_at_start(self):
        self.assertEqual(0, self._room.number_of_songs())

    def test_can_check_in_guest(self):
        guest = Guest("Victor")
        self._room.check_in_guest(guest)
        self.assertEqual(1, self._room.number_of_guests())

    def test_can_check_in_multiple_guests(self):
        jack = Guest("Jack")
        victor = Guest("Victor")
        isa = Guest("Isa")

        guests = [jack, victor, isa]
        self._room.check_in_guests(guests)
        self.assertEqual(3, self._room.number_of_guests())

    def test_can_check_guest_out(self):
        guest = Guest("Victor")
        self._room.check_in_guest(guest)
        self._room.check_out_guest(guest)
        self.assertEqual(0, self._room.number_of_guests())

    def test_can_add_song_to_room(self):
        song = Song("The Number of the Beast", "Iron Maiden")
        self._room.add_song(song)
        self.assertEqual(1, self._room.number_of_songs())


if __name__ == '__main__':
    unittest.main()
