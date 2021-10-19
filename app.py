"""
    celery -A tasks worker --loglevel=info
    # celery -A <module> worker -l info -P eventlet
    celery -A tasks worker -l info -P eventlet
"""

from flask import Flask
from celery import Celery
from dotenv import load_dotenv

import os

ENV_PATH = '.env'
load_dotenv(dotenv_path=ENV_PATH)

CELERY_BROKER_URL = os.environ['CELERY_BROKER_URL']
CELERY_RESULT_BACKEND = os.environ['CELERY_RESULT_BACKEND']


app = Flask(__name__)
celeryApp = Celery('celer_worker', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)


@app.route('/')
def main():
    return "Celery - Redis"

@app.route('/pending/start_task')
def start_task():
    app.logger.info("Call method")
    r = celeryApp.send_task('tasks.wait_add', kwargs={'x':2,'y':2})
    app.logger.info(r.backend)
    return r.id


@app.route('/pending/task_result/<task_id>')
def task_result(task_id):
    result = celeryApp.AsyncResult(task_id).result
    return "Result of the Task " + str(result)


@app.route('/task_status/<task_id>')
def task_status(task_id):
    status = celeryApp.AsyncResult(task_id, app=celeryApp)
    print("Called status method")
    return "Status of the Task " + str(status.state)