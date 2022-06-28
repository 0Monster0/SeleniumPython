# coding=utf-8
import sys
from time import sleep
sys.path.append("F:\\projects\\selenium")

from util.get_code import GetCode
from page.resgister_page import ResgisterPage
from selenium.webdriver.common.keys import Keys


class ResgisterHandler(object):
    def __init__(self, driver) -> None:
        self.resgister_p = ResgisterPage(driver)
        self.code = GetCode(driver)

    # 输入邮箱
    def send_user_email(self, email):
        self.resgister_p.get_email_element().send_keys(email)
        sleep(2)
        self.resgister_p.get_email_element().send_keys(Keys.ENTER)

    # 输入昵称
    def send_user_nickname(self, nickname):
        self.resgister_p.get_nickname_element().send_keys(nickname)
    
    # 第一次输入密码
    def send_user_first_psw(self, psw):
        self.resgister_p.get_first_psw_element().send_keys(psw)

    # 第二次输入密码
    def send_user_sec_psw(self, psw):
        self.resgister_p.get_sec_psw_element().send_keys(psw)

    # 输入验证码
    def send_user_code(self, code):
        #　code = self.code.code_recognition(screenshot)
        self.resgister_p.get_code_element().send_keys(code)

    # 获取用户文本
    def get_user_text(self, info, user_info):
        if info == "email_error":
            text = self.resgister_p.get_email_error_element().text
        elif info == "psw_first_error":
            text = self.resgister_p.get_psw_first_error_element().text
        elif info == "psw_sec_error":
            text = self.resgister_p.get_psw_sec_error_element().text
        else:
            text = self.resgister_p.get_code_error_element().text
        return (text == user_info)

    def click_resgister_btn(self):
        self.resgister_p.get_reg_btn_element().click()