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
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()

    glBegin(GL_TRIANGLES)
    glVertex(0, .1, 0)
    glVertex(-.1, -.1, 0)
    glVertex(.1, -.1, 0)
    glEnd()

    #glTranslate(.5, 0, 0)

    glBegin(GL_POINTS)
    glVertex(0, .5, 0)
    glVertex(-.5, -.5, 0)
    glVertex(.5, -.5, 0)
    glEnd()

    glBegin(GL_LINES)
    glVertex(.3, .3, 0)
    glVertex(.3, .4, 0)
    glVertex(.34, .78, 0)
    glEnd()

    glFlush()


if __name__ == '__main__': 
	main()







