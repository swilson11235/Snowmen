
__author__ = 'Stephen and Will'
__version__ = '1.0'
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *            
import math

class camera():
    def __init__(self,):
        '''Initializes a camera.'''
        self.x_rot=0
        self.y_rot=0
        self.z_rot=0
        self.posx=0
        self.posy=0
        self.posz=3
        self.factor=10
        self.tmp_y_rot=0
        self.tmp_x_rot=0
        self.tmp_z_rot=0
    def rendercamera(self):
        glRotatef(-self.x_rot , 1.0, 0.0, 0.0)
        glRotatef(-self.y_rot , 0.0, 1.0, 0.0)
        glRotatef(-self.z_rot , 0.0, 0.0, 1.0)
        glTranslatef(-self.posx, -self.posy, -self.posz )
    def strafeleft(self,num=10.0):
        self.posx-=.1
    def straferight(self):
        self.posx+=.1
    def moveup(self):
        self.posy+=.1
    def movedown(self):
        self.posy-=.1
    def walkin(self):
        self.posz-=.1
    def walkout(self):
        self.posz+=.1
    def rotate(self,num=10.0):
        self.tmp_y_rot+=float(num)
        if self.tmp_y_rot>360:
            self.tmp_y_rot=0
        self.posz = 3*math.cos(self.tmp_y_rot/180*math.pi)
        if self.tmp_y_rot==90 or self.tmp_y_rot==270:
            self.y_rot+=180

        self.tmp_x_rot+=float(num)
        if self.tmp_x_rot>360:
            self.tmp_x_rot=0
        self.posy = math.sin(self.tmp_x_rot/180*math.pi)
        if self.tmp_x_rot==90 or self.tmp_x_rot==270:
            self.factor*=-1
        self.x_rot= self.x_rot-self.factor



        
