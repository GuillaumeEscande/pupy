#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The urlrepo datasource definitions for pupy data import
"""
import os
import logging

from slugify import slugify

from datasources import datasource
from lib import downloader


LOGGER = logging.getLogger(__name__)

class Url(datasource.DataSource):
    """The generic datasource model"""

    def __init__(self, jsondata):
        """Initialize"""
        super(Url, self).__init__(jsondata)
        
    def update(self, workspace):
        """update"""

        filename = slugify( self.jsondata['name'] )

        dwnlder = downloader.Downloader( self.jsondata['url'] )

        dwnlder.download(os.path.join(workspace,filename))


