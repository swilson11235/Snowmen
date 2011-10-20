'''The block class '''
__author__ = 'Stephen and Will'
__version__ = '1.0'

class block():
    def __init__(self):
        '''Initializes a block.'''
        pass

class blockposition():
    def __init__(self):
        '''Initializes the position.'''
        self.r=r
        self.g=g
        self.b=b
    def color(self):
        tmp_tuple=(self.r,self.g,self.b)
        return tmp_tuple

class blockcolor():
    def __init__(self,r,g,b):
        '''Initializes the position.'''
        self.r=r
        self.g=g
        self.b=b
    def color(self):
        tmp_tuple=(self.r,self.g,self.b)
        return tmp_tuple

        
