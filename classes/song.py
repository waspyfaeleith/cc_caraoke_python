class Song:
    def __init__(self, title, artist):
        self._title = title
        self._artist = artist

    def get_title(self):
        return self._title

    def get_artist(self):
        return self._artist
