import json
from justwatch import JustWatch
from classes import Movie



def runManager():

    newMovie = Movie()
    newMovie.addMovie()
    newMovie.getIDs()
    newMovie.getProviders()
    print(newMovie.availServs)


runManager()