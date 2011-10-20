'''This class tests the block class.'''

__author__ = 'Stephen and Will'
__version__ = '1.0'

from block import block
import unittest


class test_block(unittest.TestCase):
    def setUp(self):
        '''Create an instance of the block object.'''
        self.my_block = block()

    def test_(self):
        '''This function tests '''
        pass
    def tearDown(self):
        '''No tear down.'''
        pass
        
if __name__ == '__main__':
    unittest.main()
