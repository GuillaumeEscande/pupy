#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The rhrepo datasource definitions for pupy data import
"""

import logging
import os

from slugify import slugify

from pupy.datasources import datasource
from pupy.lib import repo



LOGGER = logging.getLogger(__name__)

class RhRepo(datasource.DataSource):
    """The generic datasource model"""

    def __init__(self, jsondata):
        """Initialize"""
        super(RhRepo, self).__init__(jsondata)
        

    def update(self, config, args, workspace):
        """update"""

        path = slugify( self.jsondata['name'] )
        if "path" in self.jsondata:
            path = self.jsondata['path']
        working_dir = os.path.join(workspace,path)
        
        if not os.path.exists(working_dir):
            os.makedirs(working_dir)
        
        expiration = None
        if "expiration" in self.jsondata:
            expiration = self.jsondata['expiration']

        rhrepo = repo.Repo( self.jsondata['url'], args.proxy, config.thread, expiration)

        rhrepo.reposync(working_dir)