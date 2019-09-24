#coding=utf-8
import sys
sys.path.append('C:/Users/xx/Desktop/SeleniumPython2')
from page.register_page import RegisterPage
import time
class RegisterHandle:
    def __init__(self,driver):
        self.register_page = RegisterPage(driver)
    #输入邮箱
    def send_user_email(self,email):
        self.register_page.get_user_email_element().send_keys(email)
        time.sleep(5)
    #输入用户名
    def send_user_name(self,nickname):
        self.register_page.get_user_name_element().send_keys(nickname)
        time.sleep(5)
    #输入密码
    def send_user_password(self,psd):
        self.register_page.get_user_password_element().send_keys(psd)
        time.sleep(5)
    #输入验证码
    def send_user_code(self,code):
        self.register_page.get_user_code_element().send_keys(code)
        time.sleep(5)
    #点击登录
    def click_register(self):
        self.register_page.get_register_btn_element().click()
