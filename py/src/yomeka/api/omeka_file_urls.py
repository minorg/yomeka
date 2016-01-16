import __builtin__


class OmekaFileUrls(object):
    class Builder(object):
        def __init__(
            self,
            original=None,
            fullsize=None,
            square_thumbnail=None,
            thumbnail=None,
        ):
            '''
            :type original: str
            :type fullsize: str or None
            :type square_thumbnail: str or None
            :type thumbnail: str or None
            '''

            self.__original = original
            self.__fullsize = fullsize
            self.__square_thumbnail = square_thumbnail
            self.__thumbnail = thumbnail

        def build(self):
            return OmekaFileUrls(original=self.__original, fullsize=self.__fullsize, square_thumbnail=self.__square_thumbnail, thumbnail=self.__thumbnail)

        @property
        def fullsize(self):
            '''
            :rtype: str
            '''

            return self.__fullsize

        @property
        def original(self):
            '''
            :rtype: str
            '''

            return self.__original

        def set_fullsize(self, fullsize):
            '''
            :type fullsize: str or None
            '''

            self.__fullsize = fullsize
            return self

        def set_original(self, original):
            '''
            :type original: str
            '''

            self.__original = original
            return self

        def set_square_thumbnail(self, square_thumbnail):
            '''
            :type square_thumbnail: str or None
            '''

            self.__square_thumbnail = square_thumbnail
            return self

        def set_thumbnail(self, thumbnail):
            '''
            :type thumbnail: str or None
            '''

            self.__thumbnail = thumbnail
            return self

        @property
        def square_thumbnail(self):
            '''
            :rtype: str
            '''

            return self.__square_thumbnail

        @property
        def thumbnail(self):
            '''
            :rtype: str
            '''

            return self.__thumbnail

        def update(self, omeka_file_urls):
            '''
            :type original: str
            :type fullsize: str or None
            :type square_thumbnail: str or None
            :type thumbnail: str or None
            '''

            if isinstance(omeka_file_urls, OmekaFileUrls):
                self.set_original(omeka_file_urls.original)
                self.set_fullsize(omeka_file_urls.fullsize)
                self.set_square_thumbnail(omeka_file_urls.square_thumbnail)
                self.set_thumbnail(omeka_file_urls.thumbnail)
            elif isinstance(omeka_file_urls, dict):
                for key, value in omeka_file_urls.iteritems():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(omeka_file_urls)
            return self

        @fullsize.setter
        def fullsize(self, fullsize):
            '''
            :type fullsize: str or None
            '''

            self.set_fullsize(fullsize)

        @original.setter
        def original(self, original):
            '''
            :type original: str
            '''

            self.set_original(original)

        @square_thumbnail.setter
        def square_thumbnail(self, square_thumbnail):
            '''
            :type square_thumbnail: str or None
            '''

            self.set_square_thumbnail(square_thumbnail)

        @thumbnail.setter
        def thumbnail(self, thumbnail):
            '''
            :type thumbnail: str or None
            '''

            self.set_thumbnail(thumbnail)

    def __init__(
        self,
        original,
        fullsize=None,
        square_thumbnail=None,
        thumbnail=None,
    ):
        '''
        :type original: str
        :type fullsize: str or None
        :type square_thumbnail: str or None
        :type thumbnail: str or None
        '''

        if original is None:
            raise ValueError('original is required')
        if not isinstance(original, basestring):
            raise TypeError("expected original to be a str but it is a %s" % getattr(__builtin__, 'type')(original))
        self.__original = original

        if fullsize is not None:
            if not isinstance(fullsize, basestring):
                raise TypeError("expected fullsize to be a str but it is a %s" % getattr(__builtin__, 'type')(fullsize))
        self.__fullsize = fullsize

        if square_thumbnail is not None:
            if not isinstance(square_thumbnail, basestring):
                raise TypeError("expected square_thumbnail to be a str but it is a %s" % getattr(__builtin__, 'type')(square_thumbnail))
        self.__square_thumbnail = square_thumbnail

        if thumbnail is not None:
            if not isinstance(thumbnail, basestring):
                raise TypeError("expected thumbnail to be a str but it is a %s" % getattr(__builtin__, 'type')(thumbnail))
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
        return hash((self.original,self.fullsize,self.square_thumbnail,self.thumbnail,))

    def __iter__(self):
        return iter(self.as_tuple())

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        field_reprs.append('original=' + "'" + self.original.encode('ascii', 'replace') + "'")
        if self.fullsize is not None:
            field_reprs.append('fullsize=' + "'" + self.fullsize.encode('ascii', 'replace') + "'")
        if self.square_thumbnail is not None:
            field_reprs.append('square_thumbnail=' + "'" + self.square_thumbnail.encode('ascii', 'replace') + "'")
        if self.thumbnail is not None:
            field_reprs.append('thumbnail=' + "'" + self.thumbnail.encode('ascii', 'replace') + "'")
        return 'OmekaFileUrls(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        field_reprs.append('original=' + "'" + self.original.encode('ascii', 'replace') + "'")
        if self.fullsize is not None:
            field_reprs.append('fullsize=' + "'" + self.fullsize.encode('ascii', 'replace') + "'")
        if self.square_thumbnail is not None:
            field_reprs.append('square_thumbnail=' + "'" + self.square_thumbnail.encode('ascii', 'replace') + "'")
        if self.thumbnail is not None:
            field_reprs.append('thumbnail=' + "'" + self.thumbnail.encode('ascii', 'replace') + "'")
        return 'OmekaFileUrls(' + ', '.join(field_reprs) + ')'

    def as_dict(self):
        '''
        Return the fields of this object as a dictionary.

        :rtype: dict
        '''

        return {'original': self.original, 'fullsize': self.fullsize, 'square_thumbnail': self.square_thumbnail, 'thumbnail': self.thumbnail}

    def as_tuple(self):
        '''
        Return the fields of this object in declaration order as a tuple.

        :rtype: tuple
        '''

        return (self.original, self.fullsize, self.square_thumbnail, self.thumbnail,)

    @property
    def fullsize(self):
        '''
        :rtype: str
        '''

        return self.__fullsize

    @property
    def original(self):
        '''
        :rtype: str
        '''

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
            if ifield_type == 0: # STOP
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

    def replace(
        self,
        original=None,
        fullsize=None,
        square_thumbnail=None,
        thumbnail=None,
    ):
        '''
        Copy this object, replace one or more fields, and return the copy.

        :type original: str or None
        :type fullsize: str or None
        :type square_thumbnail: str or None
        :type thumbnail: str or None
        :rtype: yomeka.api.omeka_file_urls.OmekaFileUrls
        '''

        if original is None:
            original = self.original
        if fullsize is None:
            fullsize = self.fullsize
        if square_thumbnail is None:
            square_thumbnail = self.square_thumbnail
        if thumbnail is None:
            thumbnail = self.thumbnail
        return self.__class__(original=original, fullsize=fullsize, square_thumbnail=square_thumbnail, thumbnail=thumbnail)

    @property
    def square_thumbnail(self):
        '''
        :rtype: str
        '''

        return self.__square_thumbnail

    @property
    def thumbnail(self):
        '''
        :rtype: str
        '''

        return self.__thumbnail

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
