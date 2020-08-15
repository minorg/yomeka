class NoSuchOmekaCollectionException(Exception):
    class Builder(object):
        def build(self):
            return NoSuchOmekaCollectionException()

        @classmethod
        def from_template(cls, template):
            '''
            :type template: yomeka.api.no_such_omeka_collection_exception.NoSuchOmekaCollectionException
            :rtype: yomeka.api.no_such_omeka_collection_exception.NoSuchOmekaCollectionException
            '''

            builder = cls()

            return builder

    def __eq__(self, other):
        return True

    def __iter__(self):
        return iter(tuple())

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return 'NoSuchOmekaCollectionException()'

    def __str__(self):
        return 'NoSuchOmekaCollectionException()'

    @classmethod
    def builder(cls):
        return cls.Builder()

    @classmethod
    def from_builtins(cls, _dict):
        if not isinstance(_dict, dict):
            raise ValueError("expected dict")

        __builder = cls.builder()



        return __builder.build()

    @classmethod
    def read(cls, iprot):
        '''
        Read a new object from the given input protocol and return the object.

        :type iprot: thryft.protocol._input_protocol._InputProtocol
        :rtype: yomeka.api.no_such_omeka_collection_exception.NoSuchOmekaCollectionException
        '''

        iprot.read_struct_begin()
        iprot.read_struct_end()
        return cls()

    def replacer(self):
        return self.Builder.from_template(template=self)

    def to_builtins(self):
        dict_ = {}

        return dict_

    def write(self, oprot):
        '''
        Write this object to the given output protocol and return self.

        :type oprot: thryft.protocol._output_protocol._OutputProtocol
        :rtype: yomeka.api.no_such_omeka_collection_exception.NoSuchOmekaCollectionException
        '''

        oprot.write_struct_begin('NoSuchOmekaCollectionException')

        oprot.write_field_stop()

        oprot.write_struct_end()

        return self
