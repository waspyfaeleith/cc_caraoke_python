class Room:
    def __init__(self, name, capacity, fee):
        self._name = name
        self._guests = []
        self._songs = []
        self._capacity = capacity
        self._till = 0
        self._fee = fee

    def get_name(self):
        return self._name

    def get_capacity(self):
        return self._capacity

    def get_till(self):
        return self._till

    def get_fee(self):
        return self._fee

    def number_of_guests(self):
        return len(self._guests)

    def number_of_songs(self):
        return len(self._songs)

    def check_in_guest(self, guest):
        if self.free_spaces() > 0 and guest.can_afford(self._fee):
           guest.pay(self._fee)
           self.add_to_till(self._fee)
           self._guests.append(guest)

    def check_in_guests(self, guests):
        if self.free_spaces() >= len(guests):
            for guest in guests:
                self.check_in_guest(guest)

    def check_out_guest(self, guest):
        self._guests.remove(guest)

    def add_song(self, song):
        self._songs.append(song)

    def add_songs(self, songs):
        for song in songs:
            self._songs.append(song)

    def free_spaces(self):
        return self._capacity - len(self._guests)

    def add_to_till(self, amount):
        self._till += amount
