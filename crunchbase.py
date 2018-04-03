#importing python libraries
import sys
import re
import json
from collections import OrderedDict
#importing user written modules
import simple_scraper
import database_orm
import database_json


class Crunchbase(object):
    '''
    The Crunchbase class provides the functionality to scrape crunchbase info and write into a database 
    along with future retrievals of data from the database
    '''
    #personal cruchbase api key
    def __init__(self, base_url_ctr = "https://api.crunchbase.com/v3.1/odm-organizations", user_key_ctr = "698e40ad22a4bd98abbaac2e909a64b5", org_type_ctr = "company"):
        self.base_url = base_url_ctr
        self.user_key = user_key_ctr
        self.org_type = org_type_ctr
        self.my_scraper = simple_scraper.Scraper()
        self.orm_object = database_orm.ORMInterface()
        self.json_handler = database_json.JsonDB("crunchbase_data.json")
        
    def extractFeatures(self, data):
        '''
        Extracts attributes (name, website, etc) of a company from request response.text string using regex functions
        '''
        #extract attributes from request output using regex functions
        data = str(data.replace("null", "\"null\""))
        properties = re.findall("\"properties\":\{(.*?)\}", data)
        properties = properties[0]
        name = re.findall("\"name\":\"(.*?)\"", properties)[0]  
        website = re.findall("\"homepage_url\":\"(.*?)\"", properties)[0]
        facebook_url = re.findall("\"facebook_url\":\"(.*?)\"", properties)[0]
        twitter_url = re.findall("\"twitter_url\":\"(.*?)\"", properties)[0]
        linkedin_url = re.findall("\"linkedin_url\":\"(.*?)\"", properties)[0]
        social_links = [facebook_url, twitter_url, linkedin_url]
        stock_symbol = re.findall("\"stock_symbol\":\"(.*?)\"", properties)[0]
        summary = re.findall("\"short_description\":\"(.*?)\"", properties)[0]       
        return OrderedDict([("name", name), ("website", website), ("twitter_url", twitter_url), ("facebook_url", facebook_url), ("linkedin_url", linkedin_url), ("stock_symbol", stock_symbol), ("summary", summary)])
        
    def getInfo(self):
        print ("\n")
        json_data = {}
        company_list = ["apple", "netflix", "nvidia", "uber", "linkedin"]
        for company_name in company_list:
            #use the scraper in simple_scraper.py to get data
            info = self.my_scraper.scrape_data(self.base_url, self.user_key, company_name, self.org_type)
            #extract attributes using regex
            dict_item = self.extractFeatures(info)            
            #write data into database using SQLAlchemy writer in database_orm.py
            item = []
            for val in dict_item.values():
                item.append(val)
            self.orm_object.write_row(item)
            #prepare data for json dump
            json_data[company_name] = dict_item
        #dumping data into json file
        print ("Writing data into JSON file")
        self.json_handler.write_data(json_data)
        print ("\n")
            
    def updateInfo(self):
        #this method will be implemented after clarifying the requirements of caching
        #for now it functions the same way as getInfo
        print ("\n")
        self.getInfo()  
        print ("\n")      
        
    def readInfo(self):
        name = input("Enter company name: ")
        #use the SQLAlchemy reader to retrieve row from database
        self.orm_object.read_row(name)
        self.json_handler.read_data(name)


if __name__ == "__main__":
    '''    
    difference between get info and update info:    
    get info obtains data for the very first time while
    update info updates existing data in the database assuming some copy of data is present
    therefore update info should not be called before atleast one call to get info
    '''
    base = Crunchbase()    
    #implementing a menu driven interface using dictionaries to simulate a switch case
    menu = {"1" : ("Get Crunchbase Info", base.getInfo),
            "2" : ("Update Crunchbase Info", base.updateInfo),
            "3" : ("Read Crunchbase Info", base.readInfo),
            "4" : ("Exit", sys.exit)}
    while(True):
        for key in sorted(menu.keys()):
            print (key + ":" + menu[key][0])
        choice = input("Your choice: ")
        #if key is not present then exit   
        menu.get(choice, [None, sys.exit])[1]()        
