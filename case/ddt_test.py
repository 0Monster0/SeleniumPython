# coding=utf-8

from re import S
import sys
sys.path.append("F:\\projects\\selenium")
from util.excel_util import ExcelUtil
from business.resgister_business import ResgisterBusiness
import unittest
from unittest.case import _Outcome
import os
from selenium import webdriver
import HTMLTestRunner
import ddt
data = ExcelUtil().get_data()

@ddt.ddt
class DDTTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("所有case执行之前")
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        print("所有case执行之后")
        return super().tearDownClass()

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("http://u.cyol.com/xiaomei/register")
        self.driver.maximize_window()
        self.pro_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print(self.pro_path)
        self.code_screenshot = os.path.join(self.pro_path, "screenshot", "screenshot.png")
        self.driver.save_screenshot(self.code_screenshot)
        self.rb = ResgisterBusiness(self.driver)
        return super().setUp()
    
    def tearDown(self) -> None:
        errors = self._outcome.errors
        for test, exc_info in errors:
            if exc_info:
                print(exc_info)
                screenshot_path = os.path.join("F:\\projects\\selenium\\screenshot", self._testMethodName + ".png")
                self.driver.save_screenshot(screenshot_path)
        self.driver.quit()
        return super().tearDown()

    # @ddt.data(
    #     ["test", "code", "test123", "test123@qq.com", "code_error", "验证码错误"],
    #     ["test", "code", "test123", "test123", "email_error", "请输入正确邮箱"],
    #     ["test", "code", "12345", "test123@qq.com", "psw_fist_error", "密码中必须包含大小写字母、数字、特殊字符确认密码"],
    #     ["test", "code", "test1234", "test123@qq.com", "psw_sec_error", "请输入大于或等于6位密码"]
    # )
    # @ddt.unpack
    @ddt.data(*data)
    def test_resgister_case(self, data):
        nickname, screenshot, psw, email, error, info_error = data
        res_info = self.rb.resgister_funtion(nickname, screenshot, psw, email, error, info_error)
        self.assertTrue(res_info)   
        

if __name__ == '__main__':
    # unittest.main()
    suit = unittest.TestLoader().loadTestsFromTestCase(DDTTest)
    report_path = os.path.join(os.getcwd(), "reports", "my_report.html")
    fp = open(report_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title='My unit test',
                description='This demonstrates the report output by HTMLTestRunner.'
                )
    runner.run(suit)
    fp.close()
    