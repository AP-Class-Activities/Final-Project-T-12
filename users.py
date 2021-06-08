
import re
from exceptions import Error
"""
Basic Classes for Shop Objects 

- User : The Parent Class for Seller and Customer
- Seller : Seller Users
- Customer : Customer Users
- Product : Products

- User :
-- name     : (str) first_name + last_name
-- email    : (str) 
-- birth_year : (int)
-- password : (str) ( min: 8 char, 1 cap, 1 num  )
-- wallet   : (int) 

"""

class User :
  " CHECK PASSWORD METHOD "
    def checkPassword(self, password):
        status = True
        errors = []
        if len(password) < 8:
            status = False
            errors.append(1)
        if re.search('[0-9]', password) is None :
            status = False
            errors.append(2)
        if re.search('[A-Z]', password) is None :
            status = False
            errors.append(3)
        if re.search('[a-z]', password) is None :
            status = False
            errors.append(4)
        return {'status': status, 'errors': errors}
    " CHECK EMAIL METHOD "
    def checkEmail(self, email):
        pattern = '^(\w|\.|\_|\-)+[@](\w|\_|\-)+[.]\w{2,3}$'
        if re.search(pattern, email) :
            return True
        else :
            return False
    
    def __init__(self, first_name, last_name, email, birth_year, password) :
        self.__first_name, self.__last_name = first_name, last_name
        if not checkEmail(email) :
            raise Error("invalid email")
        self.__email = email
        password_status = checkPassword(password)
        if not password_status.get('status') :
            raise Error("weak password", code = password_status.get('errors'))
        self.__password = password
