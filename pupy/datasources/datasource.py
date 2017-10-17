#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The datasource definitions for pupy data import
"""


class DataSource(object):
    """The generic datasource model"""

    def __init__(self, jsondata):
        """Initialize"""
        self.jsondata = jsondata

    def update(self, workspace):
        """update"""
        raise NotImplementedError()

    @property
    def name(self):
        """Return the name"""
        return self.jsondata['name']


    

    @staticmethod
    def load( json_datasource ):
        
        from datasources import rhrepo
        from datasources import url
        from datasources import copy

        if json_datasource['type'] == 'rhrepo':
            return rhrepo.RhRepo( json_datasource )
        elif json_datasource['type'] == 'url':
            return url.Url( json_datasource )
        elif json_datasource['type'] == 'copy':
            return copy.Copy( json_datasource )
        else :
            return None
