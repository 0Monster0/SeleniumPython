# coding=utf-8
from posixpath import dirname
import sys
sys.path.append("F:\\projects\\selenium")
from log.log_util import LogUtil

import unittest
from unittest.case import _Outcome
import os
from business.resgister_business import ResgisterBusiness
from selenium import webdriver
import HTMLTestRunner

class ResgisterCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.log = LogUtil()
        cls.logger = cls.log.get_logger()
        print("所有case执行之前")
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.log.close()
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

    def test_resgister_sucsess(self):
        pass

    def test_email_resgister_error(self):
        self.assertTrue(self.rb.login_email_error("123", self.code_screenshot, "234123", "adsfgasdfa"), u"验证邮箱错误成功")

    def test_code_resgister_error(self):
        self.assertTrue(self.rb.login_code_error("123", self.code_screenshot, "234123", "sdfadfa"), u"验证验证码错误成功")

    def test_psw_first_resgister_error(self):
        self.assertTrue(self.rb.login_psw_fist_error("123", self.code_screenshot, "234123", "sdfadfa"), u"验证第一次密码错误成功")

    def test_psw_sec_resgister_error(self):
        self.assertTrue(self.rb.login_psw_sec_error("123", self.code_screenshot, "234123", "sdfadfa"), u"验证第二次密码错误成功")


if __name__ == '__main__':
    #　unittest.main()
    suit = unittest.TestLoader().loadTestsFromTestCase(ResgisterCase)
    report_path = os.path.join(os.getcwd(), "reports", "my_report.html")
    fp = open(report_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title='My unit test',
                description='This demonstrates the report output by HTMLTestRunner.'
                )
    runner.run(suit)
    fp.close()