import json

class JsonDB(object):
    '''
    The JsonDB provides data storage operations in JSON
    '''
    def __init__(self, filename_ctr):
        self.filename = filename_ctr
    def write_data(self, json_data):
        with open(self.filename, 'w') as outfile:
            data = json.dump(json_data, outfile)        
    def read_data(self, name):
        with open(self.filename, 'r') as infile:
            data = json.load(infile)                  
        datum = data[name.lower()]
        print ("Company details from JSON file: \n")
        for key in datum.keys():
            print (key, " : ", datum[key])
        print ("\n")
