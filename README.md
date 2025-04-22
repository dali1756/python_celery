## virtual env
```bash
$ mkdir python_celery
$ cd python_celery
$ poetry init -n
$ poetry shell
```
## install Redis
```bash
$ brew install redis
```
## start Redis
```bash
$ brew services start redis
```
## require for installation
```bash
$ poetry add fastapi uvicorn celery redis
```
## execute
```bash
$ uvicorn main:app --reload
$ celery -A app.worker worker --loglevel=info
$ celery -A app.worker beat --loglevel-info
```