import sys
sys.path.append("..")

import unittest

from classes.guest import Guest

class TestGuest(unittest.TestCase):

    def test_guest_has_name(self):
        guest = Guest("Jack")
        self.assertEqual("Jack", guest.get_name())

if __name__ == '__main__':
    unittest.main()
