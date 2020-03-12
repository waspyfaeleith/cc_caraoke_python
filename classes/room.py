class Room:
    def __init__(self, name, capacity):
        self._name = name
        self._guests = []
        self._songs = []
        self._capacity = capacity

    def get_name(self):
        return self._name

    def get_capacity(self):
        return self._capacity

    def number_of_guests(self):
        return len(self._guests)

    def number_of_songs(self):
        return len(self._songs)

    def check_in_guest(self, guest):
        if self.free_spaces() > 0:
           self._guests.append(guest)

    def check_in_guests(self, guests):
        if self.free_spaces() >= len(guests):
            for guest in guests:
                self._guests.append(guest)

    def check_out_guest(self, guest):
        self._guests.remove(guest)

    def add_song(self, song):
        self._songs.append(song)

    def free_spaces(self):
        return self._capacity - len(self._guests)
