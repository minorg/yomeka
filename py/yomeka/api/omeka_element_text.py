import builtins
import yomeka.api.omeka_element
import yomeka.api.omeka_element_set


class OmekaElementText(object):
    class Builder(object):
        def __init__(
            self,
            element=None,
            element_set=None,
            html=None,
            text=None,
        ):
            self.__element = element
            self.__element_set = element_set
            self.__html = html
            self.__text = text

        def build(self):
            return OmekaElementText(element=self.__element, element_set=self.__element_set, html=self.__html, text=self.__text)

        @property
        def element(self) -> yomeka.api.omeka_element.OmekaElement:
            return self.__element

        @property
        def element_set(self) -> yomeka.api.omeka_element_set.OmekaElementSet:
            return self.__element_set

        @classmethod
        def from_template(cls, template):
            '''
            :type template: yomeka.api.omeka_element_text.OmekaElementText
            :rtype: yomeka.api.omeka_element_text.OmekaElementText
            '''

            builder = cls()
            builder.element = template.element
            builder.element_set = template.element_set
            builder.html = template.html
            builder.text = template.text
            return builder

        @property
        def html(self) -> bool:
            return self.__html

        def set_element(self, element: yomeka.api.omeka_element.OmekaElement):
            if element is None:
                raise ValueError('element is required')
            if not isinstance(element, yomeka.api.omeka_element.OmekaElement):
                raise TypeError("expected element to be a yomeka.api.omeka_element.OmekaElement but it is a %s" % builtins.type(element))
            self.__element = element
            return self

        def set_element_set(self, element_set: yomeka.api.omeka_element_set.OmekaElementSet):
            if element_set is None:
                raise ValueError('element_set is required')
            if not isinstance(element_set, yomeka.api.omeka_element_set.OmekaElementSet):
                raise TypeError("expected element_set to be a yomeka.api.omeka_element_set.OmekaElementSet but it is a %s" % builtins.type(element_set))
            self.__element_set = element_set
            return self

        def set_html(self, html: bool):
            if html is None:
                raise ValueError('html is required')
            if not isinstance(html, bool):
                raise TypeError("expected html to be a bool but it is a %s" % builtins.type(html))
            self.__html = html
            return self

        def set_text(self, text: str):
            if text is None:
                raise ValueError('text is required')
            if not isinstance(text, str):
                raise TypeError("expected text to be a str but it is a %s" % builtins.type(text))
            self.__text = text
            return self

        @property
        def text(self) -> str:
            return self.__text

        def update(self, omeka_element_text):
            if isinstance(omeka_element_text, OmekaElementText):
                self.set_element(omeka_element_text.element)
                self.set_element_set(omeka_element_text.element_set)
                self.set_html(omeka_element_text.html)
                self.set_text(omeka_element_text.text)
            elif isinstance(omeka_element_text, dict):
                for key, value in omeka_element_text.items():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(omeka_element_text)
            return self

        @element.setter
        def element(self, element: yomeka.api.omeka_element.OmekaElement) -> None:
            self.set_element(element)

        @element_set.setter
        def element_set(self, element_set: yomeka.api.omeka_element_set.OmekaElementSet) -> None:
            self.set_element_set(element_set)

        @html.setter
        def html(self, html: bool) -> None:
            self.set_html(html)

        @text.setter
        def text(self, text: str) -> None:
            self.set_text(text)

    class FieldMetadata(object):
        ELEMENT = None
        ELEMENT_SET = None
        HTML = None
        TEXT = None

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
            return (cls.ELEMENT, cls.ELEMENT_SET, cls.HTML, cls.TEXT,)

    FieldMetadata.ELEMENT = FieldMetadata('element', yomeka.api.omeka_element.OmekaElement, None)
    FieldMetadata.ELEMENT_SET = FieldMetadata('element_set', yomeka.api.omeka_element_set.OmekaElementSet, None)
    FieldMetadata.HTML = FieldMetadata('html', bool, None)
    FieldMetadata.TEXT = FieldMetadata('text', str, None)

    def __init__(
        self,
        element: yomeka.api.omeka_element.OmekaElement,
        element_set: yomeka.api.omeka_element_set.OmekaElementSet,
        html: bool,
        text: str,
    ):
        if element is None:
            raise ValueError('element is required')
        if not isinstance(element, yomeka.api.omeka_element.OmekaElement):
            raise TypeError("expected element to be a yomeka.api.omeka_element.OmekaElement but it is a %s" % builtins.type(element))
        self.__element = element

        if element_set is None:
            raise ValueError('element_set is required')
        if not isinstance(element_set, yomeka.api.omeka_element_set.OmekaElementSet):
            raise TypeError("expected element_set to be a yomeka.api.omeka_element_set.OmekaElementSet but it is a %s" % builtins.type(element_set))
        self.__element_set = element_set

        if html is None:
            raise ValueError('html is required')
        if not isinstance(html, bool):
            raise TypeError("expected html to be a bool but it is a %s" % builtins.type(html))
        self.__html = html

        if text is None:
            raise ValueError('text is required')
        if not isinstance(text, str):
            raise TypeError("expected text to be a str but it is a %s" % builtins.type(text))
        self.__text = text

    def __eq__(self, other):
        if self.element != other.element:
            return False
        if self.element_set != other.element_set:
            return False
        if self.html != other.html:
            return False
        if self.text != other.text:
            return False
        return True

    def __hash__(self):
        return hash((self.element, self.element_set, self.html, self.text,))

    def __iter__(self):
        return iter((self.element, self.element_set, self.html, self.text,))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        field_reprs.append('element=' + repr(self.element))
        field_reprs.append('element_set=' + repr(self.element_set))
        field_reprs.append('html=' + repr(self.html))
        field_reprs.append('text=' + "'" + self.text.encode('ascii', 'replace').decode('ascii') + "'")
        return 'OmekaElementText(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        field_reprs.append('element=' + repr(self.element))
        field_reprs.append('element_set=' + repr(self.element_set))
        field_reprs.append('html=' + repr(self.html))
        field_reprs.append('text=' + "'" + self.text.encode('ascii', 'replace').decode('ascii') + "'")
        return 'OmekaElementText(' + ', '.join(field_reprs) + ')'

    @classmethod
    def builder(cls):
        return cls.Builder()

    @property
    def element(self) -> yomeka.api.omeka_element.OmekaElement:
        return self.__element

    @property
    def element_set(self) -> yomeka.api.omeka_element_set.OmekaElementSet:
        return self.__element_set

    @classmethod
    def from_builtins(cls, _dict):
        if not isinstance(_dict, dict):
            raise ValueError("expected dict")

        __builder = cls.builder()

        element = _dict.get("element")
        if element is None:
            raise KeyError("element")
        element = yomeka.api.omeka_element.OmekaElement.from_builtins(element)
        __builder.element = element

        element_set = _dict.get("element_set")
        if element_set is None:
            raise KeyError("element_set")
        element_set = yomeka.api.omeka_element_set.OmekaElementSet.from_builtins(element_set)
        __builder.element_set = element_set

        html = _dict.get("html")
        if html is None:
            raise KeyError("html")
        __builder.html = html

        text = _dict.get("text")
        if text is None:
            raise KeyError("text")
        __builder.text = text

        return __builder.build()

    @property
    def html(self) -> bool:
        return self.__html

    @classmethod
    def read(cls, iprot):
        '''
        Read a new object from the given input protocol and return the object.

        :type iprot: thryft.protocol._input_protocol._InputProtocol
        :rtype: yomeka.api.omeka_element_text.OmekaElementText
        '''

        init_kwds = {}

        iprot.read_struct_begin()
        while True:
            ifield_name, ifield_type, _ifield_id = iprot.read_field_begin()
            if ifield_type == 0:  # STOP
                break
            elif ifield_name == 'element':
                init_kwds['element'] = yomeka.api.omeka_element.OmekaElement.read(iprot)
            elif ifield_name == 'element_set':
                init_kwds['element_set'] = yomeka.api.omeka_element_set.OmekaElementSet.read(iprot)
            elif ifield_name == 'html':
                init_kwds['html'] = iprot.read_bool()
            elif ifield_name == 'text':
                init_kwds['text'] = iprot.read_string()
            iprot.read_field_end()
        iprot.read_struct_end()

        return cls(**init_kwds)

    def replacer(self):
        return self.Builder.from_template(template=self)

    @property
    def text(self) -> str:
        return self.__text

    def to_builtins(self):
        dict_ = {}
        dict_["element"] = self.element.to_builtins()
        dict_["element_set"] = self.element_set.to_builtins()
        dict_["html"] = self.html
        dict_["text"] = self.text
        return dict_

    def write(self, oprot):
        '''
        Write this object to the given output protocol and return self.

        :type oprot: thryft.protocol._output_protocol._OutputProtocol
        :rtype: yomeka.api.omeka_element_text.OmekaElementText
        '''

        oprot.write_struct_begin('OmekaElementText')

        oprot.write_field_begin(name='element', type=12, id=None)
        self.element.write(oprot)
        oprot.write_field_end()

        oprot.write_field_begin(name='element_set', type=12, id=None)
        self.element_set.write(oprot)
        oprot.write_field_end()

        oprot.write_field_begin(name='html', type=2, id=None)
        oprot.write_bool(self.html)
        oprot.write_field_end()

        oprot.write_field_begin(name='text', type=11, id=None)
        oprot.write_string(self.text)
        oprot.write_field_end()

        oprot.write_field_stop()

        oprot.write_struct_end()

        return self
