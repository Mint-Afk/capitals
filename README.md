# European Geographic Champion 2020 :earth_africa:

The main goal of our project is to return to the user a country or a capital name of European States, given a determined input. 
The user can choose among a huge list a European capital or state in order to find its respective state or capital.

In this repository, you can find a file named ```EGC-2K19.py``` that is the core file of our project. Through a user-friendly command-line interface, it recalls the check_capital function, defined in ```capitals.py```, to check if the given input is a valid name of a European capital city, or state respectively, and return the associated capital or state. The function is gonna calibrate the verbosity of the answers if specified by (-v) argument. 

If you run the program, given the user shell input ```$ python parser.py italy -v```, it will generate results like this:
```The capital of ITALY is ROME```

```args.place``` is passed to the check function.
The dictionary in list, previously loaded by ```load_csv```, is checked as next step to find a correspondence.

All this effort to say that the capital of Italy is obviously... ROME.

## How to populate a database

To run ```EGC-2K19.py```, the user will need a **username** and a **password**. 

```dbmanager.py``` allows to add and remove users. 

If you want to add a new user, you can use the parameter ```-add```. It requires:
**-usr**: user username
**-psw**: user password

```
$ python dbmanager.py -usr test -psw test -add   User [test] succesfully added to database!
```

You also have the possibility to remove a user, using the parameter ```-rm```. It requires:
**-usr**: user username
**-psw**: user password

```
$ python dbmanager.py -usr test -psw test -rm 
Successfully removed user [test]
```

## Data Files 

The user can choose among a list of capitals and states of Europe that is stored in .csv file located in: ```/city_check/data/capital.csv```.
A dictionary is provided with 

**Valid states and capitals**:

|State                 |Capital         |
|----------------------|----------------|
|Aland Islands         |Mariehamn       |
|Albania               |Tirana          |
|Andorra               |Andorra la Vella|
|Armenia               |Yerevan         |
|Austria               |Vienna          |
|Azerbaijan            |Baku            |
|Belarus               |Minsk           |
|Belgium               |Brussels        |
|Bosnia and Herzegovina|Sarajevo        |
|Bulgaria              |Sofia           |
|Croatia               |Zagreb          |
|Cyprus                |Nicosia         |
|Czech Republic        |Prague          |
|Denmark               |Copenhagen      |
|Estonia               |Tallinn         |
|Faroe Islands         |Torshavn        |
|Finland               |Helsinki        |
|France                |Paris           |
|Georgia               |Tbilisi         |
|Germany               |Berlin          |
|Gibraltar             |Gibraltar       |
|Greece                |Athens          |
|Guernsey              |Saint Peter Port|
|Hungary               |Budapest        |
|Iceland               |Reykjavik       |
|Ireland               |Dublin          |
|Isle of Man           |Douglas         |
|Italy                 |Rome            |
|Jersey                |Saint Helier    |
|Kosovo                |Pristina        |
|Latvia                |Riga            |
|Liechtenstein         |Vaduz           |
|Lithuania             |Vilnius         |
|Luxembourg            |Luxembourg      |
|Macedonia             |Skopje          |
|Malta                 |Valletta        |
|Moldova               |Chisinau        |
|Monaco                |Monaco          |
|Montenegro            |Podgorica       |
|Netherlands           |Amsterdam       |
|Northern Cyprus       |North Nicosia   |
|Norway                |Oslo            |
|Poland                |Warsaw          |
|Portugal              |Lisbon          |
|Romania               |Bucharest       |
|Russia                |Moscow          |
|San Marino            |San Marino      |
|Serbia                |Belgrade        |
|Slovakia              |Bratislava      |
|Slovenia              |Ljubljana       |
|Spain                 |Madrid          |
|Svalbard              |Longyearbyen    |
|Sweden                |Stockholm       |
|Switzerland           |Bern            |
|Turkey                |Ankara          |
|Ukraine               |Kyiv            |
|United Kingdom        |London          |
|Vatican City          |Vatican City    |

## Command line parameters

Some command line parameters are needed in order to run our executable file.
The arguments required are:

### check_capital parameters

**list** (dict): list containing the state/capital dictionary

**args (argparse.Namespace): user sheell inputs arguments

**place**: user state/capital input

**verbosity**: user desired output verbosity

### Parse_args() parameters 

**place** (positional): the state or capital selected by the user

**-usr** (required): Insert username of the account

**-psw** (required): Insert password of the account

**-add**: add a user

**-rm**: remove a user

**-check**: check a user

**--version** (optional): show infos about the actual version of the project

**verbosity** (optional): level of verbosity chosen by the user [0 - 1 - 2]

## Testing

Test on parts of the code are provided here: ```test/test.py/```. 

To run the three TestMain Class tests you can use: ```$ python3 -m unittest -v -b test/test.py```:

```
test_empty_data (test.test.TestMain) ... ok

    test_right_data (test.test.TestMain) ... ok

    test_wrong_data (test.test.TestMain) ... ok



    ----------------------------------------------------------------------

    Ran 3 tests in 0.004s



    OK
```

## License

Apache License 2.0


