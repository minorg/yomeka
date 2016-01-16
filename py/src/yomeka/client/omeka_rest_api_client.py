import json
import logging
from urllib import urlopen

from yomeka.api.omeka_api import OmekaApi
from yomeka.client.omeka_json_parser import OmekaJsonParser


class OmekaRestApiClient(OmekaApi):
    def __init__(self, api_key, endpoint_url):
        self.__api_key = api_key
        if not endpoint_url.endswith('/'):
            endpoint_url = endpoint_url + '/'
        self.__endpoint_url = endpoint_url
        self.__parser = OmekaJsonParser()
        self.__logger = logging.getLogger(self.__class__.__module__ + '.' + self.__class__.__name__)

    def _get_collections(self, **kwds):
        url = self.__endpoint_url + 'api/collections?key=' + self.__api_key
        for key, value in kwds.iteritems():
            url = url + "&%(key)s=%(value)s" % locals()
        return self.__parser.parse_collection_dicts(json.loads(self.__get_url(url)))

    def _get_files(self, **kwds):
        url = self.__endpoint_url + 'api/files?key=' + self.__api_key
        for key, value in kwds.iteritems():
            url = url + "&%(key)s=%(value)s" % locals()
        return self.__parser.parse_file_dicts(json.loads(self.__get_url(url)))

    def _get_items(self, **kwds):
        url = self.__endpoint_url + 'api/items?key=' + self.__api_key
        for key, value in kwds.iteritems():
            url = url + "&%(key)s=%(value)s" % locals()
        return self.__parser.parse_item_dicts(json.loads(self.__get_url(url)))

    def __get_url(self, url):
        self.__logger.debug("getting URL %s", url)
        url = urlopen(url)
        try:
            return url.read()
        finally:
            url.close()
