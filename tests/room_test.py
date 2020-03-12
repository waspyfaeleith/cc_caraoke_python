import sys
sys.path.append("..")

import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self._jack = Guest("Jack", 20)
        self._victor = Guest("Victor", 15)
        self._isa = Guest("Isa", 100)

        self._guests = [self._jack, self._victor, self._isa]

        self._winston = Guest("Winston", 5)
        self._room = Room("The Metal Room", 3, 10)

    def test_room_has_name(self):
        self.assertEqual("The Metal Room", self._room.get_name())

    def test_room_has_no_guests_at_start(self):
        self.assertEqual(0, self._room.number_of_guests())

    def test_room_has_no_songs_at_start(self):
        self.assertEqual(0, self._room.number_of_songs())

    def test_room_has_capacity(self):
        self.assertEqual(3, self._room.get_capacity())

    def test_room_till_starts_empty(self):
        self.assertEqual(0, self._room.get_till())

    def test_can_add_to_till(self):
        self._room.add_to_till(10)
        self.assertEqual(10, self._room.get_till())

    def test_can_check_in_guest(self):
        self._room.check_in_guest(self._victor)
        self.assertEqual(1, self._room.number_of_guests())

    def test_can_check_in_multiple_guests(self):
        self._room.check_in_guests(self._guests)
        self.assertEqual(3, self._room.number_of_guests())

    def test_can_check_guest_out(self):
        self._room.check_in_guest(self._victor)
        self._room.check_out_guest(self._victor)
        self.assertEqual(0, self._room.number_of_guests())

    def test_can_add_song_to_room(self):
        song = Song("The Number of the Beast", "Iron Maiden")
        self._room.add_song(song)
        self.assertEqual(1, self._room.number_of_songs())

    def test_room_has_free_spaces_equal_to_capacity_at_start(self):
        self.assertEqual(3, self._room.free_spaces())

    def test_free_spaces_goes_down_when_guest_checked_in(self):
        self._room.check_in_guest(self._victor)
        self.assertEqual(2, self._room.free_spaces())

    def test_cannot_check_in_guest_if_room_is_full(self):
        self._room.check_in_guests(self._guests)
        self._room.check_in_guest(self._winston)
        self.assertEqual(3, self._room.number_of_guests())

    def test_cannot_check_in_multiple_guest_if_not_enough_free_space(self):
        self._room.check_in_guest(self._winston)
        self._room.check_in_guests(self._guests)
        self.assertEqual(1, self._room.number_of_guests())

    def test_room_has_fee(self):
        self.assertEqual(10, self._room.get_fee())


if __name__ == '__main__':
    unittest.main()
