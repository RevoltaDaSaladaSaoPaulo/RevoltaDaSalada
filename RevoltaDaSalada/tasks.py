

from celery import task
import importPost
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@task(name="tasks.import_instagram")
def import_instagram():
    logger.info('Importing Instagram...')
    importPost.import_instagram()
