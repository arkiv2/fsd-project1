import urllib
import json

class Movie():
    def __init__(self, movie_info):
        self.title = movie_info['Title']
        self.plot = movie_info['Plot']
        

def getIMDBInfo(imdb_code):
    connection = urllib.urlopen("http://www.omdbapi.com/?i="
                         +imdb_code+
                         "&plot=full&r=json")
    movie = json.loads(connection.read())
    #print(imdb_data)
    connection.close()
    return movie

movie1 = Movie(getIMDBInfo("tt2133196"))
print(movie1.title)

