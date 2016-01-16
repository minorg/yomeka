import json

import dateparser

from yomeka.api.omeka_collection import OmekaCollection
from yomeka.api.omeka_element import OmekaElement
from yomeka.api.omeka_element_set import OmekaElementSet
from yomeka.api.omeka_element_text import OmekaElementText
from yomeka.api.omeka_file import OmekaFile
from yomeka.api.omeka_file_urls import OmekaFileUrls
from yomeka.api.omeka_item import OmekaItem
from yomeka.api.omeka_item_type import OmekaItemType
from yomeka.api.omeka_tag import OmekaTag


class OmekaJsonParser(object):
    def parse_collection_dict(self, collection_dict):
        return \
                OmekaCollection.Builder()\
                    .set_element_texts(self.__parse_element_texts(collection_dict.get('element_texts', [])))\
                    .set_added(self.__parse_date_time(collection_dict['added']))\
                    .set_featured(collection_dict['featured'])\
                    .set_id(collection_dict['id'])\
                    .set_json(json.dumps(collection_dict))\
                    .set_items_count(collection_dict['items']['count'])\
                    .set_modified(self.__parse_date_time(collection_dict['modified']))\
                    .set_public(collection_dict['public'])\
                    .set_url(collection_dict['url'])\
                    .build()

    def parse_collection_dicts(self, collection_dicts):
        collections = []
        for collection_dict in collection_dicts:
            collections.append(self.parse_collection_dict(collection_dict))
        return tuple(collections)

    def __parse_date_time(self, date_time_str):
        return dateparser.parse(date_time_str)

    def __parse_element_texts(self, element_text_dicts):
        element_texts = []
        for element_text_dict in element_text_dicts:
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
        return tuple(element_texts)

    def parse_file_dict(self, file_dict):
        file_urls_builder = OmekaFileUrls.Builder()
        for key, value in file_dict['file_urls'].iteritems():
            getattr(file_urls_builder, 'set_' + key)(value)
        file_urls = file_urls_builder.build()

        return \
            OmekaFile.Builder()\
                .set_authentication(file_dict['authentication'])\
                .set_element_texts(self.__parse_element_texts(file_dict.get('element_texts', [])))\
                .set_added(self.__parse_date_time(file_dict['added']))\
                .set_file_urls(file_urls)\
                .set_has_derivative_image(file_dict['has_derivative_image'])\
                .set_id(file_dict['id'])\
                .set_item_id(file_dict['item']['id'])\
                .set_json(json.dumps(file_dict))\
                .set_mime_type(file_dict['mime_type'])\
                .set_modified(self.__parse_date_time(file_dict['modified']))\
                .set_original_filename(file_dict['original_filename'])\
                .set_size(file_dict['size'])\
                .set_stored(file_dict['stored'])\
                .set_type_os(file_dict['type_os'])\
                .set_url(file_dict['url'])\
                .build()

    def parse_file_dicts(self, file_dicts):
        files = []
        for file_dict in file_dicts:
            files.append(self.parse_file_dict(file_dict))
        return tuple(files)

    def parse_item_dict(self, item_dict):
        element_texts = self.__parse_element_texts(item_dict.get('element_texts', []))

        item_type_dict = item_dict['item_type']
        if item_type_dict is not None:
            item_type = \
                OmekaItemType.Builder()\
                    .set_id(item_type_dict['id'])\
                    .set_name(item_type_dict['name'])\
                    .set_url(item_type_dict['url'])\
                    .build()
        else:
            item_type = None

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

        return \
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

    def parse_item_dicts(self, item_dicts):
        items = []
        for item_dict in item_dicts:
            items.append(self.parse_item_dict(item_dict))
        return tuple(items)
