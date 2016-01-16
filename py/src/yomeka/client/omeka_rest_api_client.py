import json
import logging
from urllib import urlopen

import dateparser

from yomeka.api.omeka_api import OmekaApi
from yomeka.api.omeka_element import OmekaElement
from yomeka.api.omeka_element_set import OmekaElementSet
from yomeka.api.omeka_element_text import OmekaElementText
from yomeka.api.omeka_item import OmekaItem
from yomeka.api.omeka_item_type import OmekaItemType
from yomeka.api.omeka_tag import OmekaTag


class OmekaRestApiClient(OmekaApi):
    def __init__(self, api_key, endpoint_url):
        self.__api_key = api_key
        if not endpoint_url.endswith('/'):
            endpoint_url = endpoint_url + '/'
        self.__endpoint_url = endpoint_url
        self.__logger = logging.getLogger(self.__class__.__module__ + '.' + self.__class__.__name__)

    def _get_items(self, **kwds):
        url = self.__endpoint_url + 'api/items?key=' + self.__api_key
        for key, value in kwds.iteritems():
            url = url + "&%(key)s=%(value)s" % locals()
        item_dicts = json.loads(self.__get_url(url))
        items = []
        for item_dict in item_dicts:
            element_texts = []
            for element_text_dict in item_dict.get('element_texts', []):
                element_dict = element_text_dict['element']
                element = \
                    OmekaElement.Builder()\
                        .set_id(element_dict['id'])\
                        .set_name(element_dict['name'])\
                        .set_url(element_dict['url'])\
                        .build()

                element_set_dict = element_text_dict['element_set']
                element_set = \
                    OmekaElementSet.Builder()\
                        .set_id(element_set_dict['id'])\
                        .set_name(element_set_dict['name'])\
                        .set_url(element_set_dict['url'])\
                        .build()

                element_text = \
                    OmekaElementText.Builder()\
                        .set_element(element)\
                        .set_element_set(element_set)\
                        .set_html(element_text_dict['html'])\
                        .set_text(element_text_dict['text'])\
                        .build()
                element_texts.append(element_text)
            element_texts = tuple(element_texts)

            item_type_dict = item_dict['item_type']
            item_type = \
                OmekaItemType.Builder()\
                    .set_id(item_type_dict['id'])\
                    .set_name(item_type_dict['name'])\
                    .set_url(item_type_dict['url'])\
                    .build()

            tags = []
            for tag_dict in item_dict.get('tags', []):
                tag = \
                    OmekaTag.Builder()\
                        .set_id(tag_dict['id'])\
                        .set_name(tag_dict['name'])\
                        .set_url(tag_dict['url'])\
                        .build()
                tags.append(tag)
            tags = tuple(tags)

            item = \
                OmekaItem.Builder()\
                    .set_added(self.__parse_date_time(item_dict['added']))\
                    .set_element_texts(element_texts)\
                    .set_featured(item_dict['featured'])\
                    .set_id(item_dict['id'])\
                    .set_item_type(item_type)\
                    .set_json(json.dumps(item_dict))\
                    .set_modified(self.__parse_date_time(item_dict['modified']))\
                    .set_public(item_dict['public'])\
                    .set_tags(tags)\
                    .set_url(item_dict['url'])\
                    .build()
            items.append(item)
        return tuple(items)

    def __get_url(self, url):
        self.__logger.debug("getting URL %s", url)
        url = urlopen(url)
        try:
            return url.read()
        finally:
            url.close()

    def __parse_date_time(self, date_time_str):
        return dateparser.parse(date_time_str)
