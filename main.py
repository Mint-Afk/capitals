#! /usr/bin/env python3

""" 
Import capitals module from the python package,
recalling the function check_capital. 
"""

import city_check.capitals as cpt
import sys


if __name__ == "__main__":
    """
       If sys was given an argument through the shell by user,
       it will call back to check_capital function from the module
       and give back the results.
    """
    if len(sys.argv) > 1:  
    """
       Now perform test on check_capital function.
    """
        if sys.argv[1] == 'check': 
            cpt.check_capital("Germany")
            cpt.check_capital("Honduras")
            cpt.check_capital("Rome")
            cpt.check_capital("Tokyo")
        else:
            for arg in range(1,len(sys.argv)):
                cpt.check_capital(sys.argv[arg])
    else:
        print("pls insert any input through shell")
        exit()
