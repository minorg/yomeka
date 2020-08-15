import builtins
import typing


class OmekaFileUrls(object):
    class Builder(object):
        def __init__(
            self,
            original=None,
            fullsize=None,
            square_thumbnail=None,
            thumbnail=None,
        ):
            self.__original = original
            self.__fullsize = fullsize
            self.__square_thumbnail = square_thumbnail
            self.__thumbnail = thumbnail

        def build(self):
            return OmekaFileUrls(original=self.__original, fullsize=self.__fullsize, square_thumbnail=self.__square_thumbnail, thumbnail=self.__thumbnail)

        @classmethod
        def from_template(cls, template):
            '''
            :type template: yomeka.api.omeka_file_urls.OmekaFileUrls
            :rtype: yomeka.api.omeka_file_urls.OmekaFileUrls
            '''

            builder = cls()
            builder.original = template.original
            builder.fullsize = template.fullsize
            builder.square_thumbnail = template.square_thumbnail
            builder.thumbnail = template.thumbnail
            return builder

        @property
        def fullsize(self) -> typing.Optional[str]:
            return self.__fullsize

        @property
        def original(self) -> str:
            return self.__original

        def set_fullsize(self, fullsize: typing.Optional[str]):
            if fullsize is not None:
                if not isinstance(fullsize, str):
                    raise TypeError("expected fullsize to be a str but it is a %s" % builtins.type(fullsize))
            self.__fullsize = fullsize
            return self

        def set_original(self, original: str):
            if original is None:
                raise ValueError('original is required')
            if not isinstance(original, str):
                raise TypeError("expected original to be a str but it is a %s" % builtins.type(original))
            self.__original = original
            return self

        def set_square_thumbnail(self, square_thumbnail: typing.Optional[str]):
            if square_thumbnail is not None:
                if not isinstance(square_thumbnail, str):
                    raise TypeError("expected square_thumbnail to be a str but it is a %s" % builtins.type(square_thumbnail))
            self.__square_thumbnail = square_thumbnail
            return self

        def set_thumbnail(self, thumbnail: typing.Optional[str]):
            if thumbnail is not None:
                if not isinstance(thumbnail, str):
                    raise TypeError("expected thumbnail to be a str but it is a %s" % builtins.type(thumbnail))
            self.__thumbnail = thumbnail
            return self

        @property
        def square_thumbnail(self) -> typing.Optional[str]:
            return self.__square_thumbnail

        @property
        def thumbnail(self) -> typing.Optional[str]:
            return self.__thumbnail

        def update(self, omeka_file_urls):
            if isinstance(omeka_file_urls, OmekaFileUrls):
                self.set_original(omeka_file_urls.original)
                self.set_fullsize(omeka_file_urls.fullsize)
                self.set_square_thumbnail(omeka_file_urls.square_thumbnail)
                self.set_thumbnail(omeka_file_urls.thumbnail)
            elif isinstance(omeka_file_urls, dict):
                for key, value in omeka_file_urls.items():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(omeka_file_urls)
            return self

        @fullsize.setter
        def fullsize(self, fullsize: typing.Optional[str]) -> None:
            self.set_fullsize(fullsize)

        @original.setter
        def original(self, original: str) -> None:
            self.set_original(original)

        @square_thumbnail.setter
        def square_thumbnail(self, square_thumbnail: typing.Optional[str]) -> None:
            self.set_square_thumbnail(square_thumbnail)

        @thumbnail.setter
        def thumbnail(self, thumbnail: typing.Optional[str]) -> None:
            self.set_thumbnail(thumbnail)

    class FieldMetadata(object):
        ORIGINAL = None
        FULLSIZE = None
        SQUARE_THUMBNAIL = None
        THUMBNAIL = None

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
            return (cls.ORIGINAL, cls.FULLSIZE, cls.SQUARE_THUMBNAIL, cls.THUMBNAIL,)

    FieldMetadata.ORIGINAL = FieldMetadata('original', str, None)
    FieldMetadata.FULLSIZE = FieldMetadata('fullsize', str, None)
    FieldMetadata.SQUARE_THUMBNAIL = FieldMetadata('square_thumbnail', str, None)
    FieldMetadata.THUMBNAIL = FieldMetadata('thumbnail', str, None)

    def __init__(
        self,
        original: str,
        fullsize: typing.Optional[str] = None,
        square_thumbnail: typing.Optional[str] = None,
        thumbnail: typing.Optional[str] = None,
    ):
        if original is None:
            raise ValueError('original is required')
        if not isinstance(original, str):
            raise TypeError("expected original to be a str but it is a %s" % builtins.type(original))
        self.__original = original

        if fullsize is not None:
            if not isinstance(fullsize, str):
                raise TypeError("expected fullsize to be a str but it is a %s" % builtins.type(fullsize))
        self.__fullsize = fullsize

        if square_thumbnail is not None:
            if not isinstance(square_thumbnail, str):
                raise TypeError("expected square_thumbnail to be a str but it is a %s" % builtins.type(square_thumbnail))
        self.__square_thumbnail = square_thumbnail

        if thumbnail is not None:
            if not isinstance(thumbnail, str):
                raise TypeError("expected thumbnail to be a str but it is a %s" % builtins.type(thumbnail))
        self.__thumbnail = thumbnail

    def __eq__(self, other):
        if self.original != other.original:
            return False
        if self.fullsize != other.fullsize:
            return False
        if self.square_thumbnail != other.square_thumbnail:
            return False
        if self.thumbnail != other.thumbnail:
            return False
        return True

    def __hash__(self):
        return hash((self.original, self.fullsize, self.square_thumbnail, self.thumbnail,))

    def __iter__(self):
        return iter((self.original, self.fullsize, self.square_thumbnail, self.thumbnail,))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        field_reprs.append('original=' + "'" + self.original.encode('ascii', 'replace').decode('ascii') + "'")
        if self.fullsize is not None:
            field_reprs.append('fullsize=' + "'" + self.fullsize.encode('ascii', 'replace').decode('ascii') + "'")
        if self.square_thumbnail is not None:
            field_reprs.append('square_thumbnail=' + "'" + self.square_thumbnail.encode('ascii', 'replace').decode('ascii') + "'")
        if self.thumbnail is not None:
            field_reprs.append('thumbnail=' + "'" + self.thumbnail.encode('ascii', 'replace').decode('ascii') + "'")
        return 'OmekaFileUrls(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        field_reprs.append('original=' + "'" + self.original.encode('ascii', 'replace').decode('ascii') + "'")
        if self.fullsize is not None:
            field_reprs.append('fullsize=' + "'" + self.fullsize.encode('ascii', 'replace').decode('ascii') + "'")
        if self.square_thumbnail is not None:
            field_reprs.append('square_thumbnail=' + "'" + self.square_thumbnail.encode('ascii', 'replace').decode('ascii') + "'")
        if self.thumbnail is not None:
            field_reprs.append('thumbnail=' + "'" + self.thumbnail.encode('ascii', 'replace').decode('ascii') + "'")
        return 'OmekaFileUrls(' + ', '.join(field_reprs) + ')'

    @classmethod
    def builder(cls):
        return cls.Builder()

    @classmethod
    def from_builtins(cls, _dict):
        if not isinstance(_dict, dict):
            raise ValueError("expected dict")

        __builder = cls.builder()

        original = _dict.get("original")
        if original is None:
            raise KeyError("original")
        __builder.original = original

        __builder.fullsize = _dict.get("fullsize")

        __builder.square_thumbnail = _dict.get("square_thumbnail")

        __builder.thumbnail = _dict.get("thumbnail")

        return __builder.build()

    @property
    def fullsize(self) -> typing.Optional[str]:
        return self.__fullsize

    @property
    def original(self) -> str:
        return self.__original

    @classmethod
    def read(cls, iprot):
        '''
        Read a new object from the given input protocol and return the object.

        :type iprot: thryft.protocol._input_protocol._InputProtocol
        :rtype: yomeka.api.omeka_file_urls.OmekaFileUrls
        '''

        init_kwds = {}

        iprot.read_struct_begin()
        while True:
            ifield_name, ifield_type, _ifield_id = iprot.read_field_begin()
            if ifield_type == 0:  # STOP
                break
            elif ifield_name == 'original':
                init_kwds['original'] = iprot.read_string()
            elif ifield_name == 'fullsize':
                try:
                    init_kwds['fullsize'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'square_thumbnail':
                try:
                    init_kwds['square_thumbnail'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'thumbnail':
                try:
                    init_kwds['thumbnail'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            iprot.read_field_end()
        iprot.read_struct_end()

        return cls(**init_kwds)

    def replacer(self):
        return self.Builder.from_template(template=self)

    @property
    def square_thumbnail(self) -> typing.Optional[str]:
        return self.__square_thumbnail

    @property
    def thumbnail(self) -> typing.Optional[str]:
        return self.__thumbnail

    def to_builtins(self):
        dict_ = {}
        dict_["original"] = self.original
        if self.fullsize is not None:
            dict_["fullsize"] = self.fullsize
        if self.square_thumbnail is not None:
            dict_["square_thumbnail"] = self.square_thumbnail
        if self.thumbnail is not None:
            dict_["thumbnail"] = self.thumbnail
        return dict_

    def write(self, oprot):
        '''
        Write this object to the given output protocol and return self.

        :type oprot: thryft.protocol._output_protocol._OutputProtocol
        :rtype: yomeka.api.omeka_file_urls.OmekaFileUrls
        '''

        oprot.write_struct_begin('OmekaFileUrls')

        oprot.write_field_begin(name='original', type=11, id=None)
        oprot.write_string(self.original)
        oprot.write_field_end()

        if self.fullsize is not None:
            oprot.write_field_begin(name='fullsize', type=11, id=None)
            oprot.write_string(self.fullsize)
            oprot.write_field_end()

        if self.square_thumbnail is not None:
            oprot.write_field_begin(name='square_thumbnail', type=11, id=None)
            oprot.write_string(self.square_thumbnail)
            oprot.write_field_end()

        if self.thumbnail is not None:
            oprot.write_field_begin(name='thumbnail', type=11, id=None)
            oprot.write_string(self.thumbnail)
            oprot.write_field_end()

        oprot.write_field_stop()

        oprot.write_struct_end()

        return self
