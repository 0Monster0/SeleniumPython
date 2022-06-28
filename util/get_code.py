# coding=utf-8

import sys
sys.path.append("F:\\projects\\selenium")
import time
import os
import pytesseract
from PIL import Image
from selenium import webdriver

from page.resgister_page import ResgisterPage

class GetCode(object):
    def __init__(self, driver) -> None:
        self.resgister_p = ResgisterPage(driver)

    def get_code_image(self, screenshot):
        code_ele = self.resgister_p.get_code_element()
        x = code_ele.location["x"]  + 245
        y = code_ele.location["y"] + 3
        width = code_ele.size["width"] + x - 120
        height = code_ele.size["height"] + y - 10
        ss_image = Image.open(screenshot)
        code_img = ss_image.crop((x, y, width, height))
        code_img.save("code.png")
        return code_img

    def code_recognition(self, screenshot):
        text = pytesseract.image_to_string(self.get_code_image(screenshot))
        time.sleep(3)
        return text


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://u.cyol.com/xiaomei/register")
    driver.maximize_window()
    pro_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    code_screenshot = os.path.join(pro_path, "screenshot", "code.png")
    print(code_screenshot)
    driver.save_screenshot(code_screenshot)
    gc = GetCode(driver)
    code_img = gc.get_code_image(code_screenshot)
    text = gc.code_recognition(code_img)
    time.sleep(2)
    driver.quit()

    