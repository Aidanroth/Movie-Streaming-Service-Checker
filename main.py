import json
from justwatch import JustWatch

just_watch = JustWatch(country='US')


def main():

    #results = just_watch.search_for_item(query='the matrix')
    results = just_watch.search_for_item(
        query='the matrix',
        monetization_types=['free', 'flatrate']
    )

    print(json.dumps(results, indent=4, sort_keys=False))


main()