import logging
from nodes.main import rediscache

rediscache.delete('cache-empiretoken')
empirelog = logging.getLogger('rtempire')
