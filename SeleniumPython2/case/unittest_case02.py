#coding=utf-8
import sys
sys.path.append('C:/Users/xx/Desktop/SeleniumPython2')
import unittest
import os
import HTMLTestRunner
class FirstCase01(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('This is setUpClass\n')

    @classmethod
    def tearDownClass(cls) -> None:
        print('This is tearDownClass')

    def setUp(self) -> None:
        print('方法执行之前的语句')

    def tearDown(self) -> None:
        print('方法执行之后的语句')

    def test_first01(self):
        print('This is first case')

    #@unittest.skip('test02')
    def test_first02(self):
        print('This is second case')

if __name__ == '__main__':
    #unittest.main()
    filepath = os.path.join(os.getcwd(),'')+'/report/'+'report1.html'
    fp = open(filepath, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(FirstCase01('test_first01'))
    suite.addTest(FirstCase01('test_first02'))
    #unittest.TextTestRunner().run(suite)
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='this is first report')
    runner.run(suite)