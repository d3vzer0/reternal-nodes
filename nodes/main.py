from celery import Celery
from nodes.environment import config
import os
import logging
import redis

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
rediscache = redis.Redis.from_url(config['CELERY_BACKEND'])
app = Celery('nodes', backend=config['CELERY_BACKEND'], broker=config['CELERY_BROKER'])
app.conf.task_routes = {
    'nodes.*': { 'queue': 'nodes' },
    'api.*': { 'queue': 'api' }
}
