'''This program uses the camera class to make snowmen that can be rotated.''' 

__author__ = 'Stephen and Will'
__version__ = '1.0'

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
from camera_pkg import camera

name = 'Snowmen'
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

class Snowmen:
    def __init__(self):
        self.my_camera= camera()

    def main(self):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        glutCreateWindow(name)

        light_specular = (.3, .3, .3, .1)
        light_position = (.5, 1, -1, 1)
        glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
        glLightfv(GL_LIGHT0, GL_POSITION, light_position)

        light_ambient = (1, 1, 1, 1)
        light_position = (0, 0, 1, 0)
        glLightfv(GL_LIGHT1, GL_AMBIENT, light_ambient)
        glLightfv(GL_LIGHT1, GL_POSITION, light_position)

        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHT1)

        glMatrixMode(GL_PROJECTION)
        gluPerspective(45,1,.15,100)
        glMatrixMode(GL_MODELVIEW)
        glEnable(GL_DEPTH_TEST)
        glutKeyboardFunc(self.keyPressed)
        glutDisplayFunc(self.display)
        glutIdleFunc(self.display)
        glutMainLoop()

    def keyPressed(self,key,x,y):
        print "Pressed key: ", key
        if key == 'a':
            self.my_camera.strafeleft()
        if key == 'd':
            self.my_camera.straferight()
        if key == 'w':
            self.my_camera.moveup()
        if key == 's':
            self.my_camera.movedown()
        if key =='e':
            self.my_camera.walkin()
        if key == 'c':
            self.my_camera.walkout()
        if key=='r':
            self.my_camera.rotate()


    def display(self,x=-.5, y=-.5,z=0,number=3):
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        self.my_camera.rendercamera()

        size=0.3
        for i in range(number):
            self.draw_snowman(x,y,z,size)
            x=.6
            y=.1
            z=0
        glFlush()

    def draw_snowman(self,x,y,z,size):
        glMaterial(GL_FRONT, GL_AMBIENT, (.5, .5, .5));
        glTranslate(x,y,z)
        glutSolidSphere(size, 40, 40)
        glTranslate(0,size/3*2,0)
        glutSolidSphere(size/3*2, 40, 40)
        glTranslate(0,size/3*2,0)
        glutSolidSphere(size/2, 40, 40)


if __name__ == '__main__': 
    snowmen = Snowmen()
    snowmen.main()

