# API CRUD functonality
###  A simple REST API capable of CRUD operation
// README.md
# Project Support
### Introduction
Project Support is an open source platform that enable users share causes they're passionate about and actively involved with with the hopes of connecting with other users equally interested in working with them on the given cause.
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
| POST | /api/ | To create a user |
| PUT | /api/<id> | To update valid user object |
| DELETE | /api/<id> | To an instance of a user base on its id |

### Authors
* [Black Developa](https://github.com/blackdevelopa)
* ![alt text](https://avatars0.githubusercontent.com/u/29962968?s=400&u=7753a408ed02e51f88a13a5d11014484bc4d80ee&v=4)
### License
This project is available for use under the MIT License.
