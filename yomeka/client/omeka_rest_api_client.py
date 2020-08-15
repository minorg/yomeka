import json
import logging
from typing import Optional, Tuple
from urllib.error import HTTPError
from urllib.request import urlopen

from yomeka.api.no_such_omeka_collection_exception import NoSuchOmekaCollectionException
from yomeka.api.no_such_omeka_item_exception import NoSuchOmekaItemException
from yomeka.api.omeka_collection import OmekaCollection
from yomeka.api.omeka_file import OmekaFile
from yomeka.api.omeka_item import OmekaItem
from yomeka.client.omeka_json_parser import OmekaJsonParser


class OmekaRestApiClient:
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

    def __get_all_pages(self, get_method, **kwds):
        page = 1
        per_page = 50
        while True:
            objects = get_method(page=page, per_page=per_page, **kwds)
            yield from objects
            if len(objects) < per_page:
                return
            page = page + 1

    def get_collection(self, id: int) -> OmekaCollection:  # @ReservedAssignment
        url = self.__endpoint_url + 'api/collections/%d?key=' % id + self.__api_key
        try:
            collection_dict = json.loads(self.__get_url(url))
        except HTTPError as e:
            if e.code == 404:
                raise NoSuchOmekaCollectionException
            else:
                raise
        if collection_dict.get('message') == 'Invalid record. Record not found.':
            raise NoSuchOmekaCollectionException
        return self.__parser.parse_collection_dict(collection_dict)

    def get_collections(self, *, page: Optional[int] = None, per_page: Optional[int] = None, **kwds) -> Tuple[OmekaCollection, ...]:
        url = self.__endpoint_url + 'api/collections?key=' + self.__api_key
        if page is not None:
            kwds["page"] = page
        if per_page is not None:
            kwds["per_page"] = per_page
        for key, value in kwds.items():
            if value is None:
                continue
            url = url + "&%(key)s=%(value)s" % locals()
        return self.__parser.parse_collection_dicts(json.loads(self.__get_url(url)))

    def get_files(self, *, item: Optional[int] = None, page: Optional[int] = None, per_page: Optional[int] = None, **kwds) -> Tuple[OmekaFile, ...]:
        url = self.__endpoint_url + 'api/files?key=' + self.__api_key
        if item is not None:
            kwds["item"] = item
        if page is not None:
            kwds["page"] = page
        if per_page is not None:
            kwds["per_page"] = per_page
        for key, value in kwds.items():
            if value is None:
                continue
            url = url + "&%(key)s=%(value)s" % locals()
        return self.__parser.parse_file_dicts(json.loads(self.__get_url(url)))

    def get_item(self, id: int) -> OmekaItem:  # @ReservedAssignment
        url = self.__endpoint_url + 'api/items/%d?key=' % id + self.__api_key
        try:
            item_dict = json.loads(self.__get_url(url))
        except HTTPError as e:
            if e.code == 404:
                raise NoSuchOmekaItemException
            else:
                raise
        if item_dict.get('message') == 'Invalid record. Record not found.':
            raise NoSuchOmekaItemException
        return self.__parser.parse_item_dict(item_dict)

    def get_items(self, collection: Optional[int] = None, page: Optional[int] = None, per_page: Optional[int] = None, **kwds) -> Tuple[OmekaItem, ...]:
        url = self.__endpoint_url + 'api/items?key=' + self.__api_key
        if collection is not None:
            kwds["collection"] = collection
        if page is not None:
            kwds["page"] = page
        if per_page is not None:
            kwds["per_page"] = per_page
        for key, value in kwds.items():
            if value is None:
                continue
            url = url + "&%(key)s=%(value)s" % locals()
        return self.__parser.parse_item_dicts(json.loads(self.__get_url(url)))

    def __get_url(self, url) -> str:
        self.__logger.debug("getting URL %s", url)
        url = urlopen(url)
        try:
            return url.read()
        finally:
            url.close()
