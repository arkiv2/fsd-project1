from fresh_tomatoes import open_movies_page
from boom_box import getIMDBInfo
from media import Movie

"""main.py: Main module to prepare, initialize and render movie list"""

__author__ = "Archimedes Valencia II"
__version__ = "1.0.3"
__email__ = "arvalencia@gbox.adnu.edu.ph"
__status__ = "Production"


movies = []  # Initialize list to be appended when movies are created

# Instantiate the Movie class using the syntax
# <movie_name> = Movie(<movie_list>, getIMDBInfo("<movie_imdb_id"),
# "<movie_youtube_trailer_url>")
dead_pool = Movie(movies, getIMDBInfo("tt1431045"),
                  "https://www.youtube.com/watch?v=ZIM1HydF9UA")

toy_story = Movie(movies, getIMDBInfo("tt0435761"),
                  "https://www.youtube.com/watch?v=JcpWXaA2qeg")

law_abiding_citizen = Movie(movies, getIMDBInfo("tt1197624"),
                            "https://www.youtube.com/watch?v=BJ3tHqGlCHg")

interstellar = Movie(movies, getIMDBInfo("tt0816692"),
                     "https://www.youtube.com/watch?v=Lm8p5rlrSkY")


# Call the open_movies_page function with the movies list as parameter
# from fresh_tomatoes module to render movies in an html file
open_movies_page(movies)
