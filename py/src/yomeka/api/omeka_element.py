import __builtin__


class OmekaElement(object):
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
            return OmekaElement(id=self.__id, name=self.__name, url=self.__url)

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

            self.__id = id
            return self

        def set_name(self, name):
            '''
            :type name: str
            '''

            self.__name = name
            return self

        def set_url(self, url):
            '''
            :type url: str
            '''

            self.__url = url
            return self

        def update(self, omeka_element):
            '''
            :type id: int
            :type name: str
            :type url: str
            '''

            if isinstance(omeka_element, OmekaElement):
                self.set_id(omeka_element.id)
                self.set_name(omeka_element.name)
                self.set_url(omeka_element.url)
            elif isinstance(omeka_element, dict):
                for key, value in omeka_element.iteritems():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(omeka_element)
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
        return iter(self.as_tuple())

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        field_reprs.append('id=' + repr(self.id))
        field_reprs.append('name=' + "'" + self.name.encode('ascii', 'replace') + "'")
        field_reprs.append('url=' + "'" + self.url.encode('ascii', 'replace') + "'")
        return 'OmekaElement(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        field_reprs.append('id=' + repr(self.id))
        field_reprs.append('name=' + "'" + self.name.encode('ascii', 'replace') + "'")
        field_reprs.append('url=' + "'" + self.url.encode('ascii', 'replace') + "'")
        return 'OmekaElement(' + ', '.join(field_reprs) + ')'

    def as_dict(self):
        '''
        Return the fields of this object as a dictionary.

        :rtype: dict
        '''

        return {'id': self.id, 'name': self.name, 'url': self.url}

    def as_tuple(self):
        '''
        Return the fields of this object in declaration order as a tuple.

        :rtype: tuple
        '''

        return (self.id, self.name, self.url,)

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
        :rtype: yomeka.api.omeka_element.OmekaElement
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
        :rtype: yomeka.api.omeka_element.OmekaElement
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
        :rtype: yomeka.api.omeka_element.OmekaElement
        '''

        oprot.write_struct_begin('OmekaElement')

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
