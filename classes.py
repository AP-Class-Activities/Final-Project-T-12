# main classes of the project

class User :
    def __init__(self, password, name, mail):
        self.password, self.name, self.mail = password, name, mail
        self.wallet = 0


class Seller(User):
  pass
class Customer(User):
  pass
class Product:
  pass

