#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
pupy
a python service to synchro isolated platform
"""


import argparse
import json
import logging


LOGGER = logging.getLogger(__name__)
logging.root.setLevel( logging.INFO )


def do_update(args):
    """Update repo"""
    print("do_update")

def do_export(args):
    """Export repo"""
    print("do_export")

def do_import(args):
    """Import repo"""
    print("do_import")
    


def do_version(args):
    """Shows the version"""
    print(__version__)
    _ = args

def __default_config(subparsers, command, func):
    """Add the cnfig and verbose argument to given parser"""
    parser = subparsers.add_parser(command, help=command)
    parser.add_argument('-c', '--config', help='The config file', required=True)
    parser.add_argument('-v', '--verbose', action='store_true', default=False, help='Go into verbose')
    parser.set_defaults(func=func)
    return parser

def main():
    """The main
    call pupy update [--config CONFIG]
    call pupy export [--config CONFIG]
    call pupy import [--config CONFIG]
    call pupy version
    """

    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers()

    __default_config(subparser, 'update', do_update)
    __default_config(subparser, 'export', do_export)
    __default_config(subparser, 'import', do_import)

    version_parser = subparser.add_parser('version')
    version_parser.set_defaults(func=do_version)

    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
