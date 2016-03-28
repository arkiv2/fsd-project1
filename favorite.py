class Movie():
    def __init__(self, movie_info):
        self.title = movie_info['Title']
        self.plot = movie_info['Plot']
        self.year = movie_info['Year']
        self.genre = movie_info['Genre']
        self.poster_image_url = movie_info['Poster']
        self.trailer_youtube_url = movie_info['Poster']
        self.released = movie_info['Released']
        self.writer = movie_info['Writer']
        self.actors = movie_info['Actors']
        self.rating = movie_info['imdbRating']
