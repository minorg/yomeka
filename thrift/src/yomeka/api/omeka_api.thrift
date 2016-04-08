namespace * yomeka.api

include "yomeka/api/io_exception.thrift"
include "yomeka/api/no_such_omeka_collection_exception.thrift"
include "yomeka/api/no_such_omeka_item_exception.thrift"
include "yomeka/api/omeka_collection.thrift"
include "yomeka/api/omeka_file.thrift"
include "yomeka/api/omeka_item.thrift"

service OmekaApi {
    omeka_collection.OmekaCollection
    get_collection(
        i32 id
    ) throws (
        io_exception.IoException e1,
        no_such_omeka_collection_exception.NoSuchOmekaCollectionException e2
    );

	list<omeka_collection.OmekaCollection>
	get_collections(
		optional i32 page,
		optional i32 per_page
	) throws (
		io_exception.IoException e
	);

	list<omeka_file.OmekaFile>
	get_files(
		optional i32 item,
		optional i32 page,
		optional i32 per_page
	) throws (
		io_exception.IoException e
	);

    omeka_item.OmekaItem
    get_item(
        i32 id
    ) throws (
        io_exception.IoException e1,
        no_such_omeka_item_exception.NoSuchOmekaItemException e2
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
