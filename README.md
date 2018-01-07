# Loyalty Transactor

This repository implements a Basic Loyalty Transaction System which allows user creation,
loyalty points transfer and retrieval of users and transfers.

## Overview

- REST API Server is implemented using Flask microframework in Python3
- Postgresql, a relational database is the underlying data store

## Quick Start

### Prerequisites
- [docker](https://docs.docker.com/engine/installation/)
- [docker-compose](https://docs.docker.com/compose/install/)

### Start Application
```
$ docker-compose up
```

This builds docker images, `web:latest` and `psql:latest` and starts up two containers locally.  
Container Ports 5000(Flask Server) and 5432(Postgresql) are bound to localhost.

### Interact

1. Create User

```
$ curl -d '{"firstName":"Dinesh", "lastName": "Sriram", "email": "dinesh@test.com"}' 
       -H "Content-Type: application/json" -X POST http://localhost:5000/user
```

2. Create Transfer
```
curl -d '{"points":50, "userId":1}' -H "Content-Type: application/json" 
     -X PUT http://localhost:5000/transfer/<userId>
```

3. Query Users/Transfers
#### 
| Description | GET Endpoint |
| --- | --- |
| Home page | http://localhost:5000/ |
| Retrieve All Users| http://localhost:5000/user |
| Retrieve User by userID | http://localhost:5000/user/<userId\> |
| Retrieve Transfers by userID | http://localhost:5000/transfer/<userId\> |


### Stop Application
```
$ docker-compose down
```

## Tests

Tests are currently available only for `app.entities` package and is Pytest compatible.
`app.service` package tests can be similarly written.

```
$ python -m pytest tests
```
