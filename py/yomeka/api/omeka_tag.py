import __builtin__


class OmekaTag(object):
    class Builder(object):
        def __init__(
            self,
            id=None,  # @ReservedAssignment
            name=None,
            url=None,
        ):
            '''
            :type id: int
            :type name: str
            :type url: str
            '''

            self.__id = id
            self.__name = name
            self.__url = url

        def build(self):
            return OmekaTag(id=self.__id, name=self.__name, url=self.__url)

        @property
        def id(self):  # @ReservedAssignment
            '''
            :rtype: int
            '''

            return self.__id

        @property
        def name(self):
            '''
            :rtype: str
            '''

            return self.__name

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

        def set_name(self, name):
            '''
            :type name: str
            '''

            if name is None:
                raise ValueError('name is required')
            if not isinstance(name, basestring):
                raise TypeError("expected name to be a str but it is a %s" % getattr(__builtin__, 'type')(name))
            if len(name) < 1:
                raise ValueError("expected len(name) to be >= 1, was %d" % len(name))
            self.__name = name
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

        def update(self, omeka_tag):
            '''
            :type id: int
            :type name: str
            :type url: str
            '''

            if isinstance(omeka_tag, OmekaTag):
                self.set_id(omeka_tag.id)
                self.set_name(omeka_tag.name)
                self.set_url(omeka_tag.url)
            elif isinstance(omeka_tag, dict):
                for key, value in omeka_tag.iteritems():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(omeka_tag)
            return self

        @property
        def url(self):
            '''
            :rtype: str
            '''

            return self.__url

        @id.setter
        def id(self, id):  # @ReservedAssignment
            '''
            :type id: int
            '''

            self.set_id(id)

        @name.setter
        def name(self, name):
            '''
            :type name: str
            '''

            self.set_name(name)

        @url.setter
        def url(self, url):
            '''
            :type url: str
            '''

            self.set_url(url)

    class FieldMetadata(object):
        ID = None
        NAME = None
        URL = None

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
            return (cls.ID, cls.NAME, cls.URL,)

    FieldMetadata.ID = FieldMetadata('id', int, None)
    FieldMetadata.NAME = FieldMetadata('name', str, {u'minLength': 1})
    FieldMetadata.URL = FieldMetadata('url', str, None)

    def __init__(
        self,
        id,  # @ReservedAssignment
        name,
        url,
    ):
        '''
        :type id: int
        :type name: str
        :type url: str
        '''

        if id is None:
            raise ValueError('id is required')
        if not isinstance(id, int):
            raise TypeError("expected id to be a int but it is a %s" % getattr(__builtin__, 'type')(id))
        self.__id = id

        if name is None:
            raise ValueError('name is required')
        if not isinstance(name, basestring):
            raise TypeError("expected name to be a str but it is a %s" % getattr(__builtin__, 'type')(name))
        if len(name) < 1:
            raise ValueError("expected len(name) to be >= 1, was %d" % len(name))
        self.__name = name

        if url is None:
            raise ValueError('url is required')
        if not isinstance(url, basestring):
            raise TypeError("expected url to be a str but it is a %s" % getattr(__builtin__, 'type')(url))
        self.__url = url

    def __eq__(self, other):
        if self.id != other.id:
            return False
        if self.name != other.name:
            return False
        if self.url != other.url:
            return False
        return True

    def __hash__(self):
        return hash((self.id,self.name,self.url,))

    def __iter__(self):
        return iter((self.id, self.name, self.url,))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        field_reprs.append('id=' + repr(self.id))
        field_reprs.append('name=' + "'" + self.name.encode('ascii', 'replace') + "'")
        field_reprs.append('url=' + "'" + self.url.encode('ascii', 'replace') + "'")
        return 'OmekaTag(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        field_reprs.append('id=' + repr(self.id))
        field_reprs.append('name=' + "'" + self.name.encode('ascii', 'replace') + "'")
        field_reprs.append('url=' + "'" + self.url.encode('ascii', 'replace') + "'")
        return 'OmekaTag(' + ', '.join(field_reprs) + ')'

    @property
    def id(self):  # @ReservedAssignment
        '''
        :rtype: int
        '''

        return self.__id

    @property
    def name(self):
        '''
        :rtype: str
        '''

        return self.__name

    @classmethod
    def read(cls, iprot):
        '''
        Read a new object from the given input protocol and return the object.

        :type iprot: thryft.protocol._input_protocol._InputProtocol
        :rtype: yomeka.api.omeka_tag.OmekaTag
        '''

        init_kwds = {}

        iprot.read_struct_begin()
        while True:
            ifield_name, ifield_type, _ifield_id = iprot.read_field_begin()
            if ifield_type == 0: # STOP
                break
            elif ifield_name == 'id':
                init_kwds['id'] = iprot.read_i32()
            elif ifield_name == 'name':
                init_kwds['name'] = iprot.read_string()
            elif ifield_name == 'url':
                init_kwds['url'] = iprot.read_string()
            iprot.read_field_end()
        iprot.read_struct_end()

        return cls(**init_kwds)

    def replace(
        self,
        id=None,  # @ReservedAssignment
        name=None,
        url=None,
    ):
        '''
        Copy this object, replace one or more fields, and return the copy.

        :type id: int or None
        :type name: str or None
        :type url: str or None
        :rtype: yomeka.api.omeka_tag.OmekaTag
        '''

        if id is None:
            id = self.id  # @ReservedAssignment
        if name is None:
            name = self.name
        if url is None:
            url = self.url
        return self.__class__(id=id, name=name, url=url)

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
        :rtype: yomeka.api.omeka_tag.OmekaTag
        '''

        oprot.write_struct_begin('OmekaTag')

        oprot.write_field_begin(name='id', type=8, id=None)
        oprot.write_i32(self.id)
        oprot.write_field_end()

        oprot.write_field_begin(name='name', type=11, id=None)
        oprot.write_string(self.name)
        oprot.write_field_end()

        oprot.write_field_begin(name='url', type=11, id=None)
        oprot.write_string(self.url)
        oprot.write_field_end()

        oprot.write_field_stop()

        oprot.write_struct_end()

        return self
