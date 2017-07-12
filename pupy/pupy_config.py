#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The pupy configuration module
"""


import json

from datasources.datasource import Datasource

class PupyConfig( object ):
    """A config for pupy"""

    def __init__( self, json_data ):
        """Initialize"""
        self.json_data = json_data
        self.__datasources = None

    @staticmethod
    def load( json_path ):
        """Load a pupy contained in a JSON file"""
        with open( json_path, 'r' ) as fson_fp:
            return PupyConfig( json.load( fson_fp ) )


    @property
    def datasources( self ):
        """
        Return une list of Datasource
        :rtype: list(datasource.datasource.Datasource)
        """
        if self.__datasources is None:
            datas = datasource.datasource.Datasource("TEST")
            self.__datasources.append(datas)

        return self.__datasources