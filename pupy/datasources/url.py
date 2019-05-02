#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The urlrepo datasource definitions for pupy data import
"""
import os
import logging

from slugify import slugify

from pupy.datasources import datasource
from pupy.lib import downloader


LOGGER = logging.getLogger(__name__)

class Url(datasource.DataSource):
    """The generic datasource model"""

    def __init__(self, jsondata):
        """Initialize"""
        super(Url, self).__init__(jsondata)
        
    def update(self, config, args, workspace):
        """update"""

        path = slugify( self.jsondata['name'] )
        if "path" in self.jsondata:
            path = self.jsondata['path']
        filepath = os.path.join(workspace,path)
        working_dir = os.path.dirname(filepath)

        if not os.path.exists(working_dir):
            os.makedirs(working_dir)

        sha = None
        checksum_type = None
        if "sha256" in self.jsondata:
            sha = self.jsondata["sha256"]
            checksum_type = "sha256"

        dwnlder = downloader.Downloader( self.jsondata['url'], args.proxy )

        dwnlder.download(filepath, sha, checksum_type)


