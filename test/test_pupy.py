#!/usr/bin/env python
# -*- Coding:utf-8 -*-

import unittest
from pupy import pupy


class TestPupy(unittest.TestCase):
    def test_do_import(self):
        pupy.do_import(3)
        self.assertEqual(4, 4)

if __name__ == "__main__":
    unittest.main()
