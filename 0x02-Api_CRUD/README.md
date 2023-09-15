# API CRUD functonality
###  A simple REST API to demonstrate CRUD operation

### Introduction
A simple REST API capable of CRUD operations on a "person" resource, interfacing with any database of your choice. The API dynamically handles parameters, such as adding or retrieving a person by name

## Installation
* Clone this repository: `git clone "https://github.com/Yusuf-R/HGNX/tree/main/0x02-Api_CRUD"`
* Access 0x02-API_CRUD directory: `cd  0x02-API_CRUD`
### Important Requirements
* Install MySql 
* Run the hgnx.sql
```
sudo mysql -p < hgnx.sql
```
This will help set up the environment and create the database
Launch the app using flask or Gunicorn depending on the environment of choice
```
Using Flask
ubuntu@12xxx:~/HGNX/0x02-Api_CRUD$ python3 -m api.app
```
```
Using Gunicorn
ubuntu@12xxx:~/HGNX/0x02-Api_CRUD$ gunicorn --bind 0.0.0.0:5900 api.app:app
```

Test your CRUD via the appropriate command using your desired manager, eg. POSTMAN or WebBrowser

### API Endpoints
| HTTP Verbs | Endpoints | Action |
| --- | --- | --- |
| GET | /api/ | To get all the users in the databse |
| POST | /api/ | To create a new user |
| PUT | /api/id | To update valid user object |
| DELETE | /api/id | To delete an instance of a user base on its id |

# REST API example application

This is a bare-bones example of a User application providing a REST
API to a MySql-backed database.

## GET ALL User in DB

### Request

`GET /api/`

    curl -X GET http://0.0.0.0:5800/api/

### Response
```
[
  {
    "id": "defdfc61-467d-4954-859b-e19104f83610",
    "name": "Tunde"
  },
  {
    "id": "aecd1243-1e4a-406b-9ebe-e6e66b32ee13",
    "name": "TundeR"
  },
  {
    "id": "fe14f307-e59f-44df-b58d-2e3ab468a7c1",
    "name": "Yusuf Abdulwasiu Tunde"
  }
]
```

## Create a new Thing

## POST Request

`POST /api/`
```

    curl -X POST http://0.0.0.0:5800/api -H "Content-Type: application/json" -d '{"name": "General MacTavish"}'
```

### Response
```
{
    "id": "8728905d-3500-42c0-adaf-75895babe8a5",
    "name": "General MacTavish"
}
```

## GET a specific user

### Request

`GET /api/id`

```
    curl -X GET http://0.0.0.0:5800/api/8728905d-3500-42c0-adaf-75895babe8a5
```


### Response

```
{
    "id": "8728905d-3500-42c0-adaf-75895babe8a5",
    "name": "General MacTavish"
}
```
## Update a user property

## PUT Request

`PUT /api/:id/`

```
    curl -X PUT http://0.0.0.0:5800/api -H "Content-Type: application/json" -d '{"name": "Sir General MacTavish"}'
    
```

### Response

```
{
    "id": "8728905d-3500-42c0-adaf-75895babe8a5",
    "name": "Sir General MacTavish"
}
```

## Delete a User

### DELETE Request

`DELETE /api/id`

```
     curl -X DELETE http://0.0.0.0:5800/api/8728905d-3500-42c0-adaf-75895babe8a5
```
### Response

```
{}
```

## Handling Unsupported Request

#### Attempting to create with unsupported data type

#### Only supported data type is a string

`POST /api/`

```
    curl -X POST http://0.0.0.0:5800/api -H "Content-Type: application/json" -d '{"name": 600 }'
```


### Response

<!doctype html>
<html lang=en>
<title>400 Bad Request</title>
<h1>Bad Request</h1>
<p>Error: name must be a string</p>

### Create a new object with a value already in the database

This ensures all objects are strictly unique

### Request

`POST /api`

```
    curl -X PUT http://0.0.0.0:5800/api -H "Content-Type: application/json" -d '{"name": "Sir General MacTavish"}'
```
## Response
...
<p>Error: name already exists</p>



## Authors
Abdulwasiu Tunde Yusuf

## License
This project is available for use under the MIT License.
