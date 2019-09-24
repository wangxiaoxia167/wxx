#coding=utf-8
import sys
sys.path.append('C:/Users/xx/Desktop/SeleniumPython2')
from selenium import webdriver
from util.get_by_local import GetByLocal
import time
class actionMethod:
    def __init__(self):
        pass

    #打开浏览器
    def open_browser(self,browser):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Edge()

    #输入地址
    def get_url(self,url):
        self.driver.get(url)
        self.driver.maximize_window()

    #定位元素
    def get_element(self,key,*args):
        find_element = GetByLocal(self.driver)
        try:
            element = find_element.get_element('Register',key)
        except Exception:
            element = 'error'
        return element

    #输入元素
    def element_send_keys(self,key,value):
        element = self.get_element(key)
        element.send_keys(value)

    #点击元素
    def click_element(self,key):
        self.get_element('Register',key).click()

    #等待
    def sleep_time(self,*args):
        time.sleep(5)

    #关闭浏览器
    def close_browser(self,*args):
        self.driver.close()

    #获取title
    def get_title(self,*args):
        return self.driver.title

if __name__ =='__main__':
    action_method = actionMethod()
    action_method.open_browser('chrome')
    print(action_method.get_element('register_password'))