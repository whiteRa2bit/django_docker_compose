# Документация на мой API

Ниже приведена документация для API для хранения учебных материалов.
У каждого учебного материала присутствуют следующие поля:
- name (Название)
- topic (К какой теме относиться учебный материал)
- rate (Насколько полезным считается данный материал)
- link (Ссылка на источник)

Пример:

    "name": "ds_hse"
    "topic": "distributed systems"
    "rate": 10
    "link": "https://github.com/osukhoroslov/hse-ds-2020"


Все endpoints возвращают json в cледующем формате:

    {
        "ok": True/False
        "errors": {},
        "data": {}
    }

- "ok" - True, если не возникло ошибок при обработке запроса, False иначе
- "errors" - возвращает строку с ошибкой, которая возникла при обработке запроса, если ошибок нет - {}
- "data" - результат выполнения запроса

Ниже представлены запросы, которые поддерживаются, и примеры для них.

## Get list of items

Возвращает список всех учебных материалов, которые были добавлены

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

Возвращает описание одного учебного материала по предоставленному id

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

В случае если материала с таким id не существует возвращает следующее:

    404
    {
        "ok": false,
        "errors": "No item with such id: <ID_HERE>"
    }



## Add item

Добавляет новый учебный материал. Валидирует, что запрос содержит все поля из [name, topic, rate, link] и никаких кроме них.

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

В случае некорректного запроса возвращает:

    400
    {
        "ok": false,
        "errors": "Invalid item format, provide an item with the following fields: ['name', 'topic', 'rate', 'link']"
    }

## Delete item

Удаляет учебный материал по предоставленному id

### Request

    DELETE /items/delete/id


### Response

    200
    {
        "errors": {},
        "ok": true
    }

В случае если материала с таким id не существует возвращает следующее:

    404
    {
        "ok": false,
        "errors": "No item with such id: <ID_HERE>"
    }


## Update item

Обновляет информацию об учебном материале по предоставленному id. В теле запроса предоставляются несколько полей (не обязательно все) и соотвествующие для них значения.

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

В случае если материала с таким id не существует возвращает следующее:

    404
    {
        "ok": false,
        "errors": "No item with such id: <ID_HERE>"
    }

В случае если в теле запроса будут указаны невалидные поля:

    400
    {
        "ok": false,
        "errors": "Invalid item format, provide an item with the following fields: ['name', 'topic', 'rate', 'link']"
    }


