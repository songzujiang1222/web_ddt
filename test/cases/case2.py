
import unittest
from selenium import webdriver
from po.loginPage import LoginPage
import common.util as Util 
import os
import time

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
    
    def setUp(self):
        driver = self.driver
        driver.get('http://39.107.96.138:3000/signin')

    def tearDown(self):
        self.driver.delete_all_cookies()
        name = __name__
        screenShotFile = os.path.join(Util.getScreenShotsPath(),name+'.png')
        
        self.driver.save_screenshot(screenShotFile)
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_1success(self):
        driver = self.driver
        lg = LoginPage(driver)

        lg.input_username('user1')
        lg.input_password('123456')
        lg.click_login_btn()
        text = lg.get_login_result(True)

        self.assertEqual(text,'user1','用户名验证错误')

    def test_login_2fail(self):
        driver = self.driver
        lg = LoginPage(driver)

        lg.input_username('1223user1')
        lg.input_password('123456')
        lg.click_login_btn()
        text = lg.get_login_result(False)

        self.assertEqual(text,'用户名或密码错误','错误提示信息验证错误')
