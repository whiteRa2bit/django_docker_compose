# API Documentation

Each item has the following fields
- name
- topic
- rate
- link

Example:

    "name": "ds_hse"
    "topic": "distributed systems"
    "rate": 10
    "link": "https://github.com/osukhoroslov/hse-ds-2020"


All endpoints return json in the following format:
    {
        "ok": True/False
        "errors": {},
        "data": {}
    }

- "ok" - True, if no exceptions while processing a request, False otherwise
- "errors" - returns a string with error, if no exceptions occured returns - {}
- "data" - request processing result

Below you can find a list of supported requests and their description

## Get list of items

Returns the full list of materials, that were added

### Request

    GET /items


### Response

    200
    {
        "ok": true,
        "data": [
            {
            "rate": 10,
            "topic": "distributed systems",
            "name": "ds_hse",
            "id": 1,
            "link": "https://github.com/osukhoroslov/hse-ds-2020"
            }
        ],
        "errors": {}
    }


## Get item

Return an item description provided item id

### Request

    GET /items/id


### Response

    200
    {
        "ok": true,
        "errors": {},
        "data": {
            "name": "ds_hse",
            "topic": "distributed systems",
            "id": 1,
            "link": "https://github.com/osukhoroslov/hse-ds-2020",
            "rate": 10
        }
    }

If there is not a material with provided id returns:
    404
    {
        "ok": false,
        "errors": "No item with such id: <ID_HERE>"
    }



## Add item

Adds a new item. Checks that a request contains only the fields from a list [name, topic, rate, link].

### Request

    POST /items/add
    {
        "name": "ds_hse",
        "topic": "distributed systems",
        "rate": 10,
        "link": "https://github.com/osukhoroslov/hse-ds-2020"
    }


### Response

    200
    {
        "ok": true,
        "errors": {},
        "data": {
            "name": "ds_hse",
            "topic": "distributed systems",
            "id": 1,
            "link": "https://github.com/osukhoroslov/hse-ds-2020",
            "rate": 10
        }
    }

In case of invalid item format returns
    400
    {
        "ok": false,
        "errors": "Invalid item format, provide an item with the following fields: ['name', 'topic', 'rate', 'link']"
    }

## Delete item

Deletes item provided item id

### Request

    DELETE /items/delete/id


### Response

    200
    {
        "errors": {},
        "ok": true
    }

If there is not a material with provided id returns:

    404
    {
        "ok": false,
        "errors": "No item with such id: <ID_HERE>"
    }


## Update item

Updates item information provided item id. In the request body the desired fields are provided (not necessarily all) and their corresponding values

### Request

    PATCH /items/update/id
    {
        "name": "hse_ds"
    }


### Response

    200
    {
        "ok": true,
        "errors": {},
        "data": {
            "name": "hse_ds",
            "topic": "distributed systems",
            "id": 1,
            "link": "https://github.com/osukhoroslov/hse-ds-2020",
            "rate": 10
        }
    }

If there is not a material with provided id returns:

    404
    {
        "ok": false,
        "errors": "No item with such id: <ID_HERE>"
    }

If there are invalid fields:

    400
    {
        "ok": false,
        "errors": "Invalid item format, provide an item with the following fields: ['name', 'topic', 'rate', 'link']"
    }


