#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The file downloader
"""

import logging
import requests
from clint.textui import progress


LOGGER = logging.getLogger(__name__)

class Downloader():
    """The generic datasource model"""

    def __init__(self, url):
        """Initialize"""
        self.__url = url
        

    def download(self, path):
        """download"""

        try:
            f = open( path, 'wb' )

            r = requests.get(self.__url, stream=True)

            total_length = int(r.headers.get('content-length'))

            for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
                if chunk:
                    f.write(chunk)
                    f.flush()
                    
        except requests.ConnectionError as e:
            LOGGER.error('Error on opening connection to url %s for module UrlRepo-%s', self.jsondata['url'], self.__jsondata['name'])
        except IOError as e:
            LOGGER.error('Error on opening output file for module UrlRepo-%s', self.__jsondata['name'])
        finally:
            f.close()