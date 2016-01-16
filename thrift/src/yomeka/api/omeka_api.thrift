namespace * yomeka.api

include "yomeka/api/io_exception.thrift"
include "yomeka/api/omeka_collection.thrift"
include "yomeka/api/omeka_item.thrift"

service OmekaApi {
	list<omeka_collection.OmekaCollection>
	get_collections(
		optional i32 page,
		optional i32 per_page
	) throws (
		io_exception.IoException e
	);

	list<omeka_item.OmekaItem>
	get_items(
		optional i32 collection,
		optional i32 page,
		optional i32 per_page
	) throws (
		io_exception.IoException e
	);
}
