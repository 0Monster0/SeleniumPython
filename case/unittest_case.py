# coding=utf-8

import unittest
import os
import HtmlTestRunner

class UnitTest(unittest.TestCase):
    def setUp(self) -> None:
        print("111")
        return super().setUp()

    def test_third(self):
        print("test3")

    @unittest.skip("666")
    def test_first(self):
        print("test1")

    def test_sec(self):
        print("test2")

    def test_four(self):
        print("test4")

    def tearDown(self) -> None:
        print("222")
        return super().tearDown()

if __name__ == '__main__':
    # unittest.main()
    suit = unittest.TestSuite()
    suit.addTest(UnitTest("test_sec"))
    suit.addTest(UnitTest("test_four"))
    # unittest.TextTestRunner().run(suit)
    report_path = os.path.join(os.getcwd(), "reports", "report.log")
    f = open(report_path, "w")
    runner = HtmlTestRunner.HTMLTestRunner(stream=f, descriptions="my test report", report_title="Test Report")
    runner.run(suit)

    