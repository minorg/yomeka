from datetime import datetime
from itertools import ifilterfalse
import __builtin__
import yomeka.api.omeka_element_text


class OmekaCollection(object):
    class Builder(object):
        def __init__(
            self,
            element_texts=None,
            added=None,
            featured=None,
            id=None,  # @ReservedAssignment
            items_count=None,
            modified=None,
            public=None,
            url=None,
        ):
            '''
            :type element_texts: tuple(yomeka.api.omeka_element_text.OmekaElementText)
            :type added: datetime
            :type featured: bool
            :type id: int
            :type items_count: int
            :type modified: datetime
            :type public: bool
            :type url: str
            '''

            self.__element_texts = element_texts
            self.__added = added
            self.__featured = featured
            self.__id = id
            self.__items_count = items_count
            self.__modified = modified
            self.__public = public
            self.__url = url

        def build(self):
            return OmekaCollection(element_texts=self.__element_texts, added=self.__added, featured=self.__featured, id=self.__id, items_count=self.__items_count, modified=self.__modified, public=self.__public, url=self.__url)

        @property
        def added(self):
            '''
            :rtype: datetime
            '''

            return self.__added

        @property
        def element_texts(self):
            '''
            :rtype: tuple(yomeka.api.omeka_element_text.OmekaElementText)
            '''

            return self.__element_texts

        @property
        def featured(self):
            '''
            :rtype: bool
            '''

            return self.__featured

        @property
        def id(self):  # @ReservedAssignment
            '''
            :rtype: int
            '''

            return self.__id

        @property
        def items_count(self):
            '''
            :rtype: int
            '''

            return self.__items_count

        @property
        def modified(self):
            '''
            :rtype: datetime
            '''

            return self.__modified

        @property
        def public(self):
            '''
            :rtype: bool
            '''

            return self.__public

        def set_added(self, added):
            '''
            :type added: datetime
            '''

            self.__added = added
            return self

        def set_element_texts(self, element_texts):
            '''
            :type element_texts: tuple(yomeka.api.omeka_element_text.OmekaElementText)
            '''

            self.__element_texts = element_texts
            return self

        def set_featured(self, featured):
            '''
            :type featured: bool
            '''

            self.__featured = featured
            return self

        def set_id(self, id):  # @ReservedAssignment
            '''
            :type id: int
            '''

            self.__id = id
            return self

        def set_items_count(self, items_count):
            '''
            :type items_count: int
            '''

            self.__items_count = items_count
            return self

        def set_modified(self, modified):
            '''
            :type modified: datetime
            '''

            self.__modified = modified
            return self

        def set_public(self, public):
            '''
            :type public: bool
            '''

            self.__public = public
            return self

        def set_url(self, url):
            '''
            :type url: str
            '''

            self.__url = url
            return self

        def update(self, omeka_collection):
            '''
            :type element_texts: tuple(yomeka.api.omeka_element_text.OmekaElementText)
            :type added: datetime
            :type featured: bool
            :type id: int
            :type items_count: int
            :type modified: datetime
            :type public: bool
            :type url: str
            '''

            if isinstance(omeka_collection, OmekaCollection):
                self.set_element_texts(omeka_collection.element_texts)
                self.set_added(omeka_collection.added)
                self.set_featured(omeka_collection.featured)
                self.set_id(omeka_collection.id)
                self.set_items_count(omeka_collection.items_count)
                self.set_modified(omeka_collection.modified)
                self.set_public(omeka_collection.public)
                self.set_url(omeka_collection.url)
            elif isinstance(omeka_collection, dict):
                for key, value in omeka_collection.iteritems():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(omeka_collection)
            return self

        @property
        def url(self):
            '''
            :rtype: str
            '''

            return self.__url

        @added.setter
        def added(self, added):
            '''
            :type added: datetime
            '''

            self.set_added(added)

        @element_texts.setter
        def element_texts(self, element_texts):
            '''
            :type element_texts: tuple(yomeka.api.omeka_element_text.OmekaElementText)
            '''

            self.set_element_texts(element_texts)

        @featured.setter
        def featured(self, featured):
            '''
            :type featured: bool
            '''

            self.set_featured(featured)

        @id.setter
        def id(self, id):  # @ReservedAssignment
            '''
            :type id: int
            '''

            self.set_id(id)

        @items_count.setter
        def items_count(self, items_count):
            '''
            :type items_count: int
            '''

            self.set_items_count(items_count)

        @modified.setter
        def modified(self, modified):
            '''
            :type modified: datetime
            '''

            self.set_modified(modified)

        @public.setter
        def public(self, public):
            '''
            :type public: bool
            '''

            self.set_public(public)

        @url.setter
        def url(self, url):
            '''
            :type url: str
            '''

            self.set_url(url)

    def __init__(
        self,
        element_texts,
        added,
        featured,
        id,  # @ReservedAssignment
        items_count,
        modified,
        public,
        url,
    ):
        '''
        :type element_texts: tuple(yomeka.api.omeka_element_text.OmekaElementText)
        :type added: datetime
        :type featured: bool
        :type id: int
        :type items_count: int
        :type modified: datetime
        :type public: bool
        :type url: str
        '''

        if element_texts is None:
            raise ValueError('element_texts is required')
        if not (isinstance(element_texts, tuple) and len(list(ifilterfalse(lambda _: isinstance(_, yomeka.api.omeka_element_text.OmekaElementText), element_texts))) == 0):
            raise TypeError("expected element_texts to be a tuple(yomeka.api.omeka_element_text.OmekaElementText) but it is a %s" % getattr(__builtin__, 'type')(element_texts))
        self.__element_texts = element_texts

        if added is None:
            raise ValueError('added is required')
        if not isinstance(added, datetime):
            raise TypeError("expected added to be a datetime but it is a %s" % getattr(__builtin__, 'type')(added))
        self.__added = added

        if featured is None:
            raise ValueError('featured is required')
        if not isinstance(featured, bool):
            raise TypeError("expected featured to be a bool but it is a %s" % getattr(__builtin__, 'type')(featured))
        self.__featured = featured

        if id is None:
            raise ValueError('id is required')
        if not isinstance(id, int):
            raise TypeError("expected id to be a int but it is a %s" % getattr(__builtin__, 'type')(id))
        self.__id = id

        if items_count is None:
            raise ValueError('items_count is required')
        if not isinstance(items_count, int):
            raise TypeError("expected items_count to be a int but it is a %s" % getattr(__builtin__, 'type')(items_count))
        self.__items_count = items_count

        if modified is None:
            raise ValueError('modified is required')
        if not isinstance(modified, datetime):
            raise TypeError("expected modified to be a datetime but it is a %s" % getattr(__builtin__, 'type')(modified))
        self.__modified = modified

        if public is None:
            raise ValueError('public is required')
        if not isinstance(public, bool):
            raise TypeError("expected public to be a bool but it is a %s" % getattr(__builtin__, 'type')(public))
        self.__public = public

        if url is None:
            raise ValueError('url is required')
        if not isinstance(url, basestring):
            raise TypeError("expected url to be a str but it is a %s" % getattr(__builtin__, 'type')(url))
        self.__url = url

    def __eq__(self, other):
        if self.element_texts != other.element_texts:
            return False
        if self.added != other.added:
            return False
        if self.featured != other.featured:
            return False
        if self.id != other.id:
            return False
        if self.items_count != other.items_count:
            return False
        if self.modified != other.modified:
            return False
        if self.public != other.public:
            return False
        if self.url != other.url:
            return False
        return True

    def __hash__(self):
        return hash((self.element_texts,self.added,self.featured,self.id,self.items_count,self.modified,self.public,self.url,))

    def __iter__(self):
        return iter(self.as_tuple())

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        field_reprs.append('element_texts=' + repr(self.element_texts))
        field_reprs.append('added=' + repr(self.added))
        field_reprs.append('featured=' + repr(self.featured))
        field_reprs.append('id=' + repr(self.id))
        field_reprs.append('items_count=' + repr(self.items_count))
        field_reprs.append('modified=' + repr(self.modified))
        field_reprs.append('public=' + repr(self.public))
        field_reprs.append('url=' + "'" + self.url.encode('ascii', 'replace') + "'")
        return 'OmekaCollection(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        field_reprs.append('element_texts=' + repr(self.element_texts))
        field_reprs.append('added=' + repr(self.added))
        field_reprs.append('featured=' + repr(self.featured))
        field_reprs.append('id=' + repr(self.id))
        field_reprs.append('items_count=' + repr(self.items_count))
        field_reprs.append('modified=' + repr(self.modified))
        field_reprs.append('public=' + repr(self.public))
        field_reprs.append('url=' + "'" + self.url.encode('ascii', 'replace') + "'")
        return 'OmekaCollection(' + ', '.join(field_reprs) + ')'

    @property
    def added(self):
        '''
        :rtype: datetime
        '''

        return self.__added

    def as_dict(self):
        '''
        Return the fields of this object as a dictionary.

        :rtype: dict
        '''

        return {'element_texts': self.element_texts, 'added': self.added, 'featured': self.featured, 'id': self.id, 'items_count': self.items_count, 'modified': self.modified, 'public': self.public, 'url': self.url}

    def as_tuple(self):
        '''
        Return the fields of this object in declaration order as a tuple.

        :rtype: tuple
        '''

        return (self.element_texts, self.added, self.featured, self.id, self.items_count, self.modified, self.public, self.url,)

    @property
    def element_texts(self):
        '''
        :rtype: tuple(yomeka.api.omeka_element_text.OmekaElementText)
        '''

        return self.__element_texts

    @property
    def featured(self):
        '''
        :rtype: bool
        '''

        return self.__featured

    @property
    def id(self):  # @ReservedAssignment
        '''
        :rtype: int
        '''

        return self.__id

    @property
    def items_count(self):
        '''
        :rtype: int
        '''

        return self.__items_count

    @property
    def modified(self):
        '''
        :rtype: datetime
        '''

        return self.__modified

    @property
    def public(self):
        '''
        :rtype: bool
        '''

        return self.__public

    @classmethod
    def read(cls, iprot):
        '''
        Read a new object from the given input protocol and return the object.

        :type iprot: thryft.protocol._input_protocol._InputProtocol
        :rtype: yomeka.api.omeka_collection.OmekaCollection
        '''

        init_kwds = {}

        iprot.read_struct_begin()
        while True:
            ifield_name, ifield_type, _ifield_id = iprot.read_field_begin()
            if ifield_type == 0: # STOP
                break
            elif ifield_name == 'element_texts':
                init_kwds['element_texts'] = tuple([yomeka.api.omeka_element_text.OmekaElementText.read(iprot) for _ in xrange(iprot.read_list_begin()[1])] + (iprot.read_list_end() is None and []))
            elif ifield_name == 'added':
                init_kwds['added'] = iprot.read_date_time()
            elif ifield_name == 'featured':
                init_kwds['featured'] = iprot.read_bool()
            elif ifield_name == 'id':
                init_kwds['id'] = iprot.read_i32()
            elif ifield_name == 'items_count':
                init_kwds['items_count'] = iprot.read_i32()
            elif ifield_name == 'modified':
                init_kwds['modified'] = iprot.read_date_time()
            elif ifield_name == 'public':
                init_kwds['public'] = iprot.read_bool()
            elif ifield_name == 'url':
                init_kwds['url'] = iprot.read_string()
            iprot.read_field_end()
        iprot.read_struct_end()

        return cls(**init_kwds)

    def replace(
        self,
        element_texts=None,
        added=None,
        featured=None,
        id=None,  # @ReservedAssignment
        items_count=None,
        modified=None,
        public=None,
        url=None,
    ):
        '''
        Copy this object, replace one or more fields, and return the copy.

        :type element_texts: tuple(yomeka.api.omeka_element_text.OmekaElementText) or None
        :type added: datetime or None
        :type featured: bool or None
        :type id: int or None
        :type items_count: int or None
        :type modified: datetime or None
        :type public: bool or None
        :type url: str or None
        :rtype: yomeka.api.omeka_collection.OmekaCollection
        '''

        if element_texts is None:
            element_texts = self.element_texts
        if added is None:
            added = self.added
        if featured is None:
            featured = self.featured
        if id is None:
            id = self.id  # @ReservedAssignment
        if items_count is None:
            items_count = self.items_count
        if modified is None:
            modified = self.modified
        if public is None:
            public = self.public
        if url is None:
            url = self.url
        return self.__class__(element_texts=element_texts, added=added, featured=featured, id=id, items_count=items_count, modified=modified, public=public, url=url)

    @property
    def url(self):
        '''
        :rtype: str
        '''

        return self.__url

    def write(self, oprot):
        '''
        Write this object to the given output protocol and return self.

        :type oprot: thryft.protocol._output_protocol._OutputProtocol
        :rtype: yomeka.api.omeka_collection.OmekaCollection
        '''

        oprot.write_struct_begin('OmekaCollection')

        oprot.write_field_begin(name='element_texts', type=15, id=None)
        oprot.write_list_begin(12, len(self.element_texts))
        for _0 in self.element_texts:
            _0.write(oprot)
        oprot.write_list_end()
        oprot.write_field_end()

        oprot.write_field_begin(name='added', type=10, id=None)
        oprot.write_date_time(self.added)
        oprot.write_field_end()

        oprot.write_field_begin(name='featured', type=2, id=None)
        oprot.write_bool(self.featured)
        oprot.write_field_end()

        oprot.write_field_begin(name='id', type=8, id=None)
        oprot.write_i32(self.id)
        oprot.write_field_end()

        oprot.write_field_begin(name='items_count', type=8, id=None)
        oprot.write_i32(self.items_count)
        oprot.write_field_end()

        oprot.write_field_begin(name='modified', type=10, id=None)
        oprot.write_date_time(self.modified)
        oprot.write_field_end()

        oprot.write_field_begin(name='public', type=2, id=None)
        oprot.write_bool(self.public)
        oprot.write_field_end()

        oprot.write_field_begin(name='url', type=11, id=None)
        oprot.write_string(self.url)
        oprot.write_field_end()

        oprot.write_field_stop()

        oprot.write_struct_end()

        return self
