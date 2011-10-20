'''This class tests the camera class.'''

__author__ = 'Stephen and Will'
__version__ = '1.0'

from camera import camera
import unittest


class test_camera(unittest.TestCase):
    def setUp(self):
        '''Create an instance of the camera object.'''
        self.my_camera = camera()

    def test_rotate(self):
        '''This function tests the rotate function. Currently, there is a slight error that accumulates in the negative y direction.'''
        self.my_camera.rotate(360)
        posx= self.my_camera.posx
        posy= self.my_camera.posy
        posz= self.my_camera.posz
        print 'from test'
        print posx, posy,posz 
        self.assertTrue(posx==0 and posy==0 and posz==3)
        
    def tearDown(self):
        '''No tear down.'''
        pass
        
if __name__ == '__main__':
    unittest.main()
