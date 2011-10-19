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

    #glLoadIdentity()
    #glScale(1., 1.5, 0.5)
    glTranslate(.01, 0, 0)
    #glRotate(135, 0, 0, 1)

    glBegin(GL_TRIANGLES)
    glVertex3f(0, 1, 0)
    glVertex3f(-1, -1, 0)
    glVertex3f(1, -1, 0)
    glEnd()

    glFlush()


if __name__ == '__main__': 
	main()







