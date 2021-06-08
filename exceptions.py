" Exceptions "

" Error Exception Class "
" used to handle errors while create and edit users in shop "

class Error(Exception):
    def __init__(self, message, code=0, data= {}):
        self.message = message
        self.code = code
        self.data = data
