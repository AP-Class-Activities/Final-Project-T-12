
" Error Class "
class Error(Exception):
    """
    a custome exception for handling errors while validating data and.. in the Shop
    returns a error message and (an/some) error codes with or without additional data (if needed)
    """
    def __init__(self, message, code=0, data= {}):
        self.message = message
        self.code = code
        self.data = data
