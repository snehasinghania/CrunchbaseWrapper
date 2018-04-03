import requests
import json

class Scraper(object):
    '''
    The Scraper class will provide the functionality to scrape data from a url given some parameters.
    '''
    def scrape_data(self, base_url, user_key, company_name, org_type):
        querystring = {"user_key":user_key, "name":company_name, "organization_types":org_type}
        response = requests.request("GET", base_url, params=querystring)
        return response.text   
