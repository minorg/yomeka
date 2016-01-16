from itertools import ifilterfalse
import __builtin__
import yomeka.api.omeka_item


class OmekaApi(object):
    def get_items(
        self,
    ):
        '''
        :rtype: tuple(yomeka.api.omeka_item.OmekaItem)
        '''

        get_items_return_value = self._get_items()

        if not (isinstance(get_items_return_value, tuple) and len(list(ifilterfalse(lambda _: isinstance(_, yomeka.api.omeka_item.OmekaItem), get_items_return_value))) == 0):
            raise TypeError(getattr(__builtin__, 'type')(get_items_return_value))

        return get_items_return_value

    def _get_items(
        self,
    ):
        raise NotImplementedError(self.__class__.__module__ + '.' + self.__class__.__name__ + '._get_items')
