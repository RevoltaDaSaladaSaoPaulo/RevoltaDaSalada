

from celery import task
import importPost
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

import djcelery

djcelery.setup_loader()
BROKER_URL = 'amqp://guest:guest@localhost:5672/'

from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    'import-every-30-seconds': {
        'task': 'tasks.import_instagram',
        'schedule': timedelta(seconds=30)
    },
}

CELERY_TIMEZONE = 'UTC'

@task()
def import_instagram():
    logger.info('Importing Instagram...')
    importPost.import_instagram()
