from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys

name = 'Example'
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400



def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutCreateWindow(name)

    light_diffuse = (1, 1, 1, 1)
    light_position = (.5, 1, -.5, 1)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    light_ambient = (.35, .35, .35, 1)
    light_position = (0, 0, 1, 0)
    glLightfv(GL_LIGHT1, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT1, GL_POSITION, light_position)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)

    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutMainLoop()



def display(x=0, y=0):
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()

    #glRotate(50, 1, 1, 1)
    glMaterial(GL_FRONT, GL_AMBIENT, (0, .6, .2));
    glutSolidSphere(.6, 40, 40)

    glFlush()


if __name__ == '__main__': 
	main()







