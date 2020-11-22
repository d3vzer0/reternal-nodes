from nodes import app

@app.task(name='nodes.conditionals.after_date')
def run_after_date(context: dict, input: str):
    '''  '''
    return 'get_indices_stats'

