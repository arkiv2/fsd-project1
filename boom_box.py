import favorite
import urllib
import json

def getIMDBInfo(imdb_code): #Movie's IMDB Code
    connection = urllib.urlopen("http://www.omdbapi.com/?i="
                         +imdb_code+
                         "&plot=full&r=json") #Query OMDBAPI for IMDB info
    movie = json.loads(connection.read()) #Convert JSON data to objects 
    connection.close()
    return movie    #Returns Serialized JSON

toy_story_3 = favorite.Movie(getIMDBInfo("tt0435761")) #tt0435761 is toy story 3's IMDB Code

print(toy_story_3.plot)
