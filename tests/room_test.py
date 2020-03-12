import sys
sys.path.append("..")

import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):

    def test_room_has_name(self):
        room = Room("The Metal Room")
        self.assertEqual("The Metal Room", room.get_name())

    def test_room_has_no_guests_at_start(self):
        room = Room("The Blues Room")
        self.assertEqual(0, room.number_of_guests())

    def test_room_has_no_songs_at_start(self):
        room = Room("The Blues Room")
        self.assertEqual(0, room.number_of_songs())

    def test_can_check_in_guest(self):
        room = Room("The Blues Room")
        guest = Guest("Victor")
        room.check_in_guest(guest)
        self.assertEqual(1, room.number_of_guests())

    def test_can_check_in_multiple_guests(self):
        room = Room("The Blues Room")
        jack = Guest("Jack")
        victor = Guest("Victor")
        isa = Guest("Isa")

        guests = [jack, victor, isa]
        room.check_in_guests(guests)
        self.assertEqual(3, room.number_of_guests())

    def test_can_check_guest_out(self):
        room = Room("The Blues Room")
        guest = Guest("Victor")
        room.check_in_guest(guest)
        room.check_out_guest(guest)
        self.assertEqual(0, room.number_of_guests())

    def test_can_add_song_to_room(self):
        room = Room("The Metal Room")
        song = Song("The Number of the Beast", "Iron Maiden")
        room.add_song(song)
        self.assertEqual(1, room.number_of_songs())


if __name__ == '__main__':
    unittest.main()
