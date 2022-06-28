# coding=utf-8

import configparser
from platform import node

class ReadIni(object):
    def __init__(self, file_name=None, node=None) -> None:
        if file_name is None:
            file_name = "F:\\projects\\selenium\\ini\\LocalElement.ini"
        if node is None:
            self.node = "ResgisterElement"
        else:
            self.node = node
        self.conf = self.load_ini(file_name)
        
    def load_ini(self, file_name):
        conf = configparser.ConfigParser()
        conf.read(file_name)
        return conf

    def get_value(self, key):
        data = self.conf.get(self.node, key)
        return data
    

if __name__ == '__main__':
    r = ReadIni()
    print(r.get_value("user_nickname"))