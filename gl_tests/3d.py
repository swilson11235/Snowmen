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

    glRotate(25, 1, 1, 1)

    glutWireSphere(.5, 40, 40)

    #glutSolidCube(.4)

    glFlush()


if __name__ == '__main__': 
	main()







