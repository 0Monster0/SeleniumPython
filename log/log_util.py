# coding=utf-8

from cmath import log
from datetime import datetime
import logging
import os

class LogUtil(object):
    def __init__(self) -> None:
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter("%(asctime)s %(filename)s --> %(funcName)s %(lineno)d: %(levelname)s --> %(message)s")

    def get_logger(self):
        # self.logger.addHandler(self.get_consle_handler())
        self.logger.addHandler(self.get_file_handler())
        return self.logger

    def get_file_handler(self):
        # 文件输出日志
        file_handle = logging.FileHandler(self.get_logname(), "a", encoding="utf-8")
        file_handle.setLevel(logging.INFO)
        file_handle.setFormatter(self.formatter)
        return file_handle

    def get_consle_handler(self):
        # 控制台输出日志
        consle_handler= logging.StreamHandler()
        consle_handler.setFormatter(self.formatter)
        return consle_handler

    def get_logname(self):
        # 获取文件名
        basa_dir = os.path.dirname(os.path.abspath(__file__))
        logs_dir = os.path.join(basa_dir, "logs")
        log_file = datetime.now().strftime("%Y-%m-%d.log")
        return os.path.join(logs_dir, log_file)

    def close(self):
        self.logger.removeHandler(self.get_file_handler())
        self.get_file_handler().close()

if __name__ == '__main__':
    log = LogUtil()
    logger = log.get_logger()
    logger.debug("123456")
    
        
    










