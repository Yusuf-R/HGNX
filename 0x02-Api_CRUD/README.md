# API CRUD functonality
###  A simple REST API to demonstrate CRUD operation

### Introduction
A simple REST API capable of CRUD operations on a "person" resource, interfacing with any database of your choice. The API dynamically handles parameters, such as adding or retrieving a person by name

### Project Support Features
* Users can signup and login to their accounts
* Public (non-authenticated) users can access all causes on the platform
* Authenticated users can access all causes as well as create a new cause, edit their created cause and also delete what they've created.
### Installation Guide

### Usage
* Run npm start:dev to start the application.
* Connect to the API using Postman on port 7066.

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

    curl -X POST http://0.0.0.0:5800/api -H "Content-Type: application/json" -d '{name: General MacTavish}'
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

### Response

<!doctype html>
<html lang=en>
<title>400 Bad Request</title>
<h1>Bad Request</h1>
<p>Error: name already exists</p>



## Authors
Abdulwasiu Tunde Yusuf

## License
This project is available for use under the MIT License.
