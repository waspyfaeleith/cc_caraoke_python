class Room:
    def __init__(self, name):
        self._name = name
        self._guests = []
        self.songs = []

    def get_name(self):
        return self._name
