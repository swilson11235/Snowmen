
__author__ = 'Stephen'
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
        self.factor=1
    def rendercamera(self):
        glRotatef(-self.x_rot , 1.0, 0.0, 0.0)
        glRotatef(-self.y_rot , 0.0, 1.0, 0.0)
        glRotatef(-self.z_rot , 0.0, 0.0, 1.0)
        glTranslatef(0, 0, -self.posz )
        glScale(self.factor,self.factor,self.factor)
    def strafeleft(self):
        print "Camera is at: ", self.posx, self.posy, self.posz
        self.posx-=.1
        if self.posx<0:
            self.factor-=.1
        if self.posx>0:
            self.factor+=.1
        if (self.posz or self.posx)==0:
            pass
        else:
            self.y_rot = math.tan(self.posz/self.posx)*180/math.pi
    def straferight(self):
        print "Camera is at: ", self.posx, self.posy, self.posz
        self.posx+=.1
        if self.posx>0:
            self.factor-=.1
        if self.posx<0:
            self.factor+=.1
        if (self.posz or self.posx)==0:
            pass
        else:
            self.y_rot = math.tan(self.posz/self.posx)*180/math.pi
    def moveup(self):
        self.posy+=.1
    def movedown(self):
        self.posy-=.1
    def walkin(self):
        self.posz-=.1
    def walkout(self):
        self.posz+=.1
