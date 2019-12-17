import builtins


class IoException(Exception):
    class Builder(object):
        def __init__(
            self,
            cause_message=None,
        ):
            self.__cause_message = cause_message

        def build(self):
            return IoException(cause_message=self.__cause_message)

        @property
        def cause_message(self) -> str:
            return self.__cause_message

        @classmethod
        def from_template(cls, template):
            '''
            :type template: yomeka.api.io_exception.IoException
            :rtype: yomeka.api.io_exception.IoException
            '''

            builder = cls()
            builder.cause_message = template.cause_message
            return builder

        def set_cause_message(self, cause_message: str):
            if cause_message is None:
                raise ValueError('cause_message is required')
            if not isinstance(cause_message, str):
                raise TypeError("expected cause_message to be a str but it is a %s" % builtins.type(cause_message))
            self.__cause_message = cause_message
            return self

        def update(self, io_exception):
            if isinstance(io_exception, IoException):
                self.set_cause_message(io_exception.cause_message)
            elif isinstance(io_exception, dict):
                for key, value in io_exception.items():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(io_exception)
            return self

        @cause_message.setter
        def cause_message(self, cause_message: str) -> None:
            self.set_cause_message(cause_message)

    class FieldMetadata(object):
        CAUSE_MESSAGE = None

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
            return (cls.CAUSE_MESSAGE,)

    FieldMetadata.CAUSE_MESSAGE = FieldMetadata('cause_message', str, None)

    def __init__(
        self,
        cause_message: str,
    ):
        if cause_message is None:
            raise ValueError('cause_message is required')
        if not isinstance(cause_message, str):
            raise TypeError("expected cause_message to be a str but it is a %s" % builtins.type(cause_message))
        self.__cause_message = cause_message

    def __eq__(self, other):
        if self.cause_message != other.cause_message:
            return False
        return True

    def __hash__(self):
        return hash(self.cause_message)

    def __iter__(self):
        return iter((self.cause_message,))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        field_reprs.append('cause_message=' + "'" + self.cause_message.encode('ascii', 'replace').decode('ascii') + "'")
        return 'IoException(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        field_reprs.append('cause_message=' + "'" + self.cause_message.encode('ascii', 'replace').decode('ascii') + "'")
        return 'IoException(' + ', '.join(field_reprs) + ')'

    @classmethod
    def builder(cls):
        return cls.Builder()

    @property
    def cause_message(self) -> str:
        return self.__cause_message

    @classmethod
    def from_builtins(cls, _dict):
        if not isinstance(_dict, dict):
            raise ValueError("expected dict")

        __builder = cls.builder()

        cause_message = _dict.get("cause_message")
        if cause_message is None:
            raise KeyError("cause_message")
        __builder.cause_message = cause_message

        return __builder.build()

    @classmethod
    def read(cls, iprot):
        '''
        Read a new object from the given input protocol and return the object.

        :type iprot: thryft.protocol._input_protocol._InputProtocol
        :rtype: yomeka.api.io_exception.IoException
        '''

        init_kwds = {}

        iprot.read_struct_begin()
        while True:
            ifield_name, ifield_type, _ifield_id = iprot.read_field_begin()
            if ifield_type == 0:  # STOP
                break
            elif ifield_name == 'cause_message':
                init_kwds['cause_message'] = iprot.read_string()
            iprot.read_field_end()
        iprot.read_struct_end()

        return cls(**init_kwds)

    def replacer(self):
        return self.Builder.from_template(template=self)

    def to_builtins(self):
        dict_ = {}
        dict_["cause_message"] = self.cause_message
        return dict_

    def write(self, oprot):
        '''
        Write this object to the given output protocol and return self.

        :type oprot: thryft.protocol._output_protocol._OutputProtocol
        :rtype: yomeka.api.io_exception.IoException
        '''

        oprot.write_struct_begin('IoException')

        oprot.write_field_begin(name='cause_message', type=11, id=None)
        oprot.write_string(self.cause_message)
        oprot.write_field_end()

        oprot.write_field_stop()

        oprot.write_struct_end()

        return self
