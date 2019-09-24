#coding=utf-8
import sys
sys.path.append('C:/Users/xx/Desktop/SeleniumPython2')
from util.get_by_local import GetByLocal
class RegisterPage:
    def __init__(self,driver):
        self.get_by_local = GetByLocal(driver)

    def get_user_email_element(self):
        return self.get_by_local.get_element('Register','email')

    def get_user_name_element(self):
        return self.get_by_local.get_element('Register','nickname')

    def get_user_password_element(self):
        return self.get_by_local.get_element('Register','password')

    def get_user_code_element(self):
        return self.get_by_local.get_element('Register','code')

    def get_register_btn_element(self):
        return self.get_by_local.get_element('Register', 'register')