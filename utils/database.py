"""
the Database class for working with json files.
designed for Online Shop Project

use this like and attr in user or product classes.
"""

import json
import os

class Database :
    def __init__(self, str: filename = "database") :
        self.FILENAME = filename + ".json"
        
        " if the file exists, load its contents "
        if os.path.exists(filename) and os.path.isfile(filename):
            with open(self.FILENAME, 'r') as f :
                self.CONTENTS = json.load(f)
        " when file not exists, create one and save an empty json array in it! "
        else :
            self.CONTENTS = dict()
            with open(self.FILENAME, 'w') as f :
                json.dump(self.CONTENTS, f)
    
    " getContents method returns all the data from file and updates the CONTENTS attr. "
    def getContents(self) :
        with open(self.FILENAME, 'r') as f :
            self.CONTENTS = json.load(f)
        return self.CONTENTS
    
    " putContents method saves all data in the CONTENTS attr. in the file. "
    def putContents(self) :
        with open(self.FILENAME, 'w') as f :
            json.dump(self.CONTENTS, f)
    
    " editContents method edits data of the item with given unique id. "
    def editContents(self, int: uid, dict: data) :
        self.getContents()
        if uid in self.CONTENTS.keys() :
            self.CONTENTS.get(uid).update(data)
        else :
            self.CONTENTS[uid] = data
        self.putContents()
    
    """
            ::  HELPER METHODES  ::
        
        getNewID -returns a new ID for using
        get -returns the data of a given field
        
        """
    def getNewID(self) :
        self.getContents()
        return len(self.CONTENTS)
    
    def get(self, field) :
        self.getContents()
        if field in self.CONTENTS.keys() :
            return self.CONTENTS.get(field)
        else :
            return False
