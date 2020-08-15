import unittest

from .test_credentials import TEST_API_KEY, TEST_COLLECTION_ID, TEST_ENDPOINT_URL, TEST_ITEM_ID
from yomeka.classic.no_such_omeka_classic_collection_exception import NoSuchOmekaClassicCollectionException
from yomeka.classic.no_such_omeka_classic_item_exception import NoSuchOmekaClassicItemException
from yomeka.classic.omeka_classic_collection import OmekaClassicCollection
from yomeka.classic.omeka_classic_file import OmekaClassicFile
from yomeka.classic.omeka_classic_item import OmekaClassicItem
from yomeka.classic.omeka_classic_rest_api_client import OmekaClassicRestApiClient


class OmekaClassicRestApiClientTest(unittest.TestCase):
    def setUp(self):
        self.__client = OmekaClassicRestApiClient(api_key=TEST_API_KEY, endpoint_url=TEST_ENDPOINT_URL)

    def test_get_collection(self):
        self.__client.get_collection(id=TEST_COLLECTION_ID)
        try:
            self.__client.get_collection(id=42)
            self.fail()
        except NoSuchOmekaClassicCollectionException:
            pass

    def test_get_collections(self):
        collections = self.__client.get_collections(page=1, per_page=2)
        self.assertEquals(2, len(collections))
        for collection in collections:
            self.assertTrue(isinstance(collection, OmekaClassicCollection))

    def test_get_files(self):
        files = self.__client.get_files(page=1, per_page=10)
        self.assertEquals(10, len(files))
        for file_ in files:
            self.assertTrue(isinstance(file_, OmekaClassicFile))

    def test_get_item(self):
        self.__client.get_item(id=TEST_ITEM_ID)
        try:
            self.__client.get_item(id=4242424)
            self.fail()
        except NoSuchOmekaClassicItemException:
            pass

    def test_get_items(self):
        items = self.__client.get_items(page=1, per_page=2)
        self.assertEquals(2, len(items))
        for item in items:
            self.assertTrue(isinstance(item, OmekaClassicItem))
