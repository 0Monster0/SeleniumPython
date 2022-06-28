# coding=utf-8
import sys
sys.path.append("F:\\projects\\selenium")
from time import sleep
from selenium import webdriver
from base.find_element import FindElement

class ActionMethod(object):
    def open_browser(self, browser):
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Ie()

    def get_url(self, url):
        return self.driver.get(url)

    def get_element(self, key):
        find_ele = FindElement(self.driver)
        ele = find_ele.get_element(key)
        return ele

    def element_send_keys(self, key, value):
        ele = self.get_element(key)
        ele.send_keys(value)

    def get_title(self):
        return self.driver.title

    def get_element_text(self, key):
        return self.get_element(key).text

    def element_click(self, key):
        self.get_element(key).click()

    def sleep_time(self):
        sleep(2)

    def close(self):
        self.driver.close()


if __name__ == '__main__':
    pass
    