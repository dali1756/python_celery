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
## 測試方式
透過`/tasks`API 產生 task id，可以到`/tasks/{task_id}`API 測試回應內容，或是透過`/schedule_task`API 手動執行排程等待一分鐘後所產生的 task id，再回到`/tasks/{task_id}`API 做測試。
