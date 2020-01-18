#! /usr/bin/env python3
'''API requests module in json format, using https://restcountries.eu/

.. _Git-hub Repository:
   https://github.com/Mint-Afk/EUROPEAN-GEOGRAPHY-CHAMPION-2K20--PRO-.git

'''

import requests
import json

country_url = 'https://restcountries.eu/rest/v2/name/{}'     # by name
capital_url = 'https://restcountries.eu/rest/v2/capital/{}'  # by cap


def get_info(apiurl, country):
    '''Return info's about state/capital country from API.

    Given the place selected, the function makes request to the
    restcountries service trying to get all the info's about the country.

    Parameters:
        apiurl (str): url of the API, by country name or capital
        country (str): user shell inputs argument

    Returns:
        data (str): returning json with all the info's from api
    '''
    print(type(apiurl))
    print("Trying to fetch all the data's we can get about {} from the API...")
    r = requests.get(apiurl.format(country))
    if r.status_code == 200:
        query = json.loads(r.text)
    else:
        print("Sorry, something went wrong!")
        raise requests.exceptions.RequestException
    data = json.dumps(query, indent=2, sort_keys=True)
    print(type(data))
    return data
