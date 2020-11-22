from celery.schedules import crontab
from nodes import app
from yaml import safe_load_all
import glob

nodes_available = []
for config_file in glob.glob('nodes/*/config.yml', recursive=True):
    with open(config_file) as yamlfile:
        yaml_objects = safe_load_all(yamlfile.read())
        for node_config in yaml_objects:
            nodes_available.append(node_config)

@app.task(name='nodes.system.get')
def get_nodes() -> list:
    ''' Return list of nodes '''
    print(nodes_available)
    return nodes_available
