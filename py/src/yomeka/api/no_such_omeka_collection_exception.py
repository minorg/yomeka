class NoSuchOmekaCollectionException(Exception):
    class Builder(object):
        def build(self):
            return NoSuchOmekaCollectionException()

    def __eq__(self, other):
        return True

    def __iter__(self):
        return iter(self.as_tuple())

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return 'NoSuchOmekaCollectionException()'

    def __str__(self):
        return 'NoSuchOmekaCollectionException()'

    def as_dict(self):
        '''
        Return the fields of this object as a dictionary.

        :rtype: dict
        '''

        return {}

    def as_tuple(self):
        '''
        Return the fields of this object in declaration order as a tuple.

        :rtype: tuple
        '''

        return tuple()

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
