'''The block class.'''
__author__ = 'Stephen and Will'
__version__ = '1.0'

class block:
    def __init__(self,blocktuple=((0,0,0),(0,0,1),(1))):
        '''Initializes a block. Blocktuple has a position tuple followed by a color tuple.'''
        self.pos = blockposition(blocktuple[0])
        self.col = blockcolor(blocktuple[1])
        self.siz = blocksize(blocktuple[2])
    def __getitem__(self):
        return [self.pos,self.col,self.siz]
    def changecolor(self,tup):
        self.col.color(tup)
    def changeposition(self,tup):
        self.pos.position(tup)
    def changesize(self,tup):
        self.siz.size(tup)

class blockposition:
    def __init__(self,postup):
        '''Initializes the position.'''
        self.postup=postup
    def __getitem__(self):
        return self.postup
    def position(self,postup=()):
        if not postup==():
            self.postup=postup
        return self.postup

class blockcolor:
    def __init__(self,coltup):
        '''Initializes the color.'''
        self.col=coltup
    def __getitem__(self):
        return self.col
    def color(self,coltup=()):
        if not coltup==():
            self.col=coltup
        return self.col

class blocksize:
    def __init__(self,tup):
        '''Initializes the size.'''
        self.sizetup=tup
    def __getitem__(self):
        return self.sizetup
    def size(self,tup=()):
        if not tup==():
            self.sizeup=tup
        return self.sizetup        
