# main classes of the project

class User :
    def __init__(self, password, name, mail):
        self.__password, self.__name, self.__mail = password, name, mail
        self.__wallet = 0
    def setPassword(self, new_password):
        self.__password = new_password

class Seller(User):
  pass
class Customer(User):
  pass
class Product:
  pass

