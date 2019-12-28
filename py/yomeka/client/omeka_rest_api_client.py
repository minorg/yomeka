import json
import logging
from urllib.request import urlopen

from yomeka.api.no_such_omeka_collection_exception import NoSuchOmekaCollectionException
from yomeka.api.no_such_omeka_item_exception import NoSuchOmekaItemException
from yomeka.api.omeka_api import OmekaApi
from yomeka.client.omeka_json_parser import OmekaJsonParser


class OmekaRestApiClient(OmekaApi):
    def __init__(self, api_key, endpoint_url):
        self.__api_key = api_key
        if not endpoint_url.endswith('/'):
            endpoint_url = endpoint_url + '/'
        self.__endpoint_url = endpoint_url
        self.__parser = OmekaJsonParser()
        self.__logger = logging.getLogger(self.__class__.__name__)

    def get_all_collections(self, **kwds):
        return self.__get_all_pages(self.get_collections, **kwds)

    def get_all_files(self, **kwds):
        return self.__get_all_pages(self.get_files, **kwds)

    def get_all_items(self, **kwds):
        return self.__get_all_pages(self._get_items, **kwds)

    def _get_collection(self, id):  # @ReservedAssignment
        url = self.__endpoint_url + 'api/collections/%d?key=' % id + self.__api_key
        collection_dict = json.loads(self.__get_url(url))
        if collection_dict.get('message') == 'Invalid record. Record not found.':
            raise NoSuchOmekaCollectionException
        return self.__parser.parse_collection_dict(collection_dict)

    def _get_collections(self, **kwds):
        url = self.__endpoint_url + 'api/collections?key=' + self.__api_key
        for key, value in kwds.items():
            if value is None:
                continue
            url = url + "&%(key)s=%(value)s" % locals()
        return self.__parser.parse_collection_dicts(json.loads(self.__get_url(url)))

    def _get_files(self, **kwds):
        url = self.__endpoint_url + 'api/files?key=' + self.__api_key
        for key, value in kwds.items():
            if value is None:
                continue
            url = url + "&%(key)s=%(value)s" % locals()
        return self.__parser.parse_file_dicts(json.loads(self.__get_url(url)))

    def _get_item(self, id):  # @ReservedAssignment
        url = self.__endpoint_url + 'api/items/%d?key=' % id + self.__api_key
        item_dict = json.loads(self.__get_url(url))
        if item_dict.get('message') == 'Invalid record. Record not found.':
            raise NoSuchOmekaItemException
        return self.__parser.parse_item_dict(item_dict)

    def _get_items(self, **kwds):
        url = self.__endpoint_url + 'api/items?key=' + self.__api_key
        for key, value in kwds.items():
            if value is None:
                continue
            url = url + "&%(key)s=%(value)s" % locals()
        return self.__parser.parse_item_dicts(json.loads(self.__get_url(url)))

    def __get_url(self, url):
        self.__logger.debug("getting URL %s", url)
        url = urlopen(url)
        try:
            return url.read()
        finally:
            url.close()

    def __get_all_pages(self, get_method, **kwds):
        page = 1
        per_page = 50
        while True:
            objects = get_method(page=page, per_page=per_page, **kwds)
            yield from objects
            if len(objects) < per_page:
                return
            page = page + 1
