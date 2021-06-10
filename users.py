
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
          
    " CHECK BIRTH_YEAR "
    def checkBirthyear(self, birth_year):
        if birth_year <= 1382 and birth_year >= 1300 :
            return True
        return False
    
    def __init__(self, first_name, last_name, email, birth_year, password) :
        self.__first_name, self.__last_name = first_name, last_name
        if not self.checkEmail(email) :
            raise Error("invalid email")
        self.__email = email
        password_status = self.checkPassword(password)
        if not password_status.get('status') :
            raise Error("weak password", code = password_status.get('errors'))
        self.__password = password
        if not self.checkBirthyear(birth_year) :
            raise Error("invalid birth year")
        self.__birth_year = birth_year
        
                   #####setters and getters#####
    " first_name property "
    @property
    def first_name(self):
        return self.__first_name
    @first_name.setter
    def first_name(self, new_first_name):
        self.__first_name = new_first_name
    
    " last_name property "
    @property
    def last_name(self):
        return self.__last_name
    @last_name.setter
    def last_name(self, new_last_name):
        self.__last_name = new_last_name
    
    " full_name property (getter only) "
    @property
    def full_name(self):
        return self.__first_name +" "+ self.__last_name
      
    " email property "
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, new_email):
        if not self.checkEmail(new_email):
            raise Error("invalid email")
        self.__email = new_email
    
    " birth_year property "
    @property
    def birth_year(self):
        return self.__birth_year
    @birth_year.setter
    def birth_year(self, new_birth_year):
        if not self.checkBirthyear(new_birth_year):
            raise Error("invalid birth year")
        self.__birth_year = new_birth_year
    
    " password property "
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, new_password):
        password_status = self.checkPassword(new_password)
        if not password_status.get('status'):
            raise Error("weak password", code = password_status.get('errors'))
        self.__password = new_password


        " user wallet "
        self.__wallet = 0
        
            " user wallet "
    @property
    def wallet(self):
        return self.__wallet

    " financial actions "
    def deposit(self, amount):
        if amount > 0:
            self.__wallet += amount
            return True
        return False
    def withdraw(self, amount):
        if self.__wallet > amount + 999 :
            self.__wallet -= amount
            return True
        return false
    #seller class
       class Seller(User):
    def __init__(self, first_name, last_name, email, birth_year, password):
        super().__init__(first_name, last_name, email, birth_year, password)
        
        " generating ID requires database "
        self.__SL_ID = "SL"+ self.gen_id()
        
        " seller products list : list of product ids "
        self.__products = []  
