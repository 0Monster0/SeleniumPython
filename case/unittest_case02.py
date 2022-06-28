# coding=utf-8

import unittest
import HtmlTestRunner
import os

class UnitTest(unittest.TestCase):
    def setUp(self) -> None:
        print("333")
        return super().setUp()

    def test_seven(self):
        print("test7")

    def test_six(self):
        print("test6")

    def test_five(self):
        print("test5")

    def tearDown(self) -> None:
        print("444")
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()
    suit = unittest.TestSuite()
    suit.addTest(UnitTest("test_sec"))
    # unittest.TextTestRunner().run(suit)

    