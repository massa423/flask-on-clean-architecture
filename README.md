# Overview

Flask Sample Application on Clean Architecture.


# Requirements

* Python 3.9
* [Poetry](https://python-poetry.org/docs/)

# How to use

## Installation

Clone repository.

```
git clone https://github.com/massa423/flask-on-clean-architecture.git
```

Install libraries.


```
cd flask-on-clean-architecture
poetry install
```

## initialize DB (development)

```
export FLASK_APP=app/cli.py
export APP_ENV=development
flask init-db
```

## Application launch

### development
#### a. flask run

```
./run.sh
```

#### b. uWSGI

```
uwsgi --ini uwsgi.ini
```

#### c. Docker

```
docker build . -f Dockerfile.flask -t flask:v0.1
docker run --name flask -d -p 10080:10080 flask:v0.1
```

### staging

#### docker-compose

```
docker-compose up -d
```

## API

```
curl 127.0.0.1:5000/api/v1/users/<name>
```

### Swagger UI

http://<swagger_host>/apidocs/

in development,
```
http://127.0.0.1:5000/apidocs/
```

## lint / format

```
pysen run lint
pysen run format
```

## test

```
./run-test.sh
```