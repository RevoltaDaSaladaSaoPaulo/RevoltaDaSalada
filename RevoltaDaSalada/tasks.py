from celery import task
import importPost

@task()
def import_instagram():
    importPost.import_instagram()