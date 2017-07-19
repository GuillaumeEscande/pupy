#!/usr/bin/env python
# -*- Coding:utf-8 -*-

import unittest
import sys
import logging

from pupy import pupy


class TestPupy(unittest.TestCase):
    def test_command_update(self):
        sys.stdout = sys.__stdout__
        root = logging.getLogger()
        root.setLevel(logging.DEBUG)
        root.addHandler(logging.StreamHandler(sys.stdout))
        sys.argv = ["pupy.py", "-c", "conf/test_conf.json", "update"]
        pupy.main()

if __name__ == "__main__":
    unittest.main()
