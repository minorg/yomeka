namespace * yomeka.api

include "thryft/native/date_time.thrift"
include "thryft/native/url.thrift"
include "yomeka/api/omeka_element_text.thrift"
include "yomeka/api/omeka_item_type.thrift"
include "yomeka/api/omeka_tag.thrift"

struct OmekaItem {
	date_time.DateTime added;
	list<omeka_element_text.OmekaElementText> element_texts;
    bool featured;
	i32 files_count;
	i32 id;
	date_time.DateTime modified;
	bool public;
	list<omeka_tag.OmekaTag> tags;
	url.Url url;

	optional omeka_item_type.OmekaItemType item_type;

	// JSON representation of this item
	// @validation {"minLength": 1}
	optional string json;
}
