
## アプリ起動

```
./run.sh
```

## uwsgiで起動

```
uwsgi --ini uwsgi.ini
```

## Dockerで起動

```
docker build . -t flask:v0.1
docker run --name flask -d -p 10080:10080 flask:v0.1
```
