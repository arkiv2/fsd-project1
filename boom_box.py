"""boom_box.py: module to define a function that communicated with
    an external API to query movie info from IMDB"""

__author__ = "Archimedes Valencia II"

__version__ = "1.0.3"
__email__ = "arvalencia@gbox.adnu.edu.ph"
__status__ = "Production"

from fresh_tomatoes import open_movies_page
from media import Movie
import urllib
import json

def getIMDBInfo(imdb_code):
    """ Get info from IMDB website using omdbapi.com's API
        Usage : getIMDBInfo(imdb_code)
        e.g. : print(boom_box.getIMDBInfo(tt0435771)
    """
    connection = urllib.urlopen("http://www.omdbapi.com/?i="
                         +imdb_code+
                         "&plot=full&r=json") #Query OMDBAPI for IMDB info
    movie = json.loads(connection.read()) #Convert JSON data to objects 
    connection.close()
    return movie    #Returns Serialized JSON
