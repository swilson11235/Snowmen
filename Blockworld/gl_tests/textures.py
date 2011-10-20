from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import Image
import sys

name = 'Example'
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400


class TextureExample:

    def __init__(self):
        self.xrot = 0
        self.yrot = 0
        self.zrot = 0

    def main(self):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        glutCreateWindow(name)

        glutKeyboardFunc(self.keyPressed)

        glutDisplayFunc(self.display)
        glutIdleFunc(self.display)

        glEnable(GL_TEXTURE_2D)
        glMatrixMode(GL_PROJECTION)
        gluPerspective(45., 1, .1, 100.)
        glMatrixMode(GL_MODELVIEW)
        
        glEnable(GL_DEPTH_TEST)

        self.loadTextures()

        glutMainLoop()


    def keyPressed(self, key, x, y):
        print "Pressed key: ", key
        if key == 'a':
            glRotate(3, 0, 1, 0)
        if key == 'd':
            glRotate(-3, 0, 1, 0)
        if key == 'w':
            glRotate(3, 1, 0, 0)
        if key == 's':
            glRotate(-3, 1, 0, 0)
        display()


    def loadTextures(self):
        image = Image.open("texture.bmp")
	
        ix = image.size[0]
        iy = image.size[1]
        image = image.tostring("raw", "RGBX", 0, -1)
	
        glPixelStorei(GL_UNPACK_ALIGNMENT,1)
        glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

        #glTranslate(0, 0, 1.7)


    def display(self, x=0, y=0):
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        glLoadIdentity()					# Reset The View
        glTranslatef(0.0,0.0,-4.0)			# Move Into The Screen

        glRotatef(self.xrot,1.0,0.0,0.0)			# Rotate The Cube On It's X Axis
        glRotatef(self.yrot,0.0,1.0,0.0)			# Rotate The Cube On It's Y Axis
        glRotatef(self.zrot,0.0,0.0,1.0)			# Rotate The Cube On It's Z Axis

        glBegin(GL_QUADS)			    # Start Drawing The Cube

        # Front Face (note that the texture's corners have to match the quad's corners)
        glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0,  1.0)	# Bottom Left Of The Texture and Quad
        glTexCoord2f(1.0, 0.0); glVertex3f( 1.0, -1.0,  1.0)	# Bottom Right Of The Texture and Quad
        glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0,  1.0)	# Top Right Of The Texture and Quad
        glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0,  1.0)	# Top Left Of The Texture and Quad

        # Back Face
        glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0, -1.0)	# Bottom Right Of The Texture and Quad
        glTexCoord2f(1.0, 1.0); glVertex3f(-1.0,  1.0, -1.0)	# Top Right Of The Texture and Quad
        glTexCoord2f(0.0, 1.0); glVertex3f( 1.0,  1.0, -1.0)	# Top Left Of The Texture and Quad
        glTexCoord2f(0.0, 0.0); glVertex3f( 1.0, -1.0, -1.0)	# Bottom Left Of The Texture and Quad

        # Top Face
        glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0, -1.0)	# Top Left Of The Texture and Quad
        glTexCoord2f(0.0, 0.0); glVertex3f(-1.0,  1.0,  1.0)	# Bottom Left Of The Texture and Quad
        glTexCoord2f(1.0, 0.0); glVertex3f( 1.0,  1.0,  1.0)	# Bottom Right Of The Texture and Quad
        glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0, -1.0)	# Top Right Of The Texture and Quad

        # Bottom Face       
        glTexCoord2f(1.0, 1.0); glVertex3f(-1.0, -1.0, -1.0)	# Top Right Of The Texture and Quad
        glTexCoord2f(0.0, 1.0); glVertex3f( 1.0, -1.0, -1.0)	# Top Left Of The Texture and Quad
        glTexCoord2f(0.0, 0.0); glVertex3f( 1.0, -1.0,  1.0)	# Bottom Left Of The Texture and Quad
        glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0,  1.0)	# Bottom Right Of The Texture and Quad

        # Right face
        glTexCoord2f(1.0, 0.0); glVertex3f( 1.0, -1.0, -1.0)	# Bottom Right Of The Texture and Quad
        glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0, -1.0)	# Top Right Of The Texture and Quad
        glTexCoord2f(0.0, 1.0); glVertex3f( 1.0,  1.0,  1.0)	# Top Left Of The Texture and Quad
        glTexCoord2f(0.0, 0.0); glVertex3f( 1.0, -1.0,  1.0)	# Bottom Left Of The Texture and Quad

        # Left Face
        glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0, -1.0)	# Bottom Left Of The Texture and Quad
        glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0,  1.0)	# Bottom Right Of The Texture and Quad
        glTexCoord2f(1.0, 1.0); glVertex3f(-1.0,  1.0,  1.0)	# Top Right Of The Texture and Quad
        glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0, -1.0)	# Top Left Of The Texture and Quad

        glEnd();				# Done Drawing The Cube

        glFlush()

        self.xrot = 30
        self.yrot += 0.01
        #self.zrot += 0.01


if __name__ == '__main__': 
    example = TextureExample()
    example.main()







