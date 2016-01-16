import unittest

from test_credentials import TEST_API_KEY, TEST_ENDPOINT_URL
from yomeka.api.omeka_collection import OmekaCollection
from yomeka.api.omeka_file import OmekaFile
from yomeka.api.omeka_item import OmekaItem
from yomeka.client.omeka_rest_api_client import OmekaRestApiClient


class OmekaRestApiClientTest(unittest.TestCase):
    def setUp(self):
        self.__client = OmekaRestApiClient(api_key=TEST_API_KEY, endpoint_url=TEST_ENDPOINT_URL)

    def test_get_collections(self):
        collections = self.__client.get_collections(page=1, per_page=2)
        self.assertEquals(2, len(collections))
        for collection in collections:
            self.assertTrue(isinstance(collection, OmekaCollection))

    def test_get_files(self):
        files = self.__client.get_files(page=1, per_page=10)
        self.assertEquals(10, len(files))
        for file_ in files:
            self.assertTrue(isinstance(file_, OmekaFile))

    def test_get_items(self):
        items = self.__client.get_items(page=1, per_page=2)
        self.assertEquals(2, len(items))
        for item in items:
            self.assertTrue(isinstance(item, OmekaItem))
