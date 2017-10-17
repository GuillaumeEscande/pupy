#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The rhrepo datasource definitions for pupy data import
"""

import logging
import os

from slugify import slugify

from datasources import datasource
from lib import repo


LOGGER = logging.getLogger(__name__)

class RhRepo(datasource.DataSource):
    """The generic datasource model"""

    def __init__(self, jsondata):
        """Initialize"""
        super(RhRepo, self).__init__(jsondata)
        

    def update(self, config, args, workspace):
        """update"""

        working_dir = os.path.join(workspace,slugify( self.jsondata['name'] ))
        if not os.path.exists(working_dir):
            os.makedirs(working_dir)
        
        rhrepo = repo.Repo( self.jsondata['url'], args.proxy )

        rhrepo.reposync(working_dir)