import json
from justwatch import JustWatch
#from classes import Movie

just_watch = JustWatch(country='US')

# Netflix provider id: 8

def search():

    # results is a dict
    results = just_watch.search_for_item(query='the irishman')
    # selection is a dict
    selection = results['items'][0]
    # offers is a list of dicts
    offers = results['items'][0]['offers']
    firstOffer = offers[0]

    idList = []

    i = 0
    idCounter = 0
    for i in range(len(offers)):
        if len(idList) > 0:
            if idList[idCounter] != offers[i]['provider_id']:
                idList.append(offers[i]['provider_id'])
                idCounter += 1

        else:
            idList.append(offers[i]['provider_id'])

    for j in idList:
        print(j)


    #print(json.dumps(selection, indent=4, sort_keys=False))


search()