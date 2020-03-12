import sys
sys.path.append("..")

import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self._room = Room("The Metal Room", 3)

    def test_room_has_name(self):
        self.assertEqual("The Metal Room", self._room.get_name())

    def test_room_has_no_guests_at_start(self):
        self.assertEqual(0, self._room.number_of_guests())

    def test_room_has_no_songs_at_start(self):
        self.assertEqual(0, self._room.number_of_songs())

    def test_room_has_capacity(self):
        self.assertEqual(3, self._room.get_capacity())

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

    def test_room_has_free_spaces_equal_to_capacity_at_start(self):
        self.assertEqual(3, self._room.free_spaces())

    def test_free_spaces_goes_down_when_guest_checked_in(self):
        guest = Guest("Victor")
        self._room.check_in_guest(guest)
        self.assertEqual(2, self._room.free_spaces())

    def test_cannot_check_in_guest_if_room_is_full(self):
        jack = Guest("Jack")
        victor = Guest("Victor")
        isa = Guest("Isa")
        winston = Guest("Winston")

        guests = [jack, victor, isa]
        self._room.check_in_guests(guests)
        self._room.check_in_guest(winston)
        self.assertEqual(3, self._room.number_of_guests())

    def test_cannot_check_in_multiple_guest_if_not_enough_free_space(self):
        winston = Guest("Winston")
        self._room.check_in_guest(winston)
        jack = Guest("Jack")
        victor = Guest("Victor")
        isa = Guest("Isa")
        winston = Guest("Winston")

        guests = [jack, victor, isa]
        self._room.check_in_guests(guests)
        self.assertEqual(1, self._room.number_of_guests())


if __name__ == '__main__':
    unittest.main()
