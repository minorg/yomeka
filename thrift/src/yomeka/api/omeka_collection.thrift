namespace * yomeka.api

include "thryft/native/date_time.thrift"
include "thryft/native/url.thrift"
include "yomeka/api/omeka_element_text.thrift"

struct OmekaCollection {
	date_time.DateTime added;
	list<omeka_element_text.OmekaElementText> element_texts;
	bool featured;
	i32 id;
	i32 items_count;
	date_time.DateTime modified;
	bool public;
	url.Url url;

	// JSON representation of this collection
	// @validation {"minLength": 1}
	optional string json;
}
