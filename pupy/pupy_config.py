#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The pupy configuration module
"""


import json

from pupy.datasources.datasource import DataSource

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
        Return list of Datasource
        :rtype: list(datasource.datasource.Datasource)
        """
        if self.__datasources is None:
            self.__datasources = []
            for ds in self.json_data["datasources"]:
                self.__datasources.append( DataSource.load( ds ) )            

        return self.__datasources

    @property
    def workspace( self ):
        """
        Return workspace string
        """
        return self.json_data["workspace"] 

    @property
    def name( self ):
        """
        Return name string
        """
        return self.json_data["name"] 