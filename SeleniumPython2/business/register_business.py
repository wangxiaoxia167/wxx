#coding=utf-8
import sys
sys.path.append('C:/Users/xx/Desktop/SeleniumPython2')
from selenium import webdriver
import random
from handle.register_handle import RegisterHandle
from PIL import Image
from util.ShowapiRequest import ShowapiRequest
import unittest
class RegisterBusiness(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.5itest.cn/register?goto=/")
        self.driver.maximize_window()
        self.register_handle = RegisterHandle(self.driver)

    def tearDown(self) -> None:
        self.driver.close()

    #获取验证码图片并保存到本地
    def get_code_image(self):
        self.driver.save_screenshot("C:/Users/xx/Desktop/SeleniumPython/register/test01.png")
        code_element = self.driver.find_element_by_id("getcode_num")
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width'] + left
        height = code_element.size['height'] + top
        im = Image.open("C:/Users/xx/Desktop/SeleniumPython/register/test01.png")
        box = [left, top, right, height]
        region = im.crop(box)
        region.save("C:/Users/xx/Desktop/SeleniumPython/register/test01.png")

    #解码
    def code_online(self):
        r = ShowapiRequest("http://route.showapi.com/184-4", "103444", "b8112ed5fc234f488fad6ef1d0c90ee1")
        # r.addBodyPara("img_base64", "")
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addBodyPara("needMorePrecise", "0")
        r.addFilePara("image", "C:/Users/xx/Desktop/SeleniumPython/register/test01.png")
        res = r.post()
        text = res.json()['showapi_res_body']['Result']
        return text

    # 随机生成用户名
    def get_range_user(self):
        user_email = ''.join(random.sample('1234567890abcdefghijklmnopqrstuvwxyz', 8))
        return user_email

    def test_register(self):
        nickname = self.get_range_user()
        email = nickname+'@qq.com'
        psd = '111111'
        self.register_handle.send_user_email(email)
        self.register_handle.send_user_name(nickname)
        self.register_handle.send_user_password(psd)
        self.get_code_image()
        text = self.code_online()
        self.register_handle.send_user_code(text)
        self.register_handle.click_register()

if __name__ == '__main__':
    '''
    #非容器的方式调用
    unittest.main()
    '''
    #容器
    suite = unittest.TestSuite()
    suite.addTest(RegisterBusiness('test_register'))
    unittest.TextTestRunner().run(suite)
