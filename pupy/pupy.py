#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
pupy
a python service to synchro isolated platform
"""


import argparse
import json
import logging
import sys


import pupy_config
from commands import update

import _version

__version__ = _version.get_versions()['version']

LOGGER = logging.getLogger(__name__)
logging.root.setLevel( logging.INFO )


sys.stdout = sys.__stdout__
root = logging.getLogger()
root.setLevel(logging.DEBUG)
root.addHandler(logging.StreamHandler(sys.stdout))


def do_update(config, args):
    """Update repo"""
    update.update(config, args)
    _ = args

def do_export(config, args):
    """Export repo"""
    print("do_export")

def do_import(config, args):
    """Import repo"""
    print("do_import")
    
def do_version(config, args):
    """Shows the version"""
    print(__version__)
    _ = args


def __add_command(subparsers, command, func):
    """Add the cnfig and verbose argument to given parser"""
    parser = subparsers.add_parser(command, help=command)
    if func is not None:
        parser.set_defaults(func=func)
    return parser


def main():
    """The main
    call pupy [--config CONFIG] update
    call pupy [--config CONFIG] export
    call pupy [--config CONFIG] import
    call pupy version
    """

    parser = argparse.ArgumentParser()
    parser.add_argument( '-c', '--config', help='The config file')
    parser.add_argument( '-p', '--proxy', help='Proxy config (wpad.dat url)')
    parser.add_argument('-v', '--verbose', action='store_true', default=False, help='Go into verbose')

    subparser = parser.add_subparsers()

    # Commands update
    update_parser = __add_command(subparser, 'update', do_update)

    # Commands export
    export_parser = __add_command(subparser, 'export', do_export)

    # Commands import
    import_parser = __add_command(subparser, 'import', do_import)

    # Commands version
    version_parser = __add_command(subparser, 'version', do_version)

    # args traitement
    args = parser.parse_args()
    config_file = args.config
    verbose = args.verbose

    if verbose:
        logging.root.setLevel(logging.DEBUG)
        LOGGER.setLevel(logging.DEBUG)
        LOGGER.info('%s with config %s', function.__name__, config_file)

    config = pupy_config.PupyConfig.load(config_file)

    args.func(config, args)

if __name__ == '__main__':
    main()
