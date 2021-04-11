
## DB初期化

```
export FLASK_APP=myapp/cli.py
export APP_ENV=development
flask init-db
```

## アプリケーション起動

### development
#### Flask直接起動

```
./run.sh
```

#### uwsgiで起動

```
uwsgi --ini uwsgi.ini
```

#### Dockerで起動

```
docker build . -f Dockerfile.flask -t flask:v0.1
docker run --name flask -d -p 10080:10080 flask:v0.1
```

### staging

#### docker-compose

```
docker-compose up -d
```