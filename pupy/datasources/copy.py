#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The rhrepo datasource definitions for pupy data import
"""

import logging

from datasources import datasource


LOGGER = logging.getLogger(__name__)

class Copy(datasource.DataSource):
    """The generic datasource model"""

    def __init__(self, jsondata):
        """Initialize"""
        super(Copy, self).__init__(jsondata)
        

    def update(self, workspace):
        """update"""
        print('TODO')