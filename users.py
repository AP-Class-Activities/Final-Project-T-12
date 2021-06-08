
import re

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
