# coding=utf-8
import sys
sys.path.append("F:\\projects\\selenium")
from base.find_element import FindElement


class ResgisterPage(object):
    def __init__(self, driver):
        self.fe = FindElement(driver)

    def get_email_element(self):
        print("email ele: ", self.fe.get_element("user_email"))
        return self.fe.get_element("user_email")

    def get_email_error_element(self):
        return self.fe.get_element("email_error")

    def get_nickname_element(self):
        return self.fe.get_element("user_nickname")

    def get_first_psw_element(self):
        return self.fe.get_element("user_psw_first")

    def get_sec_psw_element(self):
        return self.fe.get_element("user_psw_sec")

    def get_psw_first_error_element(self):
        return self.fe.get_element("psw_first_error")
    
    def get_psw_sec_error_element(self):
        return self.fe.get_element("psw_sec_error")

    def get_code_element(self):
        return self.fe.get_element("user_code")
    
    def get_code_error_element(self):
        return self.fe.get_element("code_error")

    def get_reg_btn_element(self):
        return self.fe.get_element("reg_btn")