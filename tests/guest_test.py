import sys
sys.path.append("..")

import unittest

from classes.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self._guest = Guest("Jack", 20)

    def test_guest_has_name(self):
        self.assertEqual("Jack", self._guest.get_name())

    def test_guest_has_cash(self):
        self.assertEqual(20, self._guest.get_cash())

if __name__ == '__main__':
    unittest.main()
