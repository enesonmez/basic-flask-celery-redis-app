from celery.utils.log import get_task_logger

import time

from app import celeryApp, client


logger = get_task_logger(__name__)

@celeryApp.task()
def wait_add(x,y):
    logger.info('Starting work')
    time.sleep(15)
    logger.info('Finished work')
    return x + y

@celeryApp.task()
def slack_message(channel_id):
    time.sleep(8)
    logger.info('Sending...')
    client.chat_postMessage(channel=channel_id, text='This is only a test.')
    logger.info('Sended...')
    return True