namespace * yomeka.api

include "yomeka/api/omeka_element.thrift"
include "yomeka/api/omeka_element_set.thrift"

struct OmekaElementText {
	omeka_element.OmekaElement element;
	omeka_element_set.OmekaElementSet element_set;
	bool html;
	string text;
}
