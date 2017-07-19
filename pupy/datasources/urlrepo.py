#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The urlrepo datasource definitions for pupy data import
"""
import os
import requests
import logging
import wget

from clint.textui import progress

from pupy.datasources import datasource
from slugify import slugify


LOGGER = logging.getLogger(__name__)

class UrlRepo(datasource.DataSource):
    """The generic datasource model"""

    def __init__(self, jsondata):
        """Initialize"""
        super(UrlRepo, self).__init__(jsondata)
        
    def update(self, workspace):
        """update"""
        attempts = 0


        filename = slugify( self.jsondata['name'] )

        try:
            f = open( os.path.join(workspace,filename), 'wb' )

            r = requests.get(self.jsondata['url'], stream=True)

            total_length = int(r.headers.get('content-length'))

            for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
                if chunk:
                    f.write(chunk)
                    f.flush()


        except ConnectionError as e:
            LOGGER.error('Error on opening connection to url %s for module UrlRepo-%s', self.jsondata['url'], self.__jsondata['name'])
        except IOError as e:
            LOGGER.error('Error on opening output file for module UrlRepo-%s', self.__jsondata['name'])
        finally:
            f.close()


