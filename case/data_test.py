# coding=utf-8

import ddt
import unittest


@ddt.ddt
class DateTest(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    @ddt.data(
        [1, 2],
        [2, 8],
        [7, 7]
    )
    @ddt.unpack
    def test_add(self, x, y):
        print(x + y)

if __name__ == '__main__':
    unittest.main()  
    