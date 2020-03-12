class Guest:
    def __init__(self, name, cash):
        self._name = name
        self._cash = cash

    def get_name(self):
        return self._name

    def get_cash(self):
        return self._cash

    def can_afford(self, amount):
        return self._cash >= amount
