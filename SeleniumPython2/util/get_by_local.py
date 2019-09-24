#coding=utf-8
#2:根据id或者className划分获取的元素
import sys
sys.path.append('C:/Users/xx/Desktop/SeleniumPython2')
from util.read_ini import ReadIni
#导入driver

__author__='wangxiaoxia'

class GetByLocal:
    def __init__(self,driver):
        self.driver = driver

    def get_element(self,section,key):
        read_ini = ReadIni('C:/Users/xx/Desktop/SeleniumPython2/config/LocalElement.ini')
        #id>com.msjt.sigma:id/id_name
        local = read_ini.get_value(section,key)
        by = local.split('>')[0]
        local_by = local.split('>')[1]
        if by == 'ids':
            return self.driver.find_elements_by_id(local_by)
        elif by =='id':
            return self.driver.find_element_by_id(local_by)
        elif by == 'className':
            return self.driver.find_element_by_class_name(local_by)
        else:
            return self.driver.find_element_by_xpath(local_by)