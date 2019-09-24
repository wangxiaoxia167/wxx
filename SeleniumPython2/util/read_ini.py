#coding=utf-8
#1:读取元素
import sys
sys.path.append('C:/Users/xx/Desktop/SeleniumPython2')
import configparser

__author__='wangxiaoxia'

class ReadIni:
	#全局变量初始化,构造函数
	def __init__(self,file_name):
		self.file_name = file_name
		self.data = self.read_ini()

	def read_ini(self):
		read_ini = configparser.ConfigParser()
		read_ini.read(self.file_name)
		return read_ini

	#定义函数
	def get_value(self,section,key):
		self.key = key
		self.section =section
		try:
			value = self.data.get(self.section,self.key)
		except Exception:
			value = None
		return value

if __name__ == '__main__':
	ReadIni = ReadIni( 'C:/Users/xx/Desktop/SeleniumPython2/config/LocalElement.ini')
	print(ReadIni.get_value('Register','captcha_code-error'))