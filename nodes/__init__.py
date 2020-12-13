from .main import app

app.autodiscover_tasks([
    'nodes.empire2',
    'nodes.generic',
    'nodes.system'
])
