# Overview

Flask Sample Application on Clean Architecture.


# Requirements

* Python 3.9

# How to use
## initialize DB

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

## lint / format

```
pysen run lint
pysen run format
```

## test

```
export APP_ENV=test
pytest -v --cov=app
```