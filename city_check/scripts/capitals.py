#! /usr/bin/env python3
'''Capital module is core to the whole functioning of the program.

This module contains two main functions:
    - load_csv: utilised to open and analyse csv file datas. 
    - check_capitals: returns the correspondence asked. 
Check function called by the main_app taking argument name of the parser, 
is gonna check the list previously loaded by the load_csv function to answer. 

Example:
    Given user shell input:

        $ python parser.py name -v

    args.name is passed to the check_capital function checking if present in the csv list
    previously loaded by load_csv function. If name = ITALY is gonna answer back:

        The capital of ITALY is ROME

    Level of verbosity is regulated through the optional argument of the parser.

.. _Git-hub Repository:
   https://github.com/Mint-Afk/capitals.git

'''

import csv


def load_csv(filename):
    '''Read the capitalcsv file and return the state/capital dictionary.'''
    list_of_capitals = {}
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            list_of_capitals[row[0]] = row[1]
    return list_of_capitals


def check_capital(list, args):
    '''Return the correspondent state/capital given the user shell input capital/state.

    - 1st Part: check if the input is a valid state in the capitals list, 
                and gives in return the capital associated. 
    - 2nd Part: check exactly the reverse of the first one. 
    The function is gonna calibrate the verbosity of the answers if specified by (-v) argument.

    Parameters:
        list (dict): list containing the state/capital dictionary
        args (argparse.Namespace): user shell inputs arguments
        *name: user state/capital input
        *verbosity: user desired output verbosity

    Returns:
        string: returning strings with variable verbosity

    Raises:
        -bash: [Non-European State/Capital]: 
        command not found : error raised if the user input is wrong/incorrect or an out of Europe place.
    '''
    if args.name in list:
        if args.verbosity >= 2:
            print('''
                  args.name is passed to the check function.
                  The dictionary in list, previously loaded by load_csv,
                  is checked as next step to find a correspondence.                   
                  
                  All that effort to say that the capital of {} is obviously... {}
                  '''.format(args.name, 
                             list[args.name]))
        elif args.verbosity >= 1:
            print("The capital of {} is {}".format(args.name, 
                                                   list[args.name]))
        else:
            print(list[args.name])
    else:
        for state, capital in list.items():
            if capital == args.name:
                if args.verbosity >= 2:
                    print('''
                          args.name is passed to the check function.
                          The dictionary in list, previously loaded by load_csv,
                          is checked as next step to find a correspondence. 

                          All that effort to say that the capital of {} is obviously... {}
                          '''.format(args.name, 
                                     state))
                elif args.verbosity >= 1:  
                    print("The state whose capital is {} is {}".format(args.name, 
                                                                            state))
                else:
                    print(state)
