#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging
import datetime

LOGGER = logging.getLogger(__name__)

def update(config):
    
    LOGGER.info('Update of platform %s', config.name)

    path = os.path.abspath( config.workspace )
    if not os.path.exists( path ):
        LOGGER.info('Creation of directory %s', path)
        os.makedirs(path)

    for ds in config.datasources:
        start = datetime.datetime.now()
        LOGGER.info('Update of module %s started ad %s', ds.name, start)
        ds.update( path )
        end = datetime.datetime.now()
        elapsed = end - start
        LOGGER.info('End of update on %f seconds', elapsed.total_seconds())