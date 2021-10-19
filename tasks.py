from celery.utils.log import get_task_logger

import time

from app import celeryApp


logger = get_task_logger(__name__)

@celeryApp.task()
def wait_add(x,y):
    logger.info('Starting work')
    time.sleep(15)
    logger.info('Finished work')
    return x + y