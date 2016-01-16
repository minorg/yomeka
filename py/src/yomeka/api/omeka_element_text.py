import __builtin__
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
            '''
            :type element: yomeka.api.omeka_element.OmekaElement
            :type element_set: yomeka.api.omeka_element_set.OmekaElementSet
            :type html: bool
            :type text: str
            '''

            self.__element = element
            self.__element_set = element_set
            self.__html = html
            self.__text = text

        def build(self):
            return OmekaElementText(element=self.__element, element_set=self.__element_set, html=self.__html, text=self.__text)

        @property
        def element(self):
            '''
            :rtype: yomeka.api.omeka_element.OmekaElement
            '''

            return self.__element

        @property
        def element_set(self):
            '''
            :rtype: yomeka.api.omeka_element_set.OmekaElementSet
            '''

            return self.__element_set

        @property
        def html(self):
            '''
            :rtype: bool
            '''

            return self.__html

        def set_element(self, element):
            '''
            :type element: yomeka.api.omeka_element.OmekaElement
            '''

            self.__element = element
            return self

        def set_element_set(self, element_set):
            '''
            :type element_set: yomeka.api.omeka_element_set.OmekaElementSet
            '''

            self.__element_set = element_set
            return self

        def set_html(self, html):
            '''
            :type html: bool
            '''

            self.__html = html
            return self

        def set_text(self, text):
            '''
            :type text: str
            '''

            self.__text = text
            return self

        @property
        def text(self):
            '''
            :rtype: str
            '''

            return self.__text

        def update(self, omeka_element_text):
            '''
            :type element: yomeka.api.omeka_element.OmekaElement
            :type element_set: yomeka.api.omeka_element_set.OmekaElementSet
            :type html: bool
            :type text: str
            '''

            if isinstance(omeka_element_text, OmekaElementText):
                self.set_element(omeka_element_text.element)
                self.set_element_set(omeka_element_text.element_set)
                self.set_html(omeka_element_text.html)
                self.set_text(omeka_element_text.text)
            elif isinstance(omeka_element_text, dict):
                for key, value in omeka_element_text.iteritems():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(omeka_element_text)
            return self

        @element.setter
        def element(self, element):
            '''
            :type element: yomeka.api.omeka_element.OmekaElement
            '''

            self.set_element(element)

        @element_set.setter
        def element_set(self, element_set):
            '''
            :type element_set: yomeka.api.omeka_element_set.OmekaElementSet
            '''

            self.set_element_set(element_set)

        @html.setter
        def html(self, html):
            '''
            :type html: bool
            '''

            self.set_html(html)

        @text.setter
        def text(self, text):
            '''
            :type text: str
            '''

            self.set_text(text)

    def __init__(
        self,
        element,
        element_set,
        html,
        text,
    ):
        '''
        :type element: yomeka.api.omeka_element.OmekaElement
        :type element_set: yomeka.api.omeka_element_set.OmekaElementSet
        :type html: bool
        :type text: str
        '''

        if element is None:
            raise ValueError('element is required')
        if not isinstance(element, yomeka.api.omeka_element.OmekaElement):
            raise TypeError("expected element to be a yomeka.api.omeka_element.OmekaElement but it is a %s" % getattr(__builtin__, 'type')(element))
        self.__element = element

        if element_set is None:
            raise ValueError('element_set is required')
        if not isinstance(element_set, yomeka.api.omeka_element_set.OmekaElementSet):
            raise TypeError("expected element_set to be a yomeka.api.omeka_element_set.OmekaElementSet but it is a %s" % getattr(__builtin__, 'type')(element_set))
        self.__element_set = element_set

        if html is None:
            raise ValueError('html is required')
        if not isinstance(html, bool):
            raise TypeError("expected html to be a bool but it is a %s" % getattr(__builtin__, 'type')(html))
        self.__html = html

        if text is None:
            raise ValueError('text is required')
        if not isinstance(text, basestring):
            raise TypeError("expected text to be a str but it is a %s" % getattr(__builtin__, 'type')(text))
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
        return hash((self.element,self.element_set,self.html,self.text,))

    def __iter__(self):
        return iter(self.as_tuple())

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        field_reprs.append('element=' + repr(self.element))
        field_reprs.append('element_set=' + repr(self.element_set))
        field_reprs.append('html=' + repr(self.html))
        field_reprs.append('text=' + "'" + self.text.encode('ascii', 'replace') + "'")
        return 'OmekaElementText(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        field_reprs.append('element=' + repr(self.element))
        field_reprs.append('element_set=' + repr(self.element_set))
        field_reprs.append('html=' + repr(self.html))
        field_reprs.append('text=' + "'" + self.text.encode('ascii', 'replace') + "'")
        return 'OmekaElementText(' + ', '.join(field_reprs) + ')'

    def as_dict(self):
        '''
        Return the fields of this object as a dictionary.

        :rtype: dict
        '''

        return {'element': self.element, 'element_set': self.element_set, 'html': self.html, 'text': self.text}

    def as_tuple(self):
        '''
        Return the fields of this object in declaration order as a tuple.

        :rtype: tuple
        '''

        return (self.element, self.element_set, self.html, self.text,)

    @property
    def element(self):
        '''
        :rtype: yomeka.api.omeka_element.OmekaElement
        '''

        return self.__element

    @property
    def element_set(self):
        '''
        :rtype: yomeka.api.omeka_element_set.OmekaElementSet
        '''

        return self.__element_set

    @property
    def html(self):
        '''
        :rtype: bool
        '''

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
            if ifield_type == 0: # STOP
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

    def replace(
        self,
        element=None,
        element_set=None,
        html=None,
        text=None,
    ):
        '''
        Copy this object, replace one or more fields, and return the copy.

        :type element: yomeka.api.omeka_element.OmekaElement or None
        :type element_set: yomeka.api.omeka_element_set.OmekaElementSet or None
        :type html: bool or None
        :type text: str or None
        :rtype: yomeka.api.omeka_element_text.OmekaElementText
        '''

        if element is None:
            element = self.element
        if element_set is None:
            element_set = self.element_set
        if html is None:
            html = self.html
        if text is None:
            text = self.text
        return self.__class__(element=element, element_set=element_set, html=html, text=text)

    @property
    def text(self):
        '''
        :rtype: str
        '''

        return self.__text

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
