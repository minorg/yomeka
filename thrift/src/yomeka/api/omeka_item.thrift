namespace * yomeka.api

include "yomeka/api/omeka_element_text.thrift"
include "yomeka/api/omeka_item_type.thrift"
include "yomeka/api/omeka_tag.thrift"
include "thryft/native/date_time.thrift"
include "thryft/native/url.thrift"

struct OmekaItem {
	list<omeka_element_text.OmekaElementText> element_texts;

	date_time.DateTime added;
	bool featured;
	i32 id;
	omeka_item_type.OmekaItemType item_type;
	date_time.DateTime modified;
	bool public;
	list<omeka_tag.OmekaTag> tags;
	url.Url url;

	// JSON representation of this item
	// @validation {"minLength": 1}
	optional string json;
}
