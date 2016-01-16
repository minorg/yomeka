namespace * yomeka.api

include "thryft/native/date_time.thrift"
include "thryft/native/url.thrift"
include "yomeka/api/omeka_element_text.thrift"

struct OmekaCollection {
	list<omeka_element_text.OmekaElementText> element_texts;
	date_time.DateTime added;
	bool featured;
	i32 id;
	i32 items_count;
	date_time.DateTime modified;
	bool public;
	url.Url url;
}
