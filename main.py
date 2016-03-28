from fresh_tomatoes import open_movies_page
from boom_box import getIMDBInfo
from media import Movie

movies = []

bat_vs_super = Movie(movies, getIMDBInfo("tt2975590"),
                           "https://www.youtube.com/watch?v=eX_iASz1Si8")

dead_pool = Movie(movies, getIMDBInfo("tt1431045"),
                          "https://www.youtube.com/watch?v=ZIM1HydF9UA")

toy_story = Movie(movies, getIMDBInfo("tt0435761"),
                           "https://www.youtube.com/watch?v=JcpWXaA2qeg")

open_movies_page(movies)
