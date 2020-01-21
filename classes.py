import json
from justwatch import JustWatch

just_watch = JustWatch(country='US')


class Movie:
    def __init__(self):
        self.title = ''
        self.availServs = []
        self.year = -1
        self.provIDs = []

    def getIDs(self):
        # queries JustWatch to get JSON object of all results from searching the title plus its release year
        results = just_watch.search_for_item(query=self.title)
        # grabs the first result's available services from the results JSON object
        offers = results['items'][0]['offers']

        # iterate through offers (a list of dictionaries) and grab each provider ID
        idCounter = 0
        for offer in offers:
            # only grab streaming service IDs (not services to purchase/rent)
            if offer['monetization_type'] == 'flatrate':
                if len(self.provIDs) > 0:
                    # if id is not already in the list, add it
                    if self.provIDs[idCounter] != offer['provider_id']:
                        self.provIDs.append(offer['provider_id'])
                        idCounter += 1
                # add the id to the list if it's the first one
                else:
                    self.provIDs.append(offer['provider_id'])


    def getProviders(self):
        # go through provider IDs and match them to their provider
        for id in self.provIDs:
            if id == 8:
                self.availServs.append('Netflix')
            elif id == 15:
                self.availServs.append('Hulu')
            elif id == 31:
                self.availServs.append('HBO GO')
            elif id == 27:
                self.availServs.append('HBO NOW')
            elif id == 9:
                self.availServs.append('Prime Video')
            else:
                self.provIDs.remove(id)


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
        self.title = title
        self.year = releaseYear




