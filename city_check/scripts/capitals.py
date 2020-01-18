#! /usr/bin/env python3
'''Capital module is core to the whole functioning of the program.

This module contains two main functions:

    - load_csv: utilised to open and analyse csv file datas.
    - check_capitals: returns the correspondence asked.

Check function called by the main_app taking argument place of the parser,
is gonna check the list previously loaded by the load_csv function to answer.

Example:
    Given user shell input:

        $ python parser.py place -v

    args.place is passed to the check_capital function and csv.
    If place = ITALY is gonna answer back:

        The capital of ITALY is ROME

    Verbosity level is regulated through the optional argument of the parser,
    The level goes from 0 (answer only) to 3 (API - country info's)

.. _Git-hub Repository:
   https://github.com/Mint-Afk/EUROPEAN-GEOGRAPHY-CHAMPION-2K20--PRO-.git

'''

import csv
from city_check.scripts import apinfo as api

country_url = 'https://restcountries.eu/rest/v2/name/{}'
capital_url = 'https://restcountries.eu/rest/v2/capital/{}'


def load_csv(filename):
    '''Read the csv file and return the state/capital dictionary.'''
    list_of_capitals = {}
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            list_of_capitals[row[0]] = row[1]
    return list_of_capitals


def check_capital(list, args):
    '''Return the right state/capital given the user shell input capital/state.

    - 1st Part: check if the input is a valid state in the capitals list,
                and gives in return the capital associated.
    - 2nd Part: check exactly the reverse of the first one.

    The function is gonna calibrate the verbosity if specified by (-v) level.

    Parameters:
        list (dict): list containing the state/capital dictionary
        args (argparse.Namespace): user shell inputs arguments
        *place: user state/capital input
        *verbosity: user desired output verbosity

    Returns:
        answer (string): returning strings with variable verbosity

    Raises:
        -bash: [Non-European State/Capital]:
        command not found : error raised if the user input is wrong/incorrect.
    '''
    if args.place in list:
        real_url = country_url
        if args.verbosity == 2:
            print('''
                  args.place is passed to the check function.
                  The dictionary, previously loaded by load_csv,
                  is checked as next step to find a correspondence.

                  All that effort to say that:
                            the capital of {} is obviously... {}
                  '''.format(args.place,
                             list[args.place]))
        elif args.verbosity == 1:
            print("The capital of {} is {}".format(args.place,
                                                   list[args.place]))
        elif args.verbosity >= 3:
            info = api.get_info(real_url, args.place)
            print(info)
        else:
            print(list[args.place])
    else:
        real_url = capital_url
        for state, capital in list.items():
            if capital == args.place:
                if args.verbosity == 2:
                    print('''
                          args.place is passed to the check function.
                          The dictionary, previously loaded by load_csv,
                          is checked as next step to find a correspondence.

                          All that effort to say that:
                          the state whose capital is {} is {}"
                          '''.format(args.place, state))
                elif args.verbosity == 1:
                    print("The state whose capital is {} is {}"
                          .format(args.place, state))
                elif args.verbosity >= 3:
                    info = api.get_info(real_url, args.place)
                    print(info)
                else:
                    print(state)
    if args.place not in list and args.place not in list.values():
        print('''
              Sorry, but {} does not seem to be a valid state or capital.
              '''. format(args.place))
