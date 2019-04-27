**Project Name**

`CrunchbaseWrapper`

**Description**

`CrunchbaseWrapper` provides functionality to:
* scrape data from [crunchbase.com](https://www.crunchbase.com/) using the `requests` library of `Python` along with the crunchbase api
* store the data into an SQLite database using the `SQLAlchemy` library which provides ORM functionality to `Python`
* store the data into a JSON file using the `json` library of `Python`
* read data from the SQLite database filtered on unique company name
* read data from the JSON file filtered on unique company name

Code has been modularized into functions and written in OOP manner with usage of classes.

There are five files:
* `crunchbase.py` is the main file containing the `Crunchbase` class which provides an interface to scrape data and read-write into a database / JSON file. Regex are used to extract information from the `response.text` string of `requests`.
* `database_orm.py` contains the `ORMInterface`  class which provides functionality to read and write data in an SQLite database using `SQLAlchemy` ORM. Additional classes `Company` and `SocialAccount` help define the two tables of the database namely, `companies` and `social_accounts` which are linked using a foreign key.
* `database_json.py` contains the `JsonDB` class which provides functionality to read and write data in a JSON file using the `json` library.
* `simple_scraper.py` contains the `Scraper` class which uses the `requests` library to scrape data from a given URL.
* `re_demo.py` is an additional separate file for experimental purposes to show the functionality of the StanfordCoreNLP parser in sentence splitting and tokenization. This is used to obtain the first five sentences of a text body.

**Installation**

A `setup.py` file is present which installs the required dependencies automatically on running:
`python3 setup.py develop`

**Usage**

To test the project:
* run `python3 crunchbase.py` which will provide a menu driven interface
* choose option `1` to get data from crunchbase and write it into an SQLite database and JSON file
* choose option `3` to retrieve the data based on a company name (ex: apple) which is also entered
* choose option `1` again to show that data is not added if it already exists
* choose option `4` to exit

On exit, `crunchbase_json.db` and `crunchbase_data.json` would have been created.


