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

    def test_guest_can_afford_10(self):
        self.assertEqual(True, self._guest.can_afford(10))

    def test_guest_can_afford_20(self):
        self.assertEqual(True, self._guest.can_afford(20))

    def test_guest_cannot_afford_30(self):
        self.assertEqual(False, self._guest.can_afford(30))

    def test_guest_can_pay_amount(self):
        self._guest.pay(10)
        self.assertEqual(10, self._guest.get_cash())

if __name__ == '__main__':
    unittest.main()
