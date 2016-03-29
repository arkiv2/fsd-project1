"""media.py: module to define classes"""

__author__ = "Archimedes Valencia II"

__version__ = "1.0.3"
__email__ = "arvalencia@gbox.adnu.edu.ph"
__status__ = "Production"


class Movie():
    def __init__(this, movies, movie_info, trailer_url):
        """
            Creates an instance of a movie and appends them to
            a list(movies)
        """
        this.imdbID = movie_info['imdbID']
        this.title = movie_info['Title']
        this.plot = movie_info['Plot']
        this.year = movie_info['Year']
        this.genre = movie_info['Genre']
        this.poster_image_url = movie_info['Poster']
        this.trailer_youtube_url = trailer_url
        this.released = movie_info['Released']
        this.writer = movie_info['Writer']
        this.actors = movie_info['Actors']
        this.rating = movie_info['imdbRating']
        movies.append(this)
