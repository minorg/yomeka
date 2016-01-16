namespace * yomeka.api

include "thryft/native/url.thrift"

struct OmekaTag {
	i32 id;
	// @validation {"minLength": 1}
	string name;
	url.Url url;
}
