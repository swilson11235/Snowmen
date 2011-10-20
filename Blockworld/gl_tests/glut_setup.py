from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys

name = 'Example'
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutCreateWindow(name)
    glutDisplayFunc(display)
    glutMainLoop()


def display():
    print "DISPLAY!"


if __name__ == '__main__': 
	main()







