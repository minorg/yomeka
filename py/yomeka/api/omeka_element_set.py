import builtins


class OmekaElementSet(object):
    class Builder(object):
        def __init__(
            self,
            id=None,  # @ReservedAssignment
            name=None,
            url=None,
        ):
            self.__id = id
            self.__name = name
            self.__url = url

        def build(self):
            return OmekaElementSet(id=self.__id, name=self.__name, url=self.__url)

        @classmethod
        def from_template(cls, template):
            '''
            :type template: yomeka.api.omeka_element_set.OmekaElementSet
            :rtype: yomeka.api.omeka_element_set.OmekaElementSet
            '''

            builder = cls()
            builder.id = template.id
            builder.name = template.name
            builder.url = template.url
            return builder

        @property
        def id(self) -> int:  # @ReservedAssignment
            return self.__id

        @property
        def name(self) -> str:
            return self.__name

        def set_id(self, id: int):  # @ReservedAssignment
            if id is None:
                raise ValueError('id is required')
            if not isinstance(id, int):
                raise TypeError("expected id to be a int but it is a %s" % builtins.type(id))
            self.__id = id
            return self

        def set_name(self, name: str):
            if name is None:
                raise ValueError('name is required')
            if not isinstance(name, str):
                raise TypeError("expected name to be a str but it is a %s" % builtins.type(name))
            if len(name) < 1:
                raise ValueError("expected len(name) to be >= 1, was %d" % len(name))
            self.__name = name
            return self

        def set_url(self, url: str):
            if url is None:
                raise ValueError('url is required')
            if not isinstance(url, str):
                raise TypeError("expected url to be a str but it is a %s" % builtins.type(url))
            self.__url = url
            return self

        def update(self, omeka_element_set):
            if isinstance(omeka_element_set, OmekaElementSet):
                self.set_id(omeka_element_set.id)
                self.set_name(omeka_element_set.name)
                self.set_url(omeka_element_set.url)
            elif isinstance(omeka_element_set, dict):
                for key, value in omeka_element_set.items():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(omeka_element_set)
            return self

        @property
        def url(self) -> str:
            return self.__url

        @id.setter
        def id(self, id: int) -> None:  # @ReservedAssignment
            self.set_id(id)

        @name.setter
        def name(self, name: str) -> None:
            self.set_name(name)

        @url.setter
        def url(self, url: str) -> None:
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
    FieldMetadata.NAME = FieldMetadata('name', str, {'minLength': 1})
    FieldMetadata.URL = FieldMetadata('url', str, None)

    def __init__(
        self,
        id: int,  # @ReservedAssignment
        name: str,
        url: str,
    ):
        if id is None:
            raise ValueError('id is required')
        if not isinstance(id, int):
            raise TypeError("expected id to be a int but it is a %s" % builtins.type(id))
        self.__id = id

        if name is None:
            raise ValueError('name is required')
        if not isinstance(name, str):
            raise TypeError("expected name to be a str but it is a %s" % builtins.type(name))
        if len(name) < 1:
            raise ValueError("expected len(name) to be >= 1, was %d" % len(name))
        self.__name = name

        if url is None:
            raise ValueError('url is required')
        if not isinstance(url, str):
            raise TypeError("expected url to be a str but it is a %s" % builtins.type(url))
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
        return hash((self.id, self.name, self.url,))

    def __iter__(self):
        return iter((self.id, self.name, self.url,))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        field_reprs.append('id=' + repr(self.id))
        field_reprs.append('name=' + "'" + self.name.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('url=' + "'" + self.url.encode('ascii', 'replace').decode('ascii') + "'")
        return 'OmekaElementSet(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        field_reprs.append('id=' + repr(self.id))
        field_reprs.append('name=' + "'" + self.name.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('url=' + "'" + self.url.encode('ascii', 'replace').decode('ascii') + "'")
        return 'OmekaElementSet(' + ', '.join(field_reprs) + ')'

    @classmethod
    def builder(cls):
        return cls.Builder()

    @classmethod
    def from_builtins(cls, _dict):
        if not isinstance(_dict, dict):
            raise ValueError("expected dict")

        __builder = cls.builder()

        id = _dict.get("id")
        if id is None:
            raise KeyError("id")
        __builder.id = id

        name = _dict.get("name")
        if name is None:
            raise KeyError("name")
        __builder.name = name

        url = _dict.get("url")
        if url is None:
            raise KeyError("url")
        __builder.url = url

        return __builder.build()

    @property
    def id(self) -> int:  # @ReservedAssignment
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @classmethod
    def read(cls, iprot):
        '''
        Read a new object from the given input protocol and return the object.

        :type iprot: thryft.protocol._input_protocol._InputProtocol
        :rtype: yomeka.api.omeka_element_set.OmekaElementSet
        '''

        init_kwds = {}

        iprot.read_struct_begin()
        while True:
            ifield_name, ifield_type, _ifield_id = iprot.read_field_begin()
            if ifield_type == 0:  # STOP
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

    def replacer(self):
        return self.Builder.from_template(template=self)

    def to_builtins(self):
        dict_ = {}
        dict_["id"] = self.id
        dict_["name"] = self.name
        dict_["url"] = self.url
        return dict_

    @property
    def url(self) -> str:
        return self.__url

    def write(self, oprot):
        '''
        Write this object to the given output protocol and return self.

        :type oprot: thryft.protocol._output_protocol._OutputProtocol
        :rtype: yomeka.api.omeka_element_set.OmekaElementSet
        '''

        oprot.write_struct_begin('OmekaElementSet')

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
