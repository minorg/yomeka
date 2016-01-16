namespace * yomeka.api

include "yomeka/api/omeka_item.thrift"

service OmekaApi {
	list<omeka_item.OmekaItem> get_items();
}
