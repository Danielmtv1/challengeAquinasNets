# Challenge Aquinas: Seamless Integration of FBI’s Most Wanted API with MySQL Database.
### "Integrating FBI's Most Wanted API into Web Services"

![N|Solid](https://blog.pronus.io/images/python/fastapi_logo.svg)

Seamless Integration of FBI's Most Wanted API with MySQL Database, Alembic Migrations, SQLAlchemy ORM, Pydantic, and Adherence to Flake8 Coding Standards".


## Features

- Retrieve Most Wanted Information (GET /wanted/):

This endpoint retrieves information about the most wanted individuals based on the provided state.
Decodes and processes the obtained data.
Stores the information in a local database.

- Add Most Wanted Information (POST /wanted/):

This endpoint fetches data about the most wanted individuals based on the provided state.
Processes the data and stores it in a local database.
Performs data transformations, such as converting weight to numeric format and managing occupations.

- Retrieve Information of a Most Wanted Individual by ID (GET /wanted/{item_id}):

This endpoint allows you to retrieve detailed information about a most wanted individual in the local database.
Provides information such as name, gender, weight, description, images, and more, based on the database ID.
## Tech

Challenge Aquinas  uses a number of open source projects to work properly:

- [Alembic] - Database migration tool for SQLAlchemy.

- [FastAPI] - A modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

- [Gunicorn] - A Python WSGI HTTP Server for UNIX.

- [MySQL] - The Python SQL Toolkit and Object-Relational Mapper.

- [Uvicorn] - The lightning-fast ASGI server.

- [Pydantic] - Data parsing using Python type annotations.

- [Python]: A powerful programming language used for a wide range of applications.

- [Poetry]: A dependency management and packaging tool for Python projects.

## Installation

To install, you need to clone the repository. Once the repository has been cloned, make sure you have Docker installed on your system. With Docker installed, you can simply run the command 'make api' into folder aquinas to start the process."

```sh
make api
```

When running "make api," three containers are created: one for the database, another for the API, and a third one specifically for running tests. The third container executes the tests and then terminates. You can check out the Swagger documentation at the following address: http://0.0.0.0:8081/docs#/. There, you will find four routes: one for testing and three functional routes. 

if you need run test just need run :
```sh
make test
```
if you need down docker use:
```sh
make down
```
## Curls
To retrieve data for the most wanted criminals in a specific state (for example, 'Miami'):
```sh
curl --request GET \
  --url 'http://0.0.0.0:8081/wanted?state=chicago' \
  --header 'accept: application/json'
```
To retrieve data for the most wanted criminals in a state and save it in the database (for example, 'New York'):
```sh
curl --request POST \
  --url 'http://0.0.0.0:8081/wanted?state=newyork' \
  --header 'accept: application/json'
```
To retrieve data for a specific criminal by their ID from the database:
```sh
curl --request GET \
  --url http://0.0.0.0:8081/wanted/3 \
  --header 'accept: application/json'
```
## License

MIT

**Free Software**

[//]: # ()
[Alembic]:<https://alembic.sqlalchemy.org/en/latest/>
[FastAPI]:<https://fastapi.tiangolo.com/>
[Gunicorn]:<https://gunicorn.org/>
[MySQL]:<https://dev.mysql.com/doc/>
[Uvicorn]:<https://www.uvicorn.org/>
[Pydantic]:<https://docs.pydantic.dev/latest/>
[Python]:<https://www.python.org/>
[Poetry]:<https://python-poetry.org/>
  
