import sys
sys.path.append("..")

import unittest

from classes.room import Room

class TestRoom(unittest.TestCase):

    def test_room_has_name(self):
        room = Room("The Metal Room")
        self.assertEqual("The Metal Room", room.get_name())

    def test_room_has_no_guests_at_start(self):
        room = Room("The Blues Room")
        self.assertEqual(0, room.number_of_guests())

if __name__ == '__main__':
    unittest.main()
