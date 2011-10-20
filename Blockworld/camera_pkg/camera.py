'''The camera class allows for manipulation of a theoretical camera in a OpenGl object.'''
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
       # self.current=0
    def rendercamera(self):
        '''Renders the camera.'''
        glRotatef(-self.x_rot , 1.0, 0.0, 0.0)
        glRotatef(-self.y_rot , 0.0, 1.0, 0.0)
        glRotatef(-self.z_rot , 0.0, 0.0, 1.0)
        glTranslatef(-self.posx, -self.posy, -self.posz )
    def strafeleft(self,num=10.0):
        '''Does a basic strafe left.'''
        self.posx-=.1
        #self.current=0
    def straferight(self):
        '''Does a basic strafe right.'''
        self.posx+=.1
        #self.current=0
    def moveup(self):
        '''Does a basic move up.'''
        self.posy+=.1
       # self.current=0
    def movedown(self):
        '''Does a basic move down.'''
        self.posy-=.1
       # self.current=0
    def walkin(self):
        '''Walks in properly.'''
        self.posz-=.1
       # self.current=0
    def walkout(self):
        '''Walks out properly.'''
        self.posz+=.1
       # self.current=0
    def rotate(self,num=10.0):
        '''Does a rotation around the x axis. Takes a num that relates to how fast in degrees to rotate.'''
        # self.current+=1
        # if self.current==1:
        #     self.tmp_y=self.posy
        #     self.tmp_x=self.posx
        #     self.tmp_z=self.posz
        self.tmp_y_rot+=float(num)
        if self.tmp_y_rot>360:
            self.tmp_y_rot=0
        self.posz = 3*math.cos(self.tmp_y_rot/180*math.pi)
        if self.tmp_y_rot==90 or self.tmp_y_rot==270:
            self.y_rot+=180
       
        self.tmp_x_rot+=float(num)
        if self.tmp_x_rot>360:
           # glTranslatef(-self.tmp_x,self.tmp_y, self.tmp_z)
            self.tmp_x_rot=0
        self.posy = math.sin(self.tmp_x_rot/180*math.pi)
        if self.tmp_x_rot==90 or self.tmp_x_rot==270:
            self.factor*=-1
        self.x_rot= self.x_rot-self.factor
        print self.posx,self.posy,self.posz

        
