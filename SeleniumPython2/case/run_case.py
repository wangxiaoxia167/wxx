#coding=utf-8
import unittest
import os
import warnings
class RunCase(unittest.TestCase):
    def testcase01(self):
        warnings.simplefilter('ignore', ResourceWarning)
        #case_path = 'C:/Users/xx/Desktop/SeleniumPython2/case'
        case_path = os.path.join(os.getcwd(),'')
        suite = unittest.defaultTestLoader.discover(case_path,'unittest_case*.py')
        unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    unittest.main()