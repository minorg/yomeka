namespace * yomeka.api

include "thryft/native/url.thrift"

struct OmekaFileUrls {
	url.Url original;

	optional url.Url fullsize;
	optional url.Url square_thumbnail;
	optional url.Url thumbnail;
}
