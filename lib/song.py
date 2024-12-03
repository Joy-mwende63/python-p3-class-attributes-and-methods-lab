class Song:
    count = 0  # Class attribute to track the number of songs
    genres = []  # Class attribute to track the genres of all songs
    artists = []  # Class attribute to track the artists of all songs
    genre_count = {}  # Class attribute to track the count of each genre
    artist_count = {}  # Class attribute to track the count of songs per artist

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Increment the song count
        Song.add_song_to_count()
        
        # Add the genre to the genres list
        Song.add_to_genres(genre)
        
        # Add the artist to the artists list
        Song.add_to_artists(artist)
        
        # Update the genre count
        Song.add_to_genre_count(genre)
        
        # Update the artist count
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        """Increment the song count by one whenever a new song is created."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Add a genre to the genres list if it is not already there."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Add an artist to the artists list if it is not already there."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Add to the genre count dictionary, incrementing the count for the given genre."""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        """Add to the artist count dictionary, incrementing the count for the given artist."""
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

