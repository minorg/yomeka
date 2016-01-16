from itertools import ifilterfalse
import __builtin__
import yomeka.api.omeka_collection
import yomeka.api.omeka_item


class OmekaApi(object):
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
