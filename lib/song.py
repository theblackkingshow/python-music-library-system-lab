class Song:
    """A Song represents a music track and tracks global song metadata."""

    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        """Increment the total number of Song instances created."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Add a genre to the list of unique genres.

        Prevent duplicate genre entries while preserving insertion order.
        """
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Add an artist to the list of unique artists.

        Prevent duplicate artist entries while preserving insertion order.
        """
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Count how many songs exist for each genre."""
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artist_count(cls, artist):
        """Count how many songs exist for each artist."""
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1

    # Alias for naming consistency with assignment instructions
    add_to_artists_count = add_to_artist_count
