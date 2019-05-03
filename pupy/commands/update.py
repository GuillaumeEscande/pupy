#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging
import datetime
import sys

from multiprocessing import Pool
from xml.parsers.expat import ExpatError

LOGGER = logging.getLogger(__name__)

def datasource_process_call(input_var) :
    
    try:
        ds, config, args, path = input_var
        ds.update( config, args, path )
        
    except ExpatError as e:
        LOGGER.error('Error for repo %s : %s', ds.name, str(e))
    except :
        LOGGER.error('Error for repo %s : %s', ds.name, sys.exc_info())


def update(config, args):
    
    LOGGER.info('Update of platform %s', config.name)

    path = os.path.abspath( config.workspace )
    if not os.path.exists( path ):
        LOGGER.info('Creation of directory %s', path)
        os.makedirs(path)


    with Pool(config.process) as p:
        inputs = []
        for ds in config.datasources:
            if ds.enable :
                inputs.append((ds, config, args, path))
        
        p.map(datasource_process_call, inputs)
        p.close()
        p.join()