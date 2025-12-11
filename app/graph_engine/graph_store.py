import uuid

graphs = {}
runs = {}


def save_graph(graph):
    graph_id = str(uuid.uuid4())
    graphs[graph_id] = graph
    return graph_id


def get_graph(graph_id):
    return graphs.get(graph_id)


def save_run(state):
    run_id = str(uuid.uuid4())
    runs[run_id] = state
    return run_id


def get_run(run_id):
    return runs.get(run_id)
