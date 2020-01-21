import json
from justwatch import JustWatch

just_watch = JustWatch(country='US')


class Movie:
    def __init__(self, title, year):
        self.title = title
        self.availServs = []
        self.year = year
        self.provIDs = []

    def getIDs(self):
        # queries JustWatch to get JSON object of all results from searching the title plus its release year
        results = just_watch.search_for_item(query=(self.title + ' ' + self.year))
        # grabs the first result's available services from the results JSON object
        offers = results['items'][0]['offers']

        # iterate through offers (a list of dictionaries) and grab each provider ID
        idCounter = 0
        for offer in offers:
            if len(self.provIDs) > 0:
                if self.provIDs[idCounter] != offer['provider_id']:
                    self.provIDs.append(offer['provider_id'])
                    idCounter += 1
            else:
                self.provIDs.append(offer['provider_id'])


    def getProviders(self):
        for id in self.provIDs:
            if id == 8:
                availServs.append('Netflix')


    def addMovie(self):
        movieInput = input("What movie would like to search to for?\n")
        results = just_watch.search_for_item(query=movieInput)
        title = results['items'][0]['title']
        releaseYear = results['items'][0]['original_release_year']

        print("Are you looking for", title, "which came out in", releaseYear, "?")
        answer = input()
        while (answer == 'no'):
            movieInput = input("Please enter your title more specifically: \n")
            results = just_watch.search_for_item(query=movieInput)
            title = results['items'][0]['title']
            releaseYear = results['items'][0]['original_release_year']

            print("Are you looking for", title, "which came out in", releaseYear, "?")
            answer = input()




