# coding=utf-8
import sys
sys.path.append("F:\\projects\\selenium")
from time import sleep
from handler.resgister_handler import ResgisterHandler


class ResgisterBusiness(object):
    def __init__(self, driver) -> None:
        self.register_h = ResgisterHandler(driver)

    def user_base(self, nickname, screenshot, psw, email):
        self.register_h.send_user_nickname(nickname)
        self.register_h.send_user_code(screenshot)
        self.register_h.send_user_first_psw(psw)
        self.register_h.send_user_sec_psw(psw)
        self.register_h.send_user_email(email)
        # self.register_h.click_resgister_btn()
        sleep(3)
    
    def register_success(self):
        pass
    
    # 验证码错误
    def login_code_error(self, nickname, screenshot, psw, email):
        self.user_base(nickname, screenshot, psw, email)
        if self.register_h.get_user_text("code_error", "验证码错误"):
            print("验证码错误校验成功")
            return True
        else:
            print("验证码错误校验失败")
            return False

    # 邮箱错误
    def login_email_error(self, nickname, screenshot, psw, email):
        self.user_base(nickname, screenshot, psw, email)
        if self.register_h.get_user_text("email_error", "请输入正确邮箱"):
            print("邮箱校验错误成功")
            return True
        else:
            print("邮箱校验错误失败")
            return False
    
    # 第一次密码错误
    def login_psw_fist_error(self, nickname, screenshot, psw, email):
        self.user_base(nickname, screenshot, psw, email)
        if self.register_h.get_user_text("psw_fist_error", "密码中必须包含大小写字母、数字、特殊字符确认密码"):
            print("第一次密码错误校验成功")
            return True
        else:
            print("第一次密码错误校验失败")
            return False

    # 第二次密码错误
    def login_psw_sec_error(self, nickname, screenshot, psw, email):
        self.user_base(nickname, screenshot, psw, email)
        if self.register_h.get_user_text("psw_sec_error", "请输入大于或等于6位密码"):
            print("第二次密码错误校验成功")
            return True
        else:
            print("第二次密码错误校验失败")
            return False

    def resgister_funtion(self, nickname, screenshot, psw, email, assertCode, assertText):
        self.user_base(nickname, screenshot, psw, email)
        if self.register_h.get_user_text(assertCode, assertText):
            print(assertCode + "校验成功")
            return True
        else:
            print(assertCode + "校验成功")
            return False