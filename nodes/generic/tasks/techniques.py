from nodes import app

@app.task(name='nodes.c2.generic.techniques.run')
def run_technique(agent_id: str = None):
    ''' Run selected technique on agent(s) '''
    return 'http_response'

