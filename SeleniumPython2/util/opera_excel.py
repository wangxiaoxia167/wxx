#coding=utf-8
import sys
sys.path.append("C:\\Users\\xx\\Desktop\\SeleniumPython2")
import xlrd
from xlutils.copy import copy
class OperaExcel:
	def __init__(self,file_path,i):
		self.file_path = file_path
		self.i = i
		self.excel = self.get_excel()
		self.data = self.get_sheets(self.i)
			
	def get_excel(self):
		excel = xlrd.open_workbook(self.file_path)
		return excel

	def get_sheets(self,i):
		tables = self.excel.sheets()[i]
		return tables

	def get_lines(self):
		lines = self.data.nrows
		return lines

	def get_cell(self,row,cell):
		data = self.data.cell_value(row,cell)
		return data

	def write_value(self,row,value):
		read_value = xlrd.open_workbook(self.file_path)
		write_data = copy(read_value)
		write_save = write_data.get_sheet(self.i)
		write_save.write(row,9,value)
		write_data.save(self.file_path)

if __name__ == '__main__':
	opera = OperaExcel('../config/keyword.xls',0)
	#print(opera.get_excel())
	#print(opera.get_sheets(0))
	#print(opera.get_cell(4,5))
	#print(opera.get_lines())
	print(opera.get_cell(2,6))