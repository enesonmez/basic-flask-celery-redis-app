# basic-flask-celery-redis-app

## Quick start
to start Flask sever:
```bash
$ flask run
```
to start Celery asynchronous task queue:
```bash
$ celery -A tasks worker --loglevel=info
```
If the above doesn't work
```bash
$ celery -A tasks worker -l info -P eventlet
```

## Content

### Pending add example
#### Start new task

* localhost:5000/pending/start_task -> if you request this route, new task _starts_ and your unique **task_id** returns

#### Check result of task out

* localhost:5000/pending/task_result/<task_id> -> if you request this route with your unique **task_id** it returns _result_ of your task

### Send Message with Slack

* localhost:5000/send_message -> if you request this route, new task _starts_ and your unique **task_id** returns. Posts
to a slack channel in the back.

### Other
#### Check status of task out

* localhost:5000/task_status/<task_id> -> if you request this route with your unique **task_id** it returns _status_ of your task