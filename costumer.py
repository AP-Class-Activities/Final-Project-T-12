import re

from sre_constants import error  # for checking password validation 

class user:
    # A USER has a (first  and last name), an email, password and id

    def __init__(self,first,last,email,password,id):
        
        self.__first,self.__last,self.__email = first,last,email
        
        #checking password validation(description is in setter section)
        if len(password)>=8 : #(1) condition 
            if re.search('[0-9]',password) is None : #(2) condition 
                raise ValueError("Make Sure Your Password Has At Least One Number  \n")
            elif re.search('[A-Z]',password) is None : #(3) condition
                raise ValueError('Make Sure Your Password Has At Least One Capital Letter  \n')
        else : 
            raise ValueError("Password Should Be At Least 8 Characters \n")
        self.__password = password
        
        #checking id validation(only digits and len == 10)
        if len(id) != 10 : 
            raise error("ID should be 10 digits")
        self.__id = id

        
                                 ###setter and getters###
    
# A getter to get (first and last) name to print ==> full name (does not need a setter)

    @property
    def full_name(self): 
        return '{} {}'.format(self.__first,self.__last)
    
# A getter setter for first name

    @property
    def first(self): 
        return self.__first
    @first.setter
    def first(self,value): 
        self.__first = value
    
# A getter setter for last name

    @property
    def last(self): 
        return self.__last
    @last.setter
    def last(self,value) :
        self.__last =  value
    
# A getter setter for email...

    @property
    def email(self) :
        return self.__email
    @email.setter
    def email(self,value) : 
        self.__email = value
    
# A getter setter for password

    @property
    def password(self) : 
        return self.__password
        
    @password.setter
    
        #password has some conditions like : 
        #1) have at least 8 charactars
        #2) have at least 1 Number
        #3) have at least 1 Capital character
        
    	
    def password(self,value):
        
        if len(value)>=8 : #(1) condition 
            if re.search('[0-9]',value) is None : #(2) condition 
                raise ValueError("Make Sure Your Password Has At Least One Number  \n")
            elif re.search('[A-Z]',value) is None : #(3) condition
                raise ValueError('Make Sure Your Password Has At Least One Capital Letter  \n')
        else : 
            raise ValueError("Password Should Be At Least 8 Characters \n")
        self.__password = value
        
# A getter setter for id
    @property
    def id(self): 
        return self.__id
    @id.setter
    
#checking id validation(only digits and len == 10)

    def id(self,value):
        if len(id) != 10 : 
            raise error("ID should be 10 digits")
        self.__id = value
# printing all user's info
    def __str__(self) -> str:
        return "fullname : {} , email : {} , password : {} , id : {} ".format(self.full_name,self.email,self.password,self.id)
        
#testing user class   
obj1 = user("sina","amareh","sina_amareh@gmail.com",input("enter password : "),input("Enter Id : "))

print(obj1.full_name)
print(obj1.first)
print(obj1.last)
print(obj1.email)
print(obj1)

