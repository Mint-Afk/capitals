#! /usr/bin/env python3
'''Executable file of the EGC - European Geography Champion 2020 Project by MFGAsoftware©

Example:
    Given user shell input:

        $ python parser.py italy -v

    Gonna answer back:

        The capital of ITALY is ROME

.. _Git-hub Repository:
   https://github.com/Mint-Afk/capitals.git

'''

import argparse
import os
from city_check.scripts import capitals as cpt


def parse_arguments():
    '''Command line option and argument parsing.

    The function use argparse to write user-friendly command-line interfaces. 
    The argparse module also automatically generates help and usage messages 
    and issues errors when users give the program invalid arguments. 

    Arguments:
        name (positional): the state or capital selected by the user
        verbosity (optional): level of verbosity chosen by the user [0 - 1 - 2]  

    Returns:
        argparse.Namespace: user shell inputs arguments
'''
    parser = argparse.ArgumentParser(
        description="Knows all about capitals and states in Europe",
        prog="European Geography Champion 2020",
        usage="%(prog)s [options]")
    parser.add_argument(
        "name",
        help="write the name of a European state or capital",
        type=str.upper)
    parser.add_argument(
        "-v",
        "--verbosity",
        help="Increase incrementally verbosity",
        action="count",
        default=0)
    parser.add_argument(
        "--version", 
        action="version", 
        version="%(prog)s 1.0, Dec 2019 by MFGAsoftware©")

    args = parser.parse_args() 
    return args


if __name__ == "__main__":
    path = os.path.abspath(os.path.join(os.getcwd(),
                                        'city_check/data/capital.csv'))
    list_of_capitals = cpt.load_csv(path)
    args = parse_arguments()
    cpt.check_capital(list_of_capitals, args)
