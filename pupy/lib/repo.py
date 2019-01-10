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

from pypac import PACSession, get_pac

from xml.dom.minidom import parseString

from lib import downloader

LOGGER = logging.getLogger(__name__)

class Repo():
    """The generic datasource model"""

    def __init__(self, url, proxy):
        """Initialize"""
        self.__url = url
        self.__proxy = proxy
        

    def reposync(self, path):
        """reposync"""

        package_dir = os.path.join(path,"Packages")
        if not os.path.exists(package_dir):
            os.makedirs(package_dir)
        repodata_dir = os.path.join(path,"repodata")
        if not os.path.exists(repodata_dir):
            os.makedirs(repodata_dir)

        # Download repo repomd file
        repomd_dwn = downloader.Downloader( self.__url + "repodata/repomd.xml", self.__proxy )
        repomd_dwn.download(os.path.join(repodata_dir,"repomd.xml"))

        repomd = repomd_dwn.download()
        repomd_root = parseString(repomd)

        for child in repomd_root.getElementsByTagName('data'):
            # Download all files
            file_url = child.getElementsByTagName("location")[0].getAttribute('href')
            checksum_node = child.getElementsByTagName("checksum")[0]
            checksum = checksum_node.firstChild.nodeValue
            checksum_type = checksum_node.getAttribute('type')
            file_dwn = downloader.Downloader( self.__url + file_url, self.__proxy )
            file_dwn.download(os.path.join(path,file_url), checksum, checksum_type)

            if child.getAttribute('type') == "primary":
                primary_url = file_url

        print(self.__url + primary_url)
        # primary
        primary_gz_dwn = downloader.Downloader( self.__url + primary_url, self.__proxy )
        primary_gz = primary_gz_dwn.download()
        primary = zlib.decompress(primary_gz, zlib.MAX_WBITS|32)
        primary_root = parseString(primary)
        
        for child in primary_root.getElementsByTagName('package'):
            location = child.getElementsByTagName("location")[0].getAttribute('href')
            filename = location.rsplit('/', 1)[-1]
            checksum_node = child.getElementsByTagName("checksum")[0]
            checksum = checksum_node.firstChild.nodeValue
            checksum_type = checksum_node.getAttribute('type')
			
            dwnlder = downloader.Downloader( self.__url + location, self.__proxy )
            dwnlder.download(os.path.join(package_dir,filename), checksum, checksum_type)