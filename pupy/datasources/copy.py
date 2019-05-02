#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The rhrepo datasource definitions for pupy data import
"""

import logging
import os

from slugify import slugify

from pupy.datasources import datasource
from shutil import copyfile, copy2


LOGGER = logging.getLogger(__name__)

class Copy(datasource.DataSource):
    """The generic datasource model"""

    def __init__(self, jsondata):
        """Initialize"""
        super(Copy, self).__init__(jsondata)
        

    def update(self, config, args, workspace):
        """update"""

        path = slugify( self.jsondata['name'] )
        if "path" in self.jsondata:
            path = self.jsondata['path']
        working_dir = os.path.join(workspace,path)

        if os.path.isfile( self.jsondata['src'] ) :
            path = os.path.join(os.path.basename(self.jsondata['src']))
            copyfile(self.jsondata['src'], path)

        elif os.path.isdir( self.jsondata['src'] ) :
            copy2(self.jsondata['src'], path)

        else:
            LOGGER.error('Source path %s do not exist', self.jsondata['src'])
