#! /usr/bin/env python3
'''Executable file of the EGC - European Geography Champion 2020 Project

Example:
    Given user shell input:

        $ python parser.py italy -v

    Gonna answer back:

        The capital of ITALY is ROME

.. _Git-hub Repository:
   https://github.com/Mint-Afk/EUROPEAN-GEOGRAPHY-CHAMPION-2K20--PRO-.git

'''

import argparse
import os
import dbmanager
from city_check.scripts import capitals as cpt

csv_path = 'city_check/data/capital.csv'


def parse_args():
    '''Command line option and argument parsing.

    The function use argparse to write user-friendly command-line interfaces.
    The argparse module also automatically generates help and usage messages
    and issues errors when users give the program invalid arguments.

    Arguments:
        place (positional): the state or capital selected by the user
        ["-usr"] (required): Insert username of the account
        ["-psw"] (required): Insert password of the account
        ["-v", "--verbosity"] (optional): level of verbosity [0-1-2]
        [--version] (optional): show infos about the project

    Returns:
        argparse.Namespace: user shell inputs arguments
    '''
    parser = argparse.ArgumentParser(
        description="Knows all about capitals and states in Europe",
        prog="European Geography Champion 2020",
        usage="%(prog)s [options]")
    parser.add_argument(
        "place",
        help="Write the name of a European state or capital",
        type=str.upper)
    parser.add_argument(
        '-usr',
        help="Write your username here",
        required=True)
    parser.add_argument(
        '-psw',
        help="Write your password here",
        required=True)
    parser.add_argument(
        "-v",
        "--verbosity",
        help="Increase incrementally verbosity",
        action="count",
        default=0)
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s v1.0, Dec 2019 by MFGAsoftware")

    arguments = parser.parse_args()
    return arguments


if __name__ == "__main__":
    ''' Execute code only if the file was run directly.'''
    dbmanager.open_and_create('database.db')
    list_of_capitals = cpt.load_csv(csv_path)
    args = parse_args()
    if dbmanager.check_user(args.usr, args.psw):
        cpt.check_capital(list_of_capitals, args)
    else:
        print('''
              Sorry, wrong username password selected!
              You may wanna register a new account through dbmanager app.
              ''')
