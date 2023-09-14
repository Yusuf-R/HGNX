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

### Authors

### License
This project is available for use under the MIT License.
