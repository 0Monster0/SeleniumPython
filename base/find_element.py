# coding=utf-8
import sys
sys.path.append("F:\\projects\\selenium")
from time import sleep
from util.read_ini import ReadIni
from selenium.webdriver.common.by import By
from selenium import webdriver

class FindElement(object):
    def __init__(self, driver) -> None:
        self.driver = driver

    def get_element(self, key):
        ri = ReadIni()
        data = ri.get_value(key)
        by_value = data.split(":")[0]
        value = data.split(":")[1]
        try:
            if by_value == "id":
                return self.driver.find_element(By.ID, value)
            elif by_value == "name":
                return self.driver.find_element(By.NAME, value)
            elif by_value == "className":
                return self.driver.find_element(By.CLASS_NAME, value)
            elif by_value == "xpath":
                return self.driver.find_element(By.XPATH, value)
            else:
                return False
        except:
            return None


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://u.cyol.com/xiaomei/register")

    fe = FindElement(driver)
    fe.get_element("user_email").send_keys("test")
    text = driver.find_element(By.ID, "email").get_attribute("value")
    print("text: ", text)
    sleep(4)
    driver.quit()
    