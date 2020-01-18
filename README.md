
# EGC-2K20 :earth_africa: | European Geography Champion 2020 

*A lightweight and fast tool to answer any state<->capital connexion, and viceversa. 
The main goal of our project is to return to the user a country or a capital name of European states through a user-friendly interface, given a determined user input.*

---
## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

---
### Prerequisites 
You can download all the necessary files to get the app functioning from:
.. _Git-hub Repository: [github.com/mintafk/EGC-2K20](https://github.com/Mint-Afk/EUROPEAN-GEOGRAPHY-CHAMPION-2K20--PRO-.git) 

Libraries contains built-in modules that provide access to system functionality as well as modules written in Python that provide standardized solutions for many problems that occur in everyday programming.
>  **Note:** the project requires the following modules to run: *os, argparse, sqlite3, random, csv, tempfile, hashlib, unittest, request, json* and *sys*.


Some of them are not included in the Python Standard Library and so you are going to need to download and install them through the command line. 
The command ```$ pip3 install library_name``` is gonna bring the desired result in most of the cases.

---

The system support a **User Management System** and so, you are going to need a valid username and password to login every time you execute the program.

---
### Populate the Database
To setup usernames and passwords, you will need to execute ```dbmanager.py``` from the command line. 

```$ python dbmanager.py -usr test -psw test -add/check/rm```

This will enable you to:
- **ADD** a new user
```
$ python dbmanager.py -usr test -psw test -add

User [test] succesfully added to database!
```
- **CHECK** an existing user 
```
$ python dbmanager.py -usr test -psw test -check

Credentials for user [test] are the correct ones!
```
- **REMOVE** an old user
```
$ python dbmanager.py -usr test -psw test -rm

Successfully removed user [test]
```
All the users and their passwords are saved in ```database.db``` file in the repository. Passwords are stored as digests, computed with a salt plus hash repetition for improved security.

>  **Note:** database manager can support only one operation at a time. Cannot *add* and *check* or *remove* at the same time.

---
Once all is ready to go, execute the main file with: 

```$ python EGC-2K20.py Italy -usr test -psw test -v```

it will give you results the following result:

```The capital of ITALY is ROME```

The user can now choose among any European capital or state in order to find its respective state or capital in a heartbeat. Using optional parameters he may also:
- calibrate the verbosity level of the ouput (4 levels);
- get info's about the version and the developers;

## Command line parameters 
As we have just mentioned, some command line parameters are required in order to run the main script.

#### Positional arguments
- **place**: the state or capital selected by the user, ready to be matched with its correlative. 
> **Note:** Only one place at a time can be passed and processed. 

#### Optional & Required arguments
- **-h, --help:** show the helper and exit.  
- **-v:, --verbosity** Augment verbosity level. There are 4 level of verbosity.   
- **-usr [required]:** Insert username of the account (requires *-p*).  
- **-psw [required]:** Insert password of the account.
- **--version:** show infos about the project.

>  **Note:** *verbosity* level goes from 0 to 3. Where 0 will give back only the answer, gradually increment the lengthiness till the 3rd level, at max verbosity the app will give you back all the info's about the country fetched from restcountries.eu API's.
 
## Running the tests
In the folder ```city_check/test``` you may find the ```test.py``` module wich is used to make automated tests for this system.

```
test_empty_data (test.test.TestMain) ... ok
test_right_data (test.test.TestMain) ... ok
test_wrong_data (test.test.TestMain) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.004s
OK
```
To run those  tests use:

```$ python3 -m unittest -v -b test/test.py```:

>  **Note:** Pay attention to call the tests from the main folder to work correctly.

### Break down into end to end tests
Through the  ```setUp``` function, we are going to create 3 temporary files using the ```tempfile``` library. The tests are done to check the correct functioning of the function ```load_csv``` in the ```city_check/scripts/capitals``` module. 

In particular:
- **SMOKE TEST** 
- **EMPTY FILE TEST**
- **WRONG FORMAT TEST**

The function ```load_csv``` handles all the exceptions correctly.


## Data  
States and capitals datas are stored in *.csv* files located in: ```city_check/data/capital.csv```.  Till now there are about 58 supported country.

> **Note:** More places will be reached in the next release i.e. worldwide 


## Documentation
Documentation can be found in ```docs``` folder and provides comments and explanations about the modules and functions that you can find in the various modules. Main page file is located in ```_build/html/index.html```.
 
 To read them with your browser, from the main folder use ```$ open docs/_build/html/index.html```.
 
 >**Documentation made with: [Sphinx](http://www.sphinx-doc.org/en/master/).**
>> **Docstrings : [Google Style](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).**


## Contributing
Everyone is welcome to contribute to this repository, but please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change. 

### Pull Request Process
1. Ensure any install or build dependencies are removed before the end of the layer when doing a build.
2. Update the README with details of changes to the interface, this includes new environment variables, exposed ports, useful file locations and container parameters.
3. Increase the version numbers to the new version that this Pull Request would represent. 

## Authors
- ```MATTEO CARNIEL -> matteo.carniel@student.h-farm.com```

###  Support
You need help? Get in touch with me.

### Contributors
Thank you all for the collaboration! 
- **Giorgia Fanton** 
- **Francesco Pedrini** 

##  License
[APACHE 2.0](https://choosealicense.com/licenses/apache-2.0/)
