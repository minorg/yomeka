from datetime import datetime
from itertools import ifilterfalse
import __builtin__
import yomeka.api.omeka_element_text
import yomeka.api.omeka_item_type
import yomeka.api.omeka_tag


class OmekaItem(object):
    class Builder(object):
        def __init__(
            self,
            added=None,
            element_texts=None,
            featured=None,
            id=None,  # @ReservedAssignment
            modified=None,
            public=None,
            tags=None,
            url=None,
            item_type=None,
            json=None,
        ):
            '''
            :type added: datetime
            :type element_texts: tuple(yomeka.api.omeka_element_text.OmekaElementText)
            :type featured: bool
            :type id: int
            :type modified: datetime
            :type public: bool
            :type tags: tuple(yomeka.api.omeka_tag.OmekaTag)
            :type url: str
            :type item_type: yomeka.api.omeka_item_type.OmekaItemType or None
            :type json: str or None
            '''

            self.__added = added
            self.__element_texts = element_texts
            self.__featured = featured
            self.__id = id
            self.__modified = modified
            self.__public = public
            self.__tags = tags
            self.__url = url
            self.__item_type = item_type
            self.__json = json

        def build(self):
            return OmekaItem(added=self.__added, element_texts=self.__element_texts, featured=self.__featured, id=self.__id, modified=self.__modified, public=self.__public, tags=self.__tags, url=self.__url, item_type=self.__item_type, json=self.__json)

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
        def item_type(self):
            '''
            :rtype: yomeka.api.omeka_item_type.OmekaItemType
            '''

            return self.__item_type

        @property
        def json(self):
            '''
            :rtype: str
            '''

            return self.__json

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

        def set_item_type(self, item_type):
            '''
            :type item_type: yomeka.api.omeka_item_type.OmekaItemType or None
            '''

            self.__item_type = item_type
            return self

        def set_json(self, json):
            '''
            :type json: str or None
            '''

            self.__json = json
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

        def set_tags(self, tags):
            '''
            :type tags: tuple(yomeka.api.omeka_tag.OmekaTag)
            '''

            self.__tags = tags
            return self

        def set_url(self, url):
            '''
            :type url: str
            '''

            self.__url = url
            return self

        @property
        def tags(self):
            '''
            :rtype: tuple(yomeka.api.omeka_tag.OmekaTag)
            '''

            return self.__tags

        def update(self, omeka_item):
            '''
            :type added: datetime
            :type element_texts: tuple(yomeka.api.omeka_element_text.OmekaElementText)
            :type featured: bool
            :type id: int
            :type modified: datetime
            :type public: bool
            :type tags: tuple(yomeka.api.omeka_tag.OmekaTag)
            :type url: str
            :type item_type: yomeka.api.omeka_item_type.OmekaItemType or None
            :type json: str or None
            '''

            if isinstance(omeka_item, OmekaItem):
                self.set_added(omeka_item.added)
                self.set_element_texts(omeka_item.element_texts)
                self.set_featured(omeka_item.featured)
                self.set_id(omeka_item.id)
                self.set_modified(omeka_item.modified)
                self.set_public(omeka_item.public)
                self.set_tags(omeka_item.tags)
                self.set_url(omeka_item.url)
                self.set_item_type(omeka_item.item_type)
                self.set_json(omeka_item.json)
            elif isinstance(omeka_item, dict):
                for key, value in omeka_item.iteritems():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(omeka_item)
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

        @item_type.setter
        def item_type(self, item_type):
            '''
            :type item_type: yomeka.api.omeka_item_type.OmekaItemType or None
            '''

            self.set_item_type(item_type)

        @json.setter
        def json(self, json):
            '''
            :type json: str or None
            '''

            self.set_json(json)

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

        @tags.setter
        def tags(self, tags):
            '''
            :type tags: tuple(yomeka.api.omeka_tag.OmekaTag)
            '''

            self.set_tags(tags)

        @url.setter
        def url(self, url):
            '''
            :type url: str
            '''

            self.set_url(url)

    def __init__(
        self,
        added,
        element_texts,
        featured,
        id,  # @ReservedAssignment
        modified,
        public,
        tags,
        url,
        item_type=None,
        json=None,
    ):
        '''
        :type added: datetime
        :type element_texts: tuple(yomeka.api.omeka_element_text.OmekaElementText)
        :type featured: bool
        :type id: int
        :type modified: datetime
        :type public: bool
        :type tags: tuple(yomeka.api.omeka_tag.OmekaTag)
        :type url: str
        :type item_type: yomeka.api.omeka_item_type.OmekaItemType or None
        :type json: str or None
        '''

        if added is None:
            raise ValueError('added is required')
        if not isinstance(added, datetime):
            raise TypeError("expected added to be a datetime but it is a %s" % getattr(__builtin__, 'type')(added))
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

        if tags is None:
            raise ValueError('tags is required')
        if not (isinstance(tags, tuple) and len(list(ifilterfalse(lambda _: isinstance(_, yomeka.api.omeka_tag.OmekaTag), tags))) == 0):
            raise TypeError("expected tags to be a tuple(yomeka.api.omeka_tag.OmekaTag) but it is a %s" % getattr(__builtin__, 'type')(tags))
        self.__tags = tags

        if url is None:
            raise ValueError('url is required')
        if not isinstance(url, basestring):
            raise TypeError("expected url to be a str but it is a %s" % getattr(__builtin__, 'type')(url))
        self.__url = url

        if item_type is not None:
            if not isinstance(item_type, yomeka.api.omeka_item_type.OmekaItemType):
                raise TypeError("expected item_type to be a yomeka.api.omeka_item_type.OmekaItemType but it is a %s" % getattr(__builtin__, 'type')(item_type))
        self.__item_type = item_type

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
        if self.modified != other.modified:
            return False
        if self.public != other.public:
            return False
        if self.tags != other.tags:
            return False
        if self.url != other.url:
            return False
        if self.item_type != other.item_type:
            return False
        if self.json != other.json:
            return False
        return True

    def __hash__(self):
        return hash((self.added,self.element_texts,self.featured,self.id,self.modified,self.public,self.tags,self.url,self.item_type,self.json,))

    def __iter__(self):
        return iter(self.as_tuple())

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        field_reprs.append('added=' + repr(self.added))
        field_reprs.append('element_texts=' + repr(self.element_texts))
        field_reprs.append('featured=' + repr(self.featured))
        field_reprs.append('id=' + repr(self.id))
        field_reprs.append('modified=' + repr(self.modified))
        field_reprs.append('public=' + repr(self.public))
        field_reprs.append('tags=' + repr(self.tags))
        field_reprs.append('url=' + "'" + self.url.encode('ascii', 'replace') + "'")
        if self.item_type is not None:
            field_reprs.append('item_type=' + repr(self.item_type))
        if self.json is not None:
            field_reprs.append('json=' + "'" + self.json.encode('ascii', 'replace') + "'")
        return 'OmekaItem(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        field_reprs.append('added=' + repr(self.added))
        field_reprs.append('element_texts=' + repr(self.element_texts))
        field_reprs.append('featured=' + repr(self.featured))
        field_reprs.append('id=' + repr(self.id))
        field_reprs.append('modified=' + repr(self.modified))
        field_reprs.append('public=' + repr(self.public))
        field_reprs.append('tags=' + repr(self.tags))
        field_reprs.append('url=' + "'" + self.url.encode('ascii', 'replace') + "'")
        if self.item_type is not None:
            field_reprs.append('item_type=' + repr(self.item_type))
        if self.json is not None:
            field_reprs.append('json=' + "'" + self.json.encode('ascii', 'replace') + "'")
        return 'OmekaItem(' + ', '.join(field_reprs) + ')'

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

        return {'added': self.added, 'element_texts': self.element_texts, 'featured': self.featured, 'id': self.id, 'modified': self.modified, 'public': self.public, 'tags': self.tags, 'url': self.url, 'item_type': self.item_type, 'json': self.json}

    def as_tuple(self):
        '''
        Return the fields of this object in declaration order as a tuple.

        :rtype: tuple
        '''

        return (self.added, self.element_texts, self.featured, self.id, self.modified, self.public, self.tags, self.url, self.item_type, self.json,)

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
    def item_type(self):
        '''
        :rtype: yomeka.api.omeka_item_type.OmekaItemType
        '''

        return self.__item_type

    @property
    def json(self):
        '''
        :rtype: str
        '''

        return self.__json

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
        :rtype: yomeka.api.omeka_item.OmekaItem
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
            elif ifield_name == 'modified':
                init_kwds['modified'] = iprot.read_date_time()
            elif ifield_name == 'public':
                init_kwds['public'] = iprot.read_bool()
            elif ifield_name == 'tags':
                init_kwds['tags'] = tuple([yomeka.api.omeka_tag.OmekaTag.read(iprot) for _ in xrange(iprot.read_list_begin()[1])] + (iprot.read_list_end() is None and []))
            elif ifield_name == 'url':
                init_kwds['url'] = iprot.read_string()
            elif ifield_name == 'item_type':
                init_kwds['item_type'] = yomeka.api.omeka_item_type.OmekaItemType.read(iprot)
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
        modified=None,
        public=None,
        tags=None,
        url=None,
        item_type=None,
        json=None,
    ):
        '''
        Copy this object, replace one or more fields, and return the copy.

        :type added: datetime or None
        :type element_texts: tuple(yomeka.api.omeka_element_text.OmekaElementText) or None
        :type featured: bool or None
        :type id: int or None
        :type modified: datetime or None
        :type public: bool or None
        :type tags: tuple(yomeka.api.omeka_tag.OmekaTag) or None
        :type url: str or None
        :type item_type: yomeka.api.omeka_item_type.OmekaItemType or None
        :type json: str or None
        :rtype: yomeka.api.omeka_item.OmekaItem
        '''

        if added is None:
            added = self.added
        if element_texts is None:
            element_texts = self.element_texts
        if featured is None:
            featured = self.featured
        if id is None:
            id = self.id  # @ReservedAssignment
        if modified is None:
            modified = self.modified
        if public is None:
            public = self.public
        if tags is None:
            tags = self.tags
        if url is None:
            url = self.url
        if item_type is None:
            item_type = self.item_type
        if json is None:
            json = self.json
        return self.__class__(added=added, element_texts=element_texts, featured=featured, id=id, modified=modified, public=public, tags=tags, url=url, item_type=item_type, json=json)

    @property
    def tags(self):
        '''
        :rtype: tuple(yomeka.api.omeka_tag.OmekaTag)
        '''

        return self.__tags

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
        :rtype: yomeka.api.omeka_item.OmekaItem
        '''

        oprot.write_struct_begin('OmekaItem')

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

        oprot.write_field_begin(name='modified', type=10, id=None)
        oprot.write_date_time(self.modified)
        oprot.write_field_end()

        oprot.write_field_begin(name='public', type=2, id=None)
        oprot.write_bool(self.public)
        oprot.write_field_end()

        oprot.write_field_begin(name='tags', type=15, id=None)
        oprot.write_list_begin(12, len(self.tags))
        for _0 in self.tags:
            _0.write(oprot)
        oprot.write_list_end()
        oprot.write_field_end()

        oprot.write_field_begin(name='url', type=11, id=None)
        oprot.write_string(self.url)
        oprot.write_field_end()

        if self.item_type is not None:
            oprot.write_field_begin(name='item_type', type=12, id=None)
            self.item_type.write(oprot)
            oprot.write_field_end()

        if self.json is not None:
            oprot.write_field_begin(name='json', type=11, id=None)
            oprot.write_string(self.json)
            oprot.write_field_end()

        oprot.write_field_stop()

        oprot.write_struct_end()

        return self
