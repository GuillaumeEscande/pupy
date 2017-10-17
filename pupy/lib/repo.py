#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The RH repo downloader
"""

import os
import logging
import requests
import zlib
from clint.textui import progress

from xml.dom.minidom import parseString

from lib import downloader

LOGGER = logging.getLogger(__name__)

class Repo():
    """The generic datasource model"""

    def __init__(self, url):
        """Initialize"""
        self.__url = url
        

    def reposync(self, path):
        """reposync"""

        working_dir = os.path.join(path,"Packages")
        if not os.path.exists(working_dir):
            os.makedirs(working_dir)

        # repomd
        repomd = requests.get( self.__url + "repodata/repomd.xml" )
        repomd_root = parseString(repomd.content)

        for child in repomd_root.getElementsByTagName('data'):
            if child.getAttribute('type') == "primary":
                primary_url = child.getElementsByTagName("location")[0].getAttribute('href')

                
        # primary
        primary_gz = requests.get( self.__url + primary_url )
        primary = zlib.decompress(primary_gz.content, zlib.MAX_WBITS|32)
        primary_root = parseString(primary)
        
        for child in primary_root.getElementsByTagName('package'):
            location = child.getElementsByTagName("location")[0].getAttribute('href')
            filename = location.rsplit('/', 1)[-1]

            dwnlder = downloader.Downloader( self.__url + location )
            dwnlder.download(os.path.join(working_dir,filename))