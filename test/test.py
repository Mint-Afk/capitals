'''Test suite for the project.

The TestMain Class include three easy tests:
 - Smoke Test, that test some valid input
 - One test with invalid input
 - One test which try a corner case.

Example:
User input:

    $ python3 -m unittest -v -b test/test.py

Give back:

    test_empty_data (test.test.TestMain) ... ok
    test_right_data (test.test.TestMain) ... ok
    test_wrong_data (test.test.TestMain) ... ok

    ----------------------------------------------------------------------
    Ran 3 tests in 0.004s

    OK

.. _Git-hub Repository:
   https://github.com/Mint-Afk/EUROPEAN-GEOGRAPHY-CHAMPION-2K20--PRO-.git

'''

import unittest
from city_check.scripts import capitals
import os
import tempfile


class TestMain(unittest.TestCase):
    '''Contains three test cases for valid, invalid and corner cases.'''
    def setUp(self):
        self.right_file = tempfile.NamedTemporaryFile(mode='w+', delete=True)
        self.right_file.write('ITALY;ROME')
        self.wrong_format = tempfile.NamedTemporaryFile(mode='w+', delete=True)
        self.right_file.write('ITALY,ROME')
        self.empty_file = tempfile.NamedTemporaryFile(mode='w+', delete=True)

    def test_right_data(self):
        self.right_file.seek(0)
        u = capitals.load_csv(filename=self.right_file.name)
        self.assertTrue(u)

    def test_wrong_data(self):
        self.wrong_format.seek(0)
        u = capitals.load_csv(filename=self.wrong_format.name)
        self.assertFalse(u)

    def test_empty_data(self):
        self.empty_file.seek(0)
        u = capitals.load_csv(filename=self.empty_file.name)
        self.assertFalse(u)

    def tearDown(self):
        self.right_file.close()
        self.wrong_format.close()
        self.empty_file.close()
