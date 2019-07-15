#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The rhrepo datasource definitions for pupy data import
"""

import logging
import os

from slugify import slugify

from pupy.datasources import datasource
import shutil


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
            working_parent_dir = os.path.dirname(working_dir)

            if not os.path.exists(working_parent_dir):
                os.makedirs(working_parent_dir)

            shutil.copyfile(self.jsondata['src'], working_dir)

        elif os.path.isdir( self.jsondata['src'] ) :
            if not os.path.exists(working_dir):
                os.makedirs(working_dir)
            shutil.rmtree(working_dir)
            shutil.copytree(self.jsondata['src'], working_dir)

        else:
            LOGGER.error('Source path %s do not exist', self.jsondata['src'])
