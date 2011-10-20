from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys

name = 'Example'
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400




def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutCreateWindow(name)

    glutDisplayFunc(display)
    #glutIdleFunc(display)
    glutMainLoop()



def display(x=0, y=0):
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()


    glColor(0, .5, .7)
    glBegin(GL_QUADS)
    glVertex(-.8, .8, 0)
    glVertex(-.2, .7, 0)
    glVertex(-.15, -.6, 0)
    glVertex(-.7, -.45, 0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor(1, 0, 0)
    glVertex3f(0, .4, 0)
    glColor(0, 1, 0)
    glVertex3f(-.4, -.4, 0)
    glColor(0, 0, 1)
    glVertex3f(.4, -.4, 0)
    glEnd()

    glFlush()


if __name__ == '__main__': 
	main()







