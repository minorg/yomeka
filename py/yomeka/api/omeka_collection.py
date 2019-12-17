from itertools import ifilterfalse
import __builtin__
import datetime
import yomeka.api.omeka_element_text


class OmekaCollection(object):
    class Builder(object):
        def __init__(
            self,
            added=None,
            element_texts=None,
            featured=None,
            id=None,  # @ReservedAssignment
            items_count=None,
            modified=None,
            public=None,
            url=None,
            json=None,
        ):
            '''
            :type added: datetime.datetime
            :type element_texts: tuple(yomeka.api.omeka_element_text.OmekaElementText)
            :type featured: bool
            :type id: int
            :type items_count: int
            :type modified: datetime.datetime
            :type public: bool
            :type url: str
            :type json: str or None
            '''

            self.__added = added
            self.__element_texts = element_texts
            self.__featured = featured
            self.__id = id
            self.__items_count = items_count
            self.__modified = modified
            self.__public = public
            self.__url = url
            self.__json = json

        def build(self):
            return OmekaCollection(added=self.__added, element_texts=self.__element_texts, featured=self.__featured, id=self.__id, items_count=self.__items_count, modified=self.__modified, public=self.__public, url=self.__url, json=self.__json)

        @property
        def added(self):
            '''
            :rtype: datetime.datetime
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
        def json(self):
            '''
            :rtype: str
            '''

            return self.__json

        @property
        def modified(self):
            '''
            :rtype: datetime.datetime
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
            :type added: datetime.datetime
            '''

            if added is None:
                raise ValueError('added is required')
            if not isinstance(added, datetime.datetime):
                raise TypeError("expected added to be a datetime.datetime but it is a %s" % getattr(__builtin__, 'type')(added))
            self.__added = added
            return self

        def set_element_texts(self, element_texts):
            '''
            :type element_texts: tuple(yomeka.api.omeka_element_text.OmekaElementText)
            '''

            if element_texts is None:
                raise ValueError('element_texts is required')
            if not (isinstance(element_texts, tuple) and len(list(ifilterfalse(lambda _: isinstance(_, yomeka.api.omeka_element_text.OmekaElementText), element_texts))) == 0):
                raise TypeError("expected element_texts to be a tuple(yomeka.api.omeka_element_text.OmekaElementText) but it is a %s" % getattr(__builtin__, 'type')(element_texts))
            self.__element_texts = element_texts
            return self

        def set_featured(self, featured):
            '''
            :type featured: bool
            '''

            if featured is None:
                raise ValueError('featured is required')
            if not isinstance(featured, bool):
                raise TypeError("expected featured to be a bool but it is a %s" % getattr(__builtin__, 'type')(featured))
            self.__featured = featured
            return self

        def set_id(self, id):  # @ReservedAssignment
            '''
            :type id: int
            '''

            if id is None:
                raise ValueError('id is required')
            if not isinstance(id, int):
                raise TypeError("expected id to be a int but it is a %s" % getattr(__builtin__, 'type')(id))
            self.__id = id
            return self

        def set_items_count(self, items_count):
            '''
            :type items_count: int
            '''

            if items_count is None:
                raise ValueError('items_count is required')
            if not isinstance(items_count, int):
                raise TypeError("expected items_count to be a int but it is a %s" % getattr(__builtin__, 'type')(items_count))
            self.__items_count = items_count
            return self

        def set_json(self, json):
            '''
            :type json: str or None
            '''

            if json is not None:
                if not isinstance(json, basestring):
                    raise TypeError("expected json to be a str but it is a %s" % getattr(__builtin__, 'type')(json))
                if len(json) < 1:
                    raise ValueError("expected len(json) to be >= 1, was %d" % len(json))
            self.__json = json
            return self

        def set_modified(self, modified):
            '''
            :type modified: datetime.datetime
            '''

            if modified is None:
                raise ValueError('modified is required')
            if not isinstance(modified, datetime.datetime):
                raise TypeError("expected modified to be a datetime.datetime but it is a %s" % getattr(__builtin__, 'type')(modified))
            self.__modified = modified
            return self

        def set_public(self, public):
            '''
            :type public: bool
            '''

            if public is None:
                raise ValueError('public is required')
            if not isinstance(public, bool):
                raise TypeError("expected public to be a bool but it is a %s" % getattr(__builtin__, 'type')(public))
            self.__public = public
            return self

        def set_url(self, url):
            '''
            :type url: str
            '''

            if url is None:
                raise ValueError('url is required')
            if not isinstance(url, basestring):
                raise TypeError("expected url to be a str but it is a %s" % getattr(__builtin__, 'type')(url))
            self.__url = url
            return self

        def update(self, omeka_collection):
            '''
            :type added: datetime.datetime
            :type element_texts: tuple(yomeka.api.omeka_element_text.OmekaElementText)
            :type featured: bool
            :type id: int
            :type items_count: int
            :type modified: datetime.datetime
            :type public: bool
            :type url: str
            :type json: str or None
            '''

            if isinstance(omeka_collection, OmekaCollection):
                self.set_added(omeka_collection.added)
                self.set_element_texts(omeka_collection.element_texts)
                self.set_featured(omeka_collection.featured)
                self.set_id(omeka_collection.id)
                self.set_items_count(omeka_collection.items_count)
                self.set_modified(omeka_collection.modified)
                self.set_public(omeka_collection.public)
                self.set_url(omeka_collection.url)
                self.set_json(omeka_collection.json)
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
            :type added: datetime.datetime
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

        @json.setter
        def json(self, json):
            '''
            :type json: str or None
            '''

            self.set_json(json)

        @modified.setter
        def modified(self, modified):
            '''
            :type modified: datetime.datetime
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

    class FieldMetadata(object):
        ADDED = None
        ELEMENT_TEXTS = None
        FEATURED = None
        ID = None
        ITEMS_COUNT = None
        MODIFIED = None
        PUBLIC = None
        URL = None
        JSON = None

        def __init__(self, name, type_, validation):
            object.__init__(self)
            self.__name = name
            self.__type = type_
            self.__validation = validation

        @property
        def name(self):
            return self.__name

        def __repr__(self):
            return self.__name

        def __str__(self):
            return self.__name

        @property
        def type(self):
            return self.__type

        @property
        def validation(self):
            return self.__validation

        @classmethod
        def values(cls):
            return (cls.ADDED, cls.ELEMENT_TEXTS, cls.FEATURED, cls.ID, cls.ITEMS_COUNT, cls.MODIFIED, cls.PUBLIC, cls.URL, cls.JSON,)

    FieldMetadata.ADDED = FieldMetadata('added', datetime.datetime, None)
    FieldMetadata.ELEMENT_TEXTS = FieldMetadata('element_texts', tuple, None)
    FieldMetadata.FEATURED = FieldMetadata('featured', bool, None)
    FieldMetadata.ID = FieldMetadata('id', int, None)
    FieldMetadata.ITEMS_COUNT = FieldMetadata('items_count', int, None)
    FieldMetadata.MODIFIED = FieldMetadata('modified', datetime.datetime, None)
    FieldMetadata.PUBLIC = FieldMetadata('public', bool, None)
    FieldMetadata.URL = FieldMetadata('url', str, None)
    FieldMetadata.JSON = FieldMetadata('json', str, {u'minLength': 1})

    def __init__(
        self,
        added,
        element_texts,
        featured,
        id,  # @ReservedAssignment
        items_count,
        modified,
        public,
        url,
        json=None,
    ):
        '''
        :type added: datetime.datetime
        :type element_texts: tuple(yomeka.api.omeka_element_text.OmekaElementText)
        :type featured: bool
        :type id: int
        :type items_count: int
        :type modified: datetime.datetime
        :type public: bool
        :type url: str
        :type json: str or None
        '''

        if added is None:
            raise ValueError('added is required')
        if not isinstance(added, datetime.datetime):
            raise TypeError("expected added to be a datetime.datetime but it is a %s" % getattr(__builtin__, 'type')(added))
        self.__added = added

        if element_texts is None:
            raise ValueError('element_texts is required')
        if not (isinstance(element_texts, tuple) and len(list(ifilterfalse(lambda _: isinstance(_, yomeka.api.omeka_element_text.OmekaElementText), element_texts))) == 0):
            raise TypeError("expected element_texts to be a tuple(yomeka.api.omeka_element_text.OmekaElementText) but it is a %s" % getattr(__builtin__, 'type')(element_texts))
        self.__element_texts = element_texts

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
        if not isinstance(modified, datetime.datetime):
            raise TypeError("expected modified to be a datetime.datetime but it is a %s" % getattr(__builtin__, 'type')(modified))
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

        if json is not None:
            if not isinstance(json, basestring):
                raise TypeError("expected json to be a str but it is a %s" % getattr(__builtin__, 'type')(json))
            if len(json) < 1:
                raise ValueError("expected len(json) to be >= 1, was %d" % len(json))
        self.__json = json

    def __eq__(self, other):
        if self.added != other.added:
            return False
        if self.element_texts != other.element_texts:
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
        if self.json != other.json:
            return False
        return True

    def __hash__(self):
        return hash((self.added,self.element_texts,self.featured,self.id,self.items_count,self.modified,self.public,self.url,self.json,))

    def __iter__(self):
        return iter((self.added, self.element_texts, self.featured, self.id, self.items_count, self.modified, self.public, self.url, self.json,))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        field_reprs.append('added=' + repr(self.added))
        field_reprs.append('element_texts=' + repr(self.element_texts))
        field_reprs.append('featured=' + repr(self.featured))
        field_reprs.append('id=' + repr(self.id))
        field_reprs.append('items_count=' + repr(self.items_count))
        field_reprs.append('modified=' + repr(self.modified))
        field_reprs.append('public=' + repr(self.public))
        field_reprs.append('url=' + "'" + self.url.encode('ascii', 'replace') + "'")
        if self.json is not None:
            field_reprs.append('json=' + "'" + self.json.encode('ascii', 'replace') + "'")
        return 'OmekaCollection(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        field_reprs.append('added=' + repr(self.added))
        field_reprs.append('element_texts=' + repr(self.element_texts))
        field_reprs.append('featured=' + repr(self.featured))
        field_reprs.append('id=' + repr(self.id))
        field_reprs.append('items_count=' + repr(self.items_count))
        field_reprs.append('modified=' + repr(self.modified))
        field_reprs.append('public=' + repr(self.public))
        field_reprs.append('url=' + "'" + self.url.encode('ascii', 'replace') + "'")
        if self.json is not None:
            field_reprs.append('json=' + "'" + self.json.encode('ascii', 'replace') + "'")
        return 'OmekaCollection(' + ', '.join(field_reprs) + ')'

    @property
    def added(self):
        '''
        :rtype: datetime.datetime
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
    def json(self):
        '''
        :rtype: str
        '''

        return self.__json

    @property
    def modified(self):
        '''
        :rtype: datetime.datetime
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
            elif ifield_name == 'added':
                init_kwds['added'] = iprot.read_date_time()
            elif ifield_name == 'element_texts':
                init_kwds['element_texts'] = tuple([yomeka.api.omeka_element_text.OmekaElementText.read(iprot) for _ in xrange(iprot.read_list_begin()[1])] + (iprot.read_list_end() is None and []))
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
            elif ifield_name == 'json':
                try:
                    init_kwds['json'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            iprot.read_field_end()
        iprot.read_struct_end()

        return cls(**init_kwds)

    def replace(
        self,
        added=None,
        element_texts=None,
        featured=None,
        id=None,  # @ReservedAssignment
        items_count=None,
        modified=None,
        public=None,
        url=None,
        json=None,
    ):
        '''
        Copy this object, replace one or more fields, and return the copy.

        :type added: datetime.datetime or None
        :type element_texts: tuple(yomeka.api.omeka_element_text.OmekaElementText) or None
        :type featured: bool or None
        :type id: int or None
        :type items_count: int or None
        :type modified: datetime.datetime or None
        :type public: bool or None
        :type url: str or None
        :type json: str or None
        :rtype: yomeka.api.omeka_collection.OmekaCollection
        '''

        if added is None:
            added = self.added
        if element_texts is None:
            element_texts = self.element_texts
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
        if json is None:
            json = self.json
        return self.__class__(added=added, element_texts=element_texts, featured=featured, id=id, items_count=items_count, modified=modified, public=public, url=url, json=json)

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

        oprot.write_field_begin(name='added', type=10, id=None)
        oprot.write_date_time(self.added)
        oprot.write_field_end()

        oprot.write_field_begin(name='element_texts', type=15, id=None)
        oprot.write_list_begin(12, len(self.element_texts))
        for _0 in self.element_texts:
            _0.write(oprot)
        oprot.write_list_end()
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

        if self.json is not None:
            oprot.write_field_begin(name='json', type=11, id=None)
            oprot.write_string(self.json)
            oprot.write_field_end()

        oprot.write_field_stop()

        oprot.write_struct_end()

        return self
