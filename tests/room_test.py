import sys
sys.path.append("..")

import unittest

from classes.room import Room

class TestRoom(unittest.TestCase):

    def test_room_has_name(self):
        room = Room("The Metal Room")
        self.assertEqual("The Metal Room", room.get_name())

if __name__ == '__main__':
    unittest.main()
