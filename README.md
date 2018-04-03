**Project Name**
`CrunchbaseScraper`

**Description**
`CrunchbaseScraper` provides functionality to:
* scrape data from [crunchbase.com](http://crunchbase.com) using the `request` library of `Python` along with the crunchbase api
* store the data into an SQLite database using the `SQLAlchemy` library which provides ORM functionality to `Python`
* store the data into a JSON file using the `json` library of `Python`
* read data from the SQLite database filtered on unique company name
* read data from the JSON file filtered on unique company name

Code has been modularized into functions and written in OOP manner with usage of classes.

There are five files:
* `crunchbase.py` is the main file containing the `Crunchbase` class which provides an interface to scrape data and read-write into a database / JSON. Regex are used to extract information from the `response.text` string of `requests`.
* `database_orm.py` contains the `ORMInterface`  class which provides functionality to read and write data in an SQLite database using `SQLAlchemy` ORM. Additional classes `Company` and `SocialAccount` help define the two tables of the database namely, `companies` and `social_accounts` which are linked using a foreign key.
* `database_json.py` contains the `JsonDB` class which provides functionality to read and write data in a JSON file using the `json` library.
* `simple_scraper.py` contains the `Scraper` class which uses the `requests` library to scrape data from a given URL.
* `re_demo.py` is an additional separate file for experimental purposes to show the functionality of the StanfordCoreNLP parser in sentence splitting and tokenization. This is used to obtain the first five sentences of a text body.

**Installation**

**Usage**




