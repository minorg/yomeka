namespace * yomeka.api

include "thryft/native/date_time.thrift"
include "thryft/native/u32.thrift"
include "thryft/native/url.thrift"
include "yomeka/api/omeka_element_text.thrift"
include "yomeka/api/omeka_file_urls.thrift"

struct OmekaFile {
	date_time.DateTime added;
	// @validation {"minLength": 1}
	string authentication;
	list<omeka_element_text.OmekaElementText> element_texts;
    omeka_file_urls.OmekaFileUrls file_urls;
	bool has_derivative_image;
	i32 id;
	i32 item_id;
	// @validation {"minLength": 1}
	string mime_type;
	date_time.DateTime modified;
	// @validation {"minLength": 1}
	string original_filename;
	u32.u32 size;
    bool stored;
	// @validation {"minLength": 1}
	string type_os;
	url.Url url;

	// JSON representation of this file
	// @validation {"minLength": 1}
	optional string json;
}
