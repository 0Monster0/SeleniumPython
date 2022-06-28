# coding=utf-8

from cProfile import run
import unittest
import os
import HtmlTestRunner

class RunCase(unittest.TestCase):
    def test_case(self):
        case_path = os.path.join(os.getcwd(), "case")
        suit = unittest.defaultTestLoader.discover(case_path, "unittest_*.py")
        # unittest.TextTestRunner().run(suit)

if __name__ == '__main__':
   unittest.main()
    