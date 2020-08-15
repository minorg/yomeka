#!/usr/bin/env python

import argparse
import csv
import os.path
import sys


try:
    __import__('yomeka')
except ImportError:
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    __import__('yomeka')

from yomeka.classic.omeka_classic_rest_api_client import OmekaClassicRestApiClient



class YomekaCli(object):
    def __init__(self, args, client, output_file):
        self.__args = args
        self.__client = client
        self.__output_file = output_file

    @staticmethod
    def __csv_encode(str_):
        return str_.encode('utf-8')

    def _item_command(self):
        self.__print_items((self.__client.get_item(self.__args.item_id),))

    def _items_command(self):
        self.__print_items(self.__client.get_all_items())

    @classmethod
    def main(cls):
        argument_parser = argparse.ArgumentParser()
        argument_parser.add_argument('--api-key', required=True)
        argument_parser.add_argument('--endpoint-url', required=True)
        argument_parser.add_argument('--format', default='csv')
        argument_parser.add_argument('-o', '--output-file')

        subparsers = argument_parser.add_subparsers()

        items_parser = subparsers.add_parser('item', help='print one item')
        items_parser.add_argument('item_id', type=int)
        items_parser.set_defaults(command='item')

        items_parser = subparsers.add_parser('items', help='print all items')
        items_parser.set_defaults(command='items')

        args = argument_parser.parse_args()

        client = OmekaClassicRestApiClient(api_key=args.api_key, endpoint_url=args.endpoint_url)

        if args.output_file is not None:
            output_file = open(args.output_file, 'w+b')
        else:
            output_file = sys.stdout

        inst = cls(args=args, client=client, output_file=output_file)
        getattr(inst, '_' + args.command + '_command')()

    def __print_items(self, items):
        if self.__args.format != 'csv':
            raise NotImplementedError(self.__args.format)

        csv_header = (
            'item_id',
            'item_added',
            'item_featured',
            'item_modified',
            'item_public',
            'item_tags',
            'item_type',
            'element_set_name',
            'element_name',
            'element_text'
        )
        csv_writer = csv.writer(self.__output_file)
        csv_writer.writerow(csv_header)

        for item in items:
            for element_text in item.element_texts:
                csv_row = []
                csv_row.append(item.id)
                csv_row.append(item.added)
                csv_row.append(item.featured)
                csv_row.append(item.modified)
                csv_row.append(item.public)
                csv_row.append('|'.join(self.__csv_encode(tag.name) for tag in item.tags))
                csv_row.append(item.item_type.name if item.item_type is not None else '')
                csv_row.append(self.__csv_encode(element_text.element_set.name))
                csv_row.append(self.__csv_encode(element_text.element.name))
                csv_row.append(self.__csv_encode(element_text.text))
                assert len(csv_row) == len(csv_header)
                csv_writer.writerow(csv_row)

        self.__output_file.flush()

assert __name__ == '__main__'
YomekaCli.main()
