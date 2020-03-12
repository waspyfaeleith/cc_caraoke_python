class Room:
    def __init__(self, name):
        self._name = name
        self._guests = []
        self._songs = []

    def get_name(self):
        return self._name

    def number_of_guests(self):
        return len(self._guests)

    def number_of_songs(self):
        return len(self._songs)
