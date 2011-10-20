'''This program uses the camera class to make snowmen that can be rotated.''' 

__author__ = 'Stephen and Will'
__version__ = '1.0'


from block_pkg import block
from lxml import etree

class Blockworld:
    def __init__(self):
        self.blocknum=0
        self.blockobjects=[]
        self.blocks=[]
        self.block=[]
        self.myblocks=[]
    def __getitem__(self):
        return self.myblocks
    def main(self):
        self.xml_import()
    def xml_import(self,fl_name='blockworld.xml'):
        tree= etree.parse(fl_name)
        self.blocknum=len(tree.xpath('//BLOCK'))
        self.blockobjects=tree.xpath('//BLOCK')
        for block in self.blockobjects:
            for dat in block:
                tagls=[]
                tagls.append([item.tag for item in dat.iter()])
                tagls.append([item.text for item in dat.iter()])
                self.block.append([tagls[0][0],tagls[1][0]])
            self.blocks.append(self.block)
            self.block=[]
        self.create_block()
    def create_block(self):
        postup=[]
        colortup=[]
        sizetup=[]
        postmp=[]
        colortmp=[]
        sizetmp=[]
        for i in range(self.blocknum):
            for n in range (len(self.blocks[0])):
                if self.blocks[i][n][0]=='X' or self.blocks[i][n][0]=='Y' or self.blocks[i][n][0]=='Z':
                    postmp.append(float(self.blocks[i][n][1]))
                if self.blocks[i][n][0]=='RED' or self.blocks[i][n][0]=='GREEN' or self.blocks[i][n][0]=='BLUE':
                    colortmp.append(float(self.blocks[i][n][1]))
                if self.blocks[i][n][0]=='BLOCKSIZE':
                    sizetmp.append(float(self.blocks[i][n][1]))
            postup.append(postmp)
            colortup.append(colortmp)
            sizetup.append(sizetmp)
            postmp=[]
            colortmp=[]
            sizetmp=[]

        for i in range(self.blocknum):
            myblock=block()
            self.myblocks.append(myblock)
            self.myblocks[i].changeposition(postup[i])
            self.myblocks[i].changecolor(colortup[i])
            self.myblocks[i].changesize(sizetup[i])

if __name__ == '__main__': 
    blockworld = Blockworld()
    blockworld.main()

