#!/usr/bin/env python
# -*- coding: utf-8 -*-

import distutils

"""
The datasource definitions for pupy data import
"""

class DataSource(object):
    """The generic datasource model"""

    def __init__(self, jsondata):
        """Initialize"""
        self.jsondata = jsondata

    def update(self, config, args, workspace):
        """update"""
        raise NotImplementedError()

    @property
    def name(self):
        """Return the name"""
        return self.jsondata['name']

    @property
    def enable(self):
        """Return the enable"""
        enable = True
        if 'enable' in self.jsondata :
          enable = distutils.util.strtobool(self.jsondata['enable'])
        return enable


    

    @staticmethod
    def load( json_datasource ):
        
        from pupy.datasources import rhrepo
        from pupy.datasources import url
        from pupy.datasources import copy

        if json_datasource['type'] == 'rhrepo':
            return rhrepo.RhRepo( json_datasource )
        elif json_datasource['type'] == 'url':
            return url.Url( json_datasource )
        elif json_datasource['type'] == 'copy':
            return copy.Copy( json_datasource )
        else :
            return DataSource(json_datasource)
