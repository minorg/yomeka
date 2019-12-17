from itertools import ifilterfalse
import __builtin__
import yomeka.api.omeka_collection
import yomeka.api.omeka_file
import yomeka.api.omeka_item


class OmekaApi(object):
    def get_collection(
        self,
        id=None,  # @ReservedAssignment
    ):
        '''
        :type id: int
        :rtype: yomeka.api.omeka_collection.OmekaCollection
        '''

        if id is None:
            raise ValueError('id is required')
        if not isinstance(id, int):
            raise TypeError("expected id to be a int but it is a %s" % getattr(__builtin__, 'type')(id))

        get_collection_return_value = self._get_collection(id=id)

        if not isinstance(get_collection_return_value, yomeka.api.omeka_collection.OmekaCollection):
            raise TypeError(getattr(__builtin__, 'type')(get_collection_return_value))

        return get_collection_return_value

    def _get_collection(
        self,
        id,  # @ReservedAssignment
    ):
        raise NotImplementedError(self.__class__.__module__ + '.' + self.__class__.__name__ + '._get_collection')

    def get_collections(
        self,
        page=None,
        per_page=None,
    ):
        '''
        :type page: int or None
        :type per_page: int or None
        :rtype: tuple(yomeka.api.omeka_collection.OmekaCollection)
        '''

        if page is not None:
            if not isinstance(page, int):
                raise TypeError("expected page to be a int but it is a %s" % getattr(__builtin__, 'type')(page))
        if per_page is not None:
            if not isinstance(per_page, int):
                raise TypeError("expected per_page to be a int but it is a %s" % getattr(__builtin__, 'type')(per_page))

        get_collections_return_value = self._get_collections(page=page, per_page=per_page)

        if not (isinstance(get_collections_return_value, tuple) and len(list(ifilterfalse(lambda _: isinstance(_, yomeka.api.omeka_collection.OmekaCollection), get_collections_return_value))) == 0):
            raise TypeError(getattr(__builtin__, 'type')(get_collections_return_value))

        return get_collections_return_value

    def _get_collections(
        self,
        page,
        per_page,
    ):
        raise NotImplementedError(self.__class__.__module__ + '.' + self.__class__.__name__ + '._get_collections')

    def get_files(
        self,
        item=None,
        page=None,
        per_page=None,
    ):
        '''
        :type item: int or None
        :type page: int or None
        :type per_page: int or None
        :rtype: tuple(yomeka.api.omeka_file.OmekaFile)
        '''

        if item is not None:
            if not isinstance(item, int):
                raise TypeError("expected item to be a int but it is a %s" % getattr(__builtin__, 'type')(item))
        if page is not None:
            if not isinstance(page, int):
                raise TypeError("expected page to be a int but it is a %s" % getattr(__builtin__, 'type')(page))
        if per_page is not None:
            if not isinstance(per_page, int):
                raise TypeError("expected per_page to be a int but it is a %s" % getattr(__builtin__, 'type')(per_page))

        get_files_return_value = self._get_files(item=item, page=page, per_page=per_page)

        if not (isinstance(get_files_return_value, tuple) and len(list(ifilterfalse(lambda _: isinstance(_, yomeka.api.omeka_file.OmekaFile), get_files_return_value))) == 0):
            raise TypeError(getattr(__builtin__, 'type')(get_files_return_value))

        return get_files_return_value

    def _get_files(
        self,
        item,
        page,
        per_page,
    ):
        raise NotImplementedError(self.__class__.__module__ + '.' + self.__class__.__name__ + '._get_files')

    def get_item(
        self,
        id=None,  # @ReservedAssignment
    ):
        '''
        :type id: int
        :rtype: yomeka.api.omeka_item.OmekaItem
        '''

        if id is None:
            raise ValueError('id is required')
        if not isinstance(id, int):
            raise TypeError("expected id to be a int but it is a %s" % getattr(__builtin__, 'type')(id))

        get_item_return_value = self._get_item(id=id)

        if not isinstance(get_item_return_value, yomeka.api.omeka_item.OmekaItem):
            raise TypeError(getattr(__builtin__, 'type')(get_item_return_value))

        return get_item_return_value

    def _get_item(
        self,
        id,  # @ReservedAssignment
    ):
        raise NotImplementedError(self.__class__.__module__ + '.' + self.__class__.__name__ + '._get_item')

    def get_items(
        self,
        collection=None,
        page=None,
        per_page=None,
    ):
        '''
        :type collection: int or None
        :type page: int or None
        :type per_page: int or None
        :rtype: tuple(yomeka.api.omeka_item.OmekaItem)
        '''

        if collection is not None:
            if not isinstance(collection, int):
                raise TypeError("expected collection to be a int but it is a %s" % getattr(__builtin__, 'type')(collection))
        if page is not None:
            if not isinstance(page, int):
                raise TypeError("expected page to be a int but it is a %s" % getattr(__builtin__, 'type')(page))
        if per_page is not None:
            if not isinstance(per_page, int):
                raise TypeError("expected per_page to be a int but it is a %s" % getattr(__builtin__, 'type')(per_page))

        get_items_return_value = self._get_items(collection=collection, page=page, per_page=per_page)

        if not (isinstance(get_items_return_value, tuple) and len(list(ifilterfalse(lambda _: isinstance(_, yomeka.api.omeka_item.OmekaItem), get_items_return_value))) == 0):
            raise TypeError(getattr(__builtin__, 'type')(get_items_return_value))

        return get_items_return_value

    def _get_items(
        self,
        collection,
        page,
        per_page,
    ):
        raise NotImplementedError(self.__class__.__module__ + '.' + self.__class__.__name__ + '._get_items')
