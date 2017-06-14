# yomeka
BSD-licensed client for the Omeka API


## Command line client

Run the entry point with -h for a list of all options.

#### Get a single item in CSV:

    py/bin/yomeka_cli.py --api-key <Omeka API key> --endpoint-url <Omeka API endpoint URL> item 634

#### Get all items in CSV:

    py/bin/yomeka_cli.py --api-key <Omeka API key> --endpoint-url <Omeka API endpoint URL> items
