class Guest:
    def __init__(self, name, cash, song):
        self._name = name
        self._cash = cash
        self._favourite_song = song

    def get_name(self):
        return self._name

    def get_cash(self):
        return self._cash

    def get_favourite_song(self):
        return self._favourite_song

    def set_favourite_song(self, song):
        self._favourite_song = song

    def can_afford(self, amount):
        return self._cash >= amount

    def pay(self, amount):
        self._cash -= amount

    def cheer(self, songs):
        for song in songs:
            if song.equals(self._favourite_song):
                return "Whoo Hoo!"
        return None
