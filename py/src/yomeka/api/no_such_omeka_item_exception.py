class NoSuchOmekaItemException(Exception):
    class Builder(object):
        def build(self):
            return NoSuchOmekaItemException()

    def __eq__(self, other):
        return True

    def __iter__(self):
        return iter(tuple())

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return 'NoSuchOmekaItemException()'

    def __str__(self):
        return 'NoSuchOmekaItemException()'

    @classmethod
    def read(cls, iprot):
        '''
        Read a new object from the given input protocol and return the object.

        :type iprot: thryft.protocol._input_protocol._InputProtocol
        :rtype: yomeka.api.no_such_omeka_item_exception.NoSuchOmekaItemException
        '''

        iprot.read_struct_begin()
        iprot.read_struct_end()
        return cls()

    def write(self, oprot):
        '''
        Write this object to the given output protocol and return self.

        :type oprot: thryft.protocol._output_protocol._OutputProtocol
        :rtype: yomeka.api.no_such_omeka_item_exception.NoSuchOmekaItemException
        '''

        oprot.write_struct_begin('NoSuchOmekaItemException')

        oprot.write_field_stop()

        oprot.write_struct_end()

        return self
