#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The datasource definitions for pupy data import
"""

class Datasource(object):
    """The generic datasource model"""

    def __init__(sefl, name):
        """Initialize"""
        self.__name = name

    @property
    def name(self):
        """Return the name"""
        return self.__name