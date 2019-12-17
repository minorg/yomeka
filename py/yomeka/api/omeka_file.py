from itertools import filterfalse
import builtins
import datetime
import typing
import yomeka.api.omeka_element_text
import yomeka.api.omeka_file_urls


class OmekaFile(object):
    class Builder(object):
        def __init__(
            self,
            added=None,
            authentication=None,
            element_texts=None,
            file_urls=None,
            has_derivative_image=None,
            id=None,  # @ReservedAssignment
            item_id=None,
            mime_type=None,
            modified=None,
            original_filename=None,
            size=None,
            stored=None,
            type_os=None,
            url=None,
            json=None,
        ):
            self.__added = added
            self.__authentication = authentication
            self.__element_texts = element_texts
            self.__file_urls = file_urls
            self.__has_derivative_image = has_derivative_image
            self.__id = id
            self.__item_id = item_id
            self.__mime_type = mime_type
            self.__modified = modified
            self.__original_filename = original_filename
            self.__size = size
            self.__stored = stored
            self.__type_os = type_os
            self.__url = url
            self.__json = json

        def build(self):
            return OmekaFile(added=self.__added, authentication=self.__authentication, element_texts=self.__element_texts, file_urls=self.__file_urls, has_derivative_image=self.__has_derivative_image, id=self.__id, item_id=self.__item_id, mime_type=self.__mime_type, modified=self.__modified, original_filename=self.__original_filename, size=self.__size, stored=self.__stored, type_os=self.__type_os, url=self.__url, json=self.__json)

        @property
        def added(self) -> datetime.datetime:
            return self.__added

        @property
        def authentication(self) -> str:
            return self.__authentication

        @property
        def element_texts(self) -> typing.Tuple[yomeka.api.omeka_element_text.OmekaElementText, ...]:
            return self.__element_texts

        @property
        def file_urls(self) -> yomeka.api.omeka_file_urls.OmekaFileUrls:
            return self.__file_urls

        @classmethod
        def from_template(cls, template):
            '''
            :type template: yomeka.api.omeka_file.OmekaFile
            :rtype: yomeka.api.omeka_file.OmekaFile
            '''

            builder = cls()
            builder.added = template.added
            builder.authentication = template.authentication
            builder.element_texts = template.element_texts
            builder.file_urls = template.file_urls
            builder.has_derivative_image = template.has_derivative_image
            builder.id = template.id
            builder.item_id = template.item_id
            builder.mime_type = template.mime_type
            builder.modified = template.modified
            builder.original_filename = template.original_filename
            builder.size = template.size
            builder.stored = template.stored
            builder.type_os = template.type_os
            builder.url = template.url
            builder.json = template.json
            return builder

        @property
        def has_derivative_image(self) -> bool:
            return self.__has_derivative_image

        @property
        def id(self) -> int:  # @ReservedAssignment
            return self.__id

        @property
        def item_id(self) -> int:
            return self.__item_id

        @property
        def json(self) -> typing.Optional[str]:
            return self.__json

        @property
        def mime_type(self) -> str:
            return self.__mime_type

        @property
        def modified(self) -> datetime.datetime:
            return self.__modified

        @property
        def original_filename(self) -> str:
            return self.__original_filename

        def set_added(self, added: datetime.datetime):
            if added is None:
                raise ValueError('added is required')
            if not isinstance(added, datetime.datetime):
                raise TypeError("expected added to be a datetime.datetime but it is a %s" % builtins.type(added))
            self.__added = added
            return self

        def set_authentication(self, authentication: str):
            if authentication is None:
                raise ValueError('authentication is required')
            if not isinstance(authentication, str):
                raise TypeError("expected authentication to be a str but it is a %s" % builtins.type(authentication))
            if len(authentication) < 1:
                raise ValueError("expected len(authentication) to be >= 1, was %d" % len(authentication))
            self.__authentication = authentication
            return self

        def set_element_texts(self, element_texts: typing.Tuple[yomeka.api.omeka_element_text.OmekaElementText, ...]):
            if element_texts is None:
                raise ValueError('element_texts is required')
            if not (isinstance(element_texts, tuple) and len(list(filterfalse(lambda _: isinstance(_, yomeka.api.omeka_element_text.OmekaElementText), element_texts))) == 0):
                raise TypeError("expected element_texts to be a typing.Tuple[yomeka.api.omeka_element_text.OmekaElementText, ...] but it is a %s" % builtins.type(element_texts))
            self.__element_texts = element_texts
            return self

        def set_file_urls(self, file_urls: yomeka.api.omeka_file_urls.OmekaFileUrls):
            if file_urls is None:
                raise ValueError('file_urls is required')
            if not isinstance(file_urls, yomeka.api.omeka_file_urls.OmekaFileUrls):
                raise TypeError("expected file_urls to be a yomeka.api.omeka_file_urls.OmekaFileUrls but it is a %s" % builtins.type(file_urls))
            self.__file_urls = file_urls
            return self

        def set_has_derivative_image(self, has_derivative_image: bool):
            if has_derivative_image is None:
                raise ValueError('has_derivative_image is required')
            if not isinstance(has_derivative_image, bool):
                raise TypeError("expected has_derivative_image to be a bool but it is a %s" % builtins.type(has_derivative_image))
            self.__has_derivative_image = has_derivative_image
            return self

        def set_id(self, id: int):  # @ReservedAssignment
            if id is None:
                raise ValueError('id is required')
            if not isinstance(id, int):
                raise TypeError("expected id to be a int but it is a %s" % builtins.type(id))
            self.__id = id
            return self

        def set_item_id(self, item_id: int):
            if item_id is None:
                raise ValueError('item_id is required')
            if not isinstance(item_id, int):
                raise TypeError("expected item_id to be a int but it is a %s" % builtins.type(item_id))
            self.__item_id = item_id
            return self

        def set_json(self, json: typing.Optional[str]):
            if json is not None:
                if not isinstance(json, str):
                    raise TypeError("expected json to be a str but it is a %s" % builtins.type(json))
                if len(json) < 1:
                    raise ValueError("expected len(json) to be >= 1, was %d" % len(json))
            self.__json = json
            return self

        def set_mime_type(self, mime_type: str):
            if mime_type is None:
                raise ValueError('mime_type is required')
            if not isinstance(mime_type, str):
                raise TypeError("expected mime_type to be a str but it is a %s" % builtins.type(mime_type))
            if len(mime_type) < 1:
                raise ValueError("expected len(mime_type) to be >= 1, was %d" % len(mime_type))
            self.__mime_type = mime_type
            return self

        def set_modified(self, modified: datetime.datetime):
            if modified is None:
                raise ValueError('modified is required')
            if not isinstance(modified, datetime.datetime):
                raise TypeError("expected modified to be a datetime.datetime but it is a %s" % builtins.type(modified))
            self.__modified = modified
            return self

        def set_original_filename(self, original_filename: str):
            if original_filename is None:
                raise ValueError('original_filename is required')
            if not isinstance(original_filename, str):
                raise TypeError("expected original_filename to be a str but it is a %s" % builtins.type(original_filename))
            if len(original_filename) < 1:
                raise ValueError("expected len(original_filename) to be >= 1, was %d" % len(original_filename))
            self.__original_filename = original_filename
            return self

        def set_size(self, size: int):
            if size is None:
                raise ValueError('size is required')
            if not isinstance(size, int):
                raise TypeError("expected size to be a int but it is a %s" % builtins.type(size))
            self.__size = size
            return self

        def set_stored(self, stored: bool):
            if stored is None:
                raise ValueError('stored is required')
            if not isinstance(stored, bool):
                raise TypeError("expected stored to be a bool but it is a %s" % builtins.type(stored))
            self.__stored = stored
            return self

        def set_type_os(self, type_os: str):
            if type_os is None:
                raise ValueError('type_os is required')
            if not isinstance(type_os, str):
                raise TypeError("expected type_os to be a str but it is a %s" % builtins.type(type_os))
            if len(type_os) < 1:
                raise ValueError("expected len(type_os) to be >= 1, was %d" % len(type_os))
            self.__type_os = type_os
            return self

        def set_url(self, url: str):
            if url is None:
                raise ValueError('url is required')
            if not isinstance(url, str):
                raise TypeError("expected url to be a str but it is a %s" % builtins.type(url))
            self.__url = url
            return self

        @property
        def size(self) -> int:
            return self.__size

        @property
        def stored(self) -> bool:
            return self.__stored

        @property
        def type_os(self) -> str:
            return self.__type_os

        def update(self, omeka_file):
            if isinstance(omeka_file, OmekaFile):
                self.set_added(omeka_file.added)
                self.set_authentication(omeka_file.authentication)
                self.set_element_texts(omeka_file.element_texts)
                self.set_file_urls(omeka_file.file_urls)
                self.set_has_derivative_image(omeka_file.has_derivative_image)
                self.set_id(omeka_file.id)
                self.set_item_id(omeka_file.item_id)
                self.set_mime_type(omeka_file.mime_type)
                self.set_modified(omeka_file.modified)
                self.set_original_filename(omeka_file.original_filename)
                self.set_size(omeka_file.size)
                self.set_stored(omeka_file.stored)
                self.set_type_os(omeka_file.type_os)
                self.set_url(omeka_file.url)
                self.set_json(omeka_file.json)
            elif isinstance(omeka_file, dict):
                for key, value in omeka_file.items():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(omeka_file)
            return self

        @property
        def url(self) -> str:
            return self.__url

        @added.setter
        def added(self, added: datetime.datetime) -> None:
            self.set_added(added)

        @authentication.setter
        def authentication(self, authentication: str) -> None:
            self.set_authentication(authentication)

        @element_texts.setter
        def element_texts(self, element_texts: typing.Tuple[yomeka.api.omeka_element_text.OmekaElementText, ...]) -> None:
            self.set_element_texts(element_texts)

        @file_urls.setter
        def file_urls(self, file_urls: yomeka.api.omeka_file_urls.OmekaFileUrls) -> None:
            self.set_file_urls(file_urls)

        @has_derivative_image.setter
        def has_derivative_image(self, has_derivative_image: bool) -> None:
            self.set_has_derivative_image(has_derivative_image)

        @id.setter
        def id(self, id: int) -> None:  # @ReservedAssignment
            self.set_id(id)

        @item_id.setter
        def item_id(self, item_id: int) -> None:
            self.set_item_id(item_id)

        @json.setter
        def json(self, json: typing.Optional[str]) -> None:
            self.set_json(json)

        @mime_type.setter
        def mime_type(self, mime_type: str) -> None:
            self.set_mime_type(mime_type)

        @modified.setter
        def modified(self, modified: datetime.datetime) -> None:
            self.set_modified(modified)

        @original_filename.setter
        def original_filename(self, original_filename: str) -> None:
            self.set_original_filename(original_filename)

        @size.setter
        def size(self, size: int) -> None:
            self.set_size(size)

        @stored.setter
        def stored(self, stored: bool) -> None:
            self.set_stored(stored)

        @type_os.setter
        def type_os(self, type_os: str) -> None:
            self.set_type_os(type_os)

        @url.setter
        def url(self, url: str) -> None:
            self.set_url(url)

    class FieldMetadata(object):
        ADDED = None
        AUTHENTICATION = None
        ELEMENT_TEXTS = None
        FILE_URLS = None
        HAS_DERIVATIVE_IMAGE = None
        ID = None
        ITEM_ID = None
        MIME_TYPE = None
        MODIFIED = None
        ORIGINAL_FILENAME = None
        SIZE = None
        STORED = None
        TYPE_OS = None
        URL = None
        JSON = None

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
            return (cls.ADDED, cls.AUTHENTICATION, cls.ELEMENT_TEXTS, cls.FILE_URLS, cls.HAS_DERIVATIVE_IMAGE, cls.ID, cls.ITEM_ID, cls.MIME_TYPE, cls.MODIFIED, cls.ORIGINAL_FILENAME, cls.SIZE, cls.STORED, cls.TYPE_OS, cls.URL, cls.JSON,)

    FieldMetadata.ADDED = FieldMetadata('added', datetime.datetime, None)
    FieldMetadata.AUTHENTICATION = FieldMetadata('authentication', str, {'minLength': 1})
    FieldMetadata.ELEMENT_TEXTS = FieldMetadata('element_texts', tuple, None)
    FieldMetadata.FILE_URLS = FieldMetadata('file_urls', yomeka.api.omeka_file_urls.OmekaFileUrls, None)
    FieldMetadata.HAS_DERIVATIVE_IMAGE = FieldMetadata('has_derivative_image', bool, None)
    FieldMetadata.ID = FieldMetadata('id', int, None)
    FieldMetadata.ITEM_ID = FieldMetadata('item_id', int, None)
    FieldMetadata.MIME_TYPE = FieldMetadata('mime_type', str, {'minLength': 1})
    FieldMetadata.MODIFIED = FieldMetadata('modified', datetime.datetime, None)
    FieldMetadata.ORIGINAL_FILENAME = FieldMetadata('original_filename', str, {'minLength': 1})
    FieldMetadata.SIZE = FieldMetadata('size', int, None)
    FieldMetadata.STORED = FieldMetadata('stored', bool, None)
    FieldMetadata.TYPE_OS = FieldMetadata('type_os', str, {'minLength': 1})
    FieldMetadata.URL = FieldMetadata('url', str, None)
    FieldMetadata.JSON = FieldMetadata('json', str, {'minLength': 1})

    def __init__(
        self,
        added: datetime.datetime,
        authentication: str,
        element_texts: typing.Tuple[yomeka.api.omeka_element_text.OmekaElementText, ...],
        file_urls: yomeka.api.omeka_file_urls.OmekaFileUrls,
        has_derivative_image: bool,
        id: int,  # @ReservedAssignment
        item_id: int,
        mime_type: str,
        modified: datetime.datetime,
        original_filename: str,
        size: int,
        stored: bool,
        type_os: str,
        url: str,
        json: typing.Optional[str] = None,
    ):
        if added is None:
            raise ValueError('added is required')
        if not isinstance(added, datetime.datetime):
            raise TypeError("expected added to be a datetime.datetime but it is a %s" % builtins.type(added))
        self.__added = added

        if authentication is None:
            raise ValueError('authentication is required')
        if not isinstance(authentication, str):
            raise TypeError("expected authentication to be a str but it is a %s" % builtins.type(authentication))
        if len(authentication) < 1:
            raise ValueError("expected len(authentication) to be >= 1, was %d" % len(authentication))
        self.__authentication = authentication

        if element_texts is None:
            raise ValueError('element_texts is required')
        if not (isinstance(element_texts, tuple) and len(list(filterfalse(lambda _: isinstance(_, yomeka.api.omeka_element_text.OmekaElementText), element_texts))) == 0):
            raise TypeError("expected element_texts to be a typing.Tuple[yomeka.api.omeka_element_text.OmekaElementText, ...] but it is a %s" % builtins.type(element_texts))
        self.__element_texts = element_texts

        if file_urls is None:
            raise ValueError('file_urls is required')
        if not isinstance(file_urls, yomeka.api.omeka_file_urls.OmekaFileUrls):
            raise TypeError("expected file_urls to be a yomeka.api.omeka_file_urls.OmekaFileUrls but it is a %s" % builtins.type(file_urls))
        self.__file_urls = file_urls

        if has_derivative_image is None:
            raise ValueError('has_derivative_image is required')
        if not isinstance(has_derivative_image, bool):
            raise TypeError("expected has_derivative_image to be a bool but it is a %s" % builtins.type(has_derivative_image))
        self.__has_derivative_image = has_derivative_image

        if id is None:
            raise ValueError('id is required')
        if not isinstance(id, int):
            raise TypeError("expected id to be a int but it is a %s" % builtins.type(id))
        self.__id = id

        if item_id is None:
            raise ValueError('item_id is required')
        if not isinstance(item_id, int):
            raise TypeError("expected item_id to be a int but it is a %s" % builtins.type(item_id))
        self.__item_id = item_id

        if mime_type is None:
            raise ValueError('mime_type is required')
        if not isinstance(mime_type, str):
            raise TypeError("expected mime_type to be a str but it is a %s" % builtins.type(mime_type))
        if len(mime_type) < 1:
            raise ValueError("expected len(mime_type) to be >= 1, was %d" % len(mime_type))
        self.__mime_type = mime_type

        if modified is None:
            raise ValueError('modified is required')
        if not isinstance(modified, datetime.datetime):
            raise TypeError("expected modified to be a datetime.datetime but it is a %s" % builtins.type(modified))
        self.__modified = modified

        if original_filename is None:
            raise ValueError('original_filename is required')
        if not isinstance(original_filename, str):
            raise TypeError("expected original_filename to be a str but it is a %s" % builtins.type(original_filename))
        if len(original_filename) < 1:
            raise ValueError("expected len(original_filename) to be >= 1, was %d" % len(original_filename))
        self.__original_filename = original_filename

        if size is None:
            raise ValueError('size is required')
        if not isinstance(size, int):
            raise TypeError("expected size to be a int but it is a %s" % builtins.type(size))
        self.__size = size

        if stored is None:
            raise ValueError('stored is required')
        if not isinstance(stored, bool):
            raise TypeError("expected stored to be a bool but it is a %s" % builtins.type(stored))
        self.__stored = stored

        if type_os is None:
            raise ValueError('type_os is required')
        if not isinstance(type_os, str):
            raise TypeError("expected type_os to be a str but it is a %s" % builtins.type(type_os))
        if len(type_os) < 1:
            raise ValueError("expected len(type_os) to be >= 1, was %d" % len(type_os))
        self.__type_os = type_os

        if url is None:
            raise ValueError('url is required')
        if not isinstance(url, str):
            raise TypeError("expected url to be a str but it is a %s" % builtins.type(url))
        self.__url = url

        if json is not None:
            if not isinstance(json, str):
                raise TypeError("expected json to be a str but it is a %s" % builtins.type(json))
            if len(json) < 1:
                raise ValueError("expected len(json) to be >= 1, was %d" % len(json))
        self.__json = json

    def __eq__(self, other):
        if self.added != other.added:
            return False
        if self.authentication != other.authentication:
            return False
        if self.element_texts != other.element_texts:
            return False
        if self.file_urls != other.file_urls:
            return False
        if self.has_derivative_image != other.has_derivative_image:
            return False
        if self.id != other.id:
            return False
        if self.item_id != other.item_id:
            return False
        if self.mime_type != other.mime_type:
            return False
        if self.modified != other.modified:
            return False
        if self.original_filename != other.original_filename:
            return False
        if self.size != other.size:
            return False
        if self.stored != other.stored:
            return False
        if self.type_os != other.type_os:
            return False
        if self.url != other.url:
            return False
        if self.json != other.json:
            return False
        return True

    def __hash__(self):
        return hash((self.added, self.authentication, self.element_texts, self.file_urls, self.has_derivative_image, self.id, self.item_id, self.mime_type, self.modified, self.original_filename, self.size, self.stored, self.type_os, self.url, self.json,))

    def __iter__(self):
        return iter((self.added, self.authentication, self.element_texts, self.file_urls, self.has_derivative_image, self.id, self.item_id, self.mime_type, self.modified, self.original_filename, self.size, self.stored, self.type_os, self.url, self.json,))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        field_reprs.append('added=' + repr(self.added))
        field_reprs.append('authentication=' + "'" + self.authentication.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('element_texts=' + repr(self.element_texts))
        field_reprs.append('file_urls=' + repr(self.file_urls))
        field_reprs.append('has_derivative_image=' + repr(self.has_derivative_image))
        field_reprs.append('id=' + repr(self.id))
        field_reprs.append('item_id=' + repr(self.item_id))
        field_reprs.append('mime_type=' + "'" + self.mime_type.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('modified=' + repr(self.modified))
        field_reprs.append('original_filename=' + "'" + self.original_filename.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('size=' + repr(self.size))
        field_reprs.append('stored=' + repr(self.stored))
        field_reprs.append('type_os=' + "'" + self.type_os.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('url=' + "'" + self.url.encode('ascii', 'replace').decode('ascii') + "'")
        if self.json is not None:
            field_reprs.append('json=' + "'" + self.json.encode('ascii', 'replace').decode('ascii') + "'")
        return 'OmekaFile(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        field_reprs.append('added=' + repr(self.added))
        field_reprs.append('authentication=' + "'" + self.authentication.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('element_texts=' + repr(self.element_texts))
        field_reprs.append('file_urls=' + repr(self.file_urls))
        field_reprs.append('has_derivative_image=' + repr(self.has_derivative_image))
        field_reprs.append('id=' + repr(self.id))
        field_reprs.append('item_id=' + repr(self.item_id))
        field_reprs.append('mime_type=' + "'" + self.mime_type.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('modified=' + repr(self.modified))
        field_reprs.append('original_filename=' + "'" + self.original_filename.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('size=' + repr(self.size))
        field_reprs.append('stored=' + repr(self.stored))
        field_reprs.append('type_os=' + "'" + self.type_os.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('url=' + "'" + self.url.encode('ascii', 'replace').decode('ascii') + "'")
        if self.json is not None:
            field_reprs.append('json=' + "'" + self.json.encode('ascii', 'replace').decode('ascii') + "'")
        return 'OmekaFile(' + ', '.join(field_reprs) + ')'

    @property
    def added(self) -> datetime.datetime:
        return self.__added

    @property
    def authentication(self) -> str:
        return self.__authentication

    @classmethod
    def builder(cls):
        return cls.Builder()

    @property
    def element_texts(self) -> typing.Tuple[yomeka.api.omeka_element_text.OmekaElementText, ...]:
        return self.__element_texts

    @property
    def file_urls(self) -> yomeka.api.omeka_file_urls.OmekaFileUrls:
        return self.__file_urls

    @classmethod
    def from_builtins(cls, _dict):
        if not isinstance(_dict, dict):
            raise ValueError("expected dict")

        __builder = cls.builder()

        added = _dict.get("added")
        if added is None:
            raise KeyError("added")
        __builder.added = added

        authentication = _dict.get("authentication")
        if authentication is None:
            raise KeyError("authentication")
        __builder.authentication = authentication

        element_texts = _dict.get("element_texts")
        if element_texts is None:
            raise KeyError("element_texts")
        element_texts = tuple(yomeka.api.omeka_element_text.OmekaElementText.from_builtins(element0) for element0 in element_texts)
        __builder.element_texts = element_texts

        file_urls = _dict.get("file_urls")
        if file_urls is None:
            raise KeyError("file_urls")
        file_urls = yomeka.api.omeka_file_urls.OmekaFileUrls.from_builtins(file_urls)
        __builder.file_urls = file_urls

        has_derivative_image = _dict.get("has_derivative_image")
        if has_derivative_image is None:
            raise KeyError("has_derivative_image")
        __builder.has_derivative_image = has_derivative_image

        id = _dict.get("id")
        if id is None:
            raise KeyError("id")
        __builder.id = id

        item_id = _dict.get("item_id")
        if item_id is None:
            raise KeyError("item_id")
        __builder.item_id = item_id

        mime_type = _dict.get("mime_type")
        if mime_type is None:
            raise KeyError("mime_type")
        __builder.mime_type = mime_type

        modified = _dict.get("modified")
        if modified is None:
            raise KeyError("modified")
        __builder.modified = modified

        original_filename = _dict.get("original_filename")
        if original_filename is None:
            raise KeyError("original_filename")
        __builder.original_filename = original_filename

        size = _dict.get("size")
        if size is None:
            raise KeyError("size")
        __builder.size = size

        stored = _dict.get("stored")
        if stored is None:
            raise KeyError("stored")
        __builder.stored = stored

        type_os = _dict.get("type_os")
        if type_os is None:
            raise KeyError("type_os")
        __builder.type_os = type_os

        url = _dict.get("url")
        if url is None:
            raise KeyError("url")
        __builder.url = url

        __builder.json = _dict.get("json")

        return __builder.build()

    @property
    def has_derivative_image(self) -> bool:
        return self.__has_derivative_image

    @property
    def id(self) -> int:  # @ReservedAssignment
        return self.__id

    @property
    def item_id(self) -> int:
        return self.__item_id

    @property
    def json(self) -> typing.Optional[str]:
        return self.__json

    @property
    def mime_type(self) -> str:
        return self.__mime_type

    @property
    def modified(self) -> datetime.datetime:
        return self.__modified

    @property
    def original_filename(self) -> str:
        return self.__original_filename

    @classmethod
    def read(cls, iprot):
        '''
        Read a new object from the given input protocol and return the object.

        :type iprot: thryft.protocol._input_protocol._InputProtocol
        :rtype: yomeka.api.omeka_file.OmekaFile
        '''

        init_kwds = {}

        iprot.read_struct_begin()
        while True:
            ifield_name, ifield_type, _ifield_id = iprot.read_field_begin()
            if ifield_type == 0:  # STOP
                break
            elif ifield_name == 'added':
                init_kwds['added'] = iprot.read_date_time()
            elif ifield_name == 'authentication':
                init_kwds['authentication'] = iprot.read_string()
            elif ifield_name == 'element_texts':
                init_kwds['element_texts'] = tuple([yomeka.api.omeka_element_text.OmekaElementText.read(iprot) for _ in range(iprot.read_list_begin()[1])] + (iprot.read_list_end() is None and []))
            elif ifield_name == 'file_urls':
                init_kwds['file_urls'] = yomeka.api.omeka_file_urls.OmekaFileUrls.read(iprot)
            elif ifield_name == 'has_derivative_image':
                init_kwds['has_derivative_image'] = iprot.read_bool()
            elif ifield_name == 'id':
                init_kwds['id'] = iprot.read_i32()
            elif ifield_name == 'item_id':
                init_kwds['item_id'] = iprot.read_i32()
            elif ifield_name == 'mime_type':
                init_kwds['mime_type'] = iprot.read_string()
            elif ifield_name == 'modified':
                init_kwds['modified'] = iprot.read_date_time()
            elif ifield_name == 'original_filename':
                init_kwds['original_filename'] = iprot.read_string()
            elif ifield_name == 'size':
                init_kwds['size'] = iprot.read_i32()
            elif ifield_name == 'stored':
                init_kwds['stored'] = iprot.read_bool()
            elif ifield_name == 'type_os':
                init_kwds['type_os'] = iprot.read_string()
            elif ifield_name == 'url':
                init_kwds['url'] = iprot.read_string()
            elif ifield_name == 'json':
                try:
                    init_kwds['json'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            iprot.read_field_end()
        iprot.read_struct_end()

        return cls(**init_kwds)

    def replacer(self):
        return self.Builder.from_template(template=self)

    @property
    def size(self) -> int:
        return self.__size

    @property
    def stored(self) -> bool:
        return self.__stored

    def to_builtins(self):
        dict_ = {}
        dict_["added"] = self.added
        dict_["authentication"] = self.authentication
        dict_["element_texts"] = tuple(element0.to_builtins() for element0 in self.element_texts)
        dict_["file_urls"] = self.file_urls.to_builtins()
        dict_["has_derivative_image"] = self.has_derivative_image
        dict_["id"] = self.id
        dict_["item_id"] = self.item_id
        dict_["mime_type"] = self.mime_type
        dict_["modified"] = self.modified
        dict_["original_filename"] = self.original_filename
        dict_["size"] = self.size
        dict_["stored"] = self.stored
        dict_["type_os"] = self.type_os
        dict_["url"] = self.url
        if self.json is not None:
            dict_["json"] = self.json
        return dict_

    @property
    def type_os(self) -> str:
        return self.__type_os

    @property
    def url(self) -> str:
        return self.__url

    def write(self, oprot):
        '''
        Write this object to the given output protocol and return self.

        :type oprot: thryft.protocol._output_protocol._OutputProtocol
        :rtype: yomeka.api.omeka_file.OmekaFile
        '''

        oprot.write_struct_begin('OmekaFile')

        oprot.write_field_begin(name='added', type=10, id=None)
        oprot.write_date_time(self.added)
        oprot.write_field_end()

        oprot.write_field_begin(name='authentication', type=11, id=None)
        oprot.write_string(self.authentication)
        oprot.write_field_end()

        oprot.write_field_begin(name='element_texts', type=15, id=None)
        oprot.write_list_begin(12, len(self.element_texts))
        for _0 in self.element_texts:
            _0.write(oprot)
        oprot.write_list_end()
        oprot.write_field_end()

        oprot.write_field_begin(name='file_urls', type=12, id=None)
        self.file_urls.write(oprot)
        oprot.write_field_end()

        oprot.write_field_begin(name='has_derivative_image', type=2, id=None)
        oprot.write_bool(self.has_derivative_image)
        oprot.write_field_end()

        oprot.write_field_begin(name='id', type=8, id=None)
        oprot.write_i32(self.id)
        oprot.write_field_end()

        oprot.write_field_begin(name='item_id', type=8, id=None)
        oprot.write_i32(self.item_id)
        oprot.write_field_end()

        oprot.write_field_begin(name='mime_type', type=11, id=None)
        oprot.write_string(self.mime_type)
        oprot.write_field_end()

        oprot.write_field_begin(name='modified', type=10, id=None)
        oprot.write_date_time(self.modified)
        oprot.write_field_end()

        oprot.write_field_begin(name='original_filename', type=11, id=None)
        oprot.write_string(self.original_filename)
        oprot.write_field_end()

        oprot.write_field_begin(name='size', type=8, id=None)
        oprot.write_i32(self.size)
        oprot.write_field_end()

        oprot.write_field_begin(name='stored', type=2, id=None)
        oprot.write_bool(self.stored)
        oprot.write_field_end()

        oprot.write_field_begin(name='type_os', type=11, id=None)
        oprot.write_string(self.type_os)
        oprot.write_field_end()

        oprot.write_field_begin(name='url', type=11, id=None)
        oprot.write_string(self.url)
        oprot.write_field_end()

        if self.json is not None:
            oprot.write_field_begin(name='json', type=11, id=None)
            oprot.write_string(self.json)
            oprot.write_field_end()

        oprot.write_field_stop()

        oprot.write_struct_end()

        return self
