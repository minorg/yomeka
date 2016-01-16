namespace * yomeka.api

include "thryft/native/url.thrift"

struct OmekaElementSet {
	i32 id;
	// @validation {"minLength": 1}
	string name;
	url.Url url;
}
