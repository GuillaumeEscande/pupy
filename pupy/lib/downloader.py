#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The file downloader
"""

import os
import logging
import requests
import hashlib

from clint.textui import progress

from pypac import PACSession, get_pac


LOGGER = logging.getLogger(__name__)

logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)

class Downloader():
    """The generic datasource model"""

    def __init__(self, url, proxy=None):
        """Initialize"""

        if proxy:
            pac = get_pac(url=proxy)
            self.__session = PACSession(pac)
        else:
            self.__session = requests

        self.__url = url

    def download(self, path=None, checksum=None, checksum_type=None):
        """download"""

        if path :

            update = False
            LOGGER.debug(u"Get file %s " %(self.__url))

            if not os.path.isfile(path) :
                LOGGER.info(u"Téléchargement du fichier %s", self.__url)
                update = True
            elif checksum is not None:
                if checksum_type == "sha256":
                    h = hashlib.sha256()
                elif checksum_type == "sha":
                    h = hashlib.sha1()
                else : 
                    raise Exception("checksun type inconnue : " + checksum_type)
                with open(path, 'rb', buffering=0) as f:
                    for b in iter(lambda : f.read(128*1024), b''):
                        h.update(b)
                calculated = h.hexdigest()
                if checksum != calculated:
                    LOGGER.debug(u"Different checksum -> mise à jour du fichier")
                    update = True
                else :
                    LOGGER.debug(u"Déjà présent et déjà à jour")
            else :
                update = True

            if update:
                try:
                    f = None
                    f = open( path, 'wb' )

                    r = self.__session.get(self.__url, stream=True)

                    total_length = int(r.headers.get('content-length'))

                    for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
                        if chunk:
                            f.write(chunk)
                            f.flush()
                            
                except requests.ConnectionError as e:
                    LOGGER.error('Error on opening connection to url %s ', self.__url)
                except IOError as e:
                    LOGGER.error('Error on opening output file %s', path)
                finally:
                    if f is not None :
                        f.close()
        else :
            return self.__session.get(self.__url).content