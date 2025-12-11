from fastapi import FastAPI
from app.schemas import RunRequest
from app.graph_engine.engine import WorkflowEngine
from app.graph_engine.graph_store import save_graph, get_graph, save_run, get_run
from app.workflows.code_review_flow import create_code_review_workflow

app = FastAPI()


@app.post("/graph/create")
def create_graph():
    """
    Creates a graph using the sample Code Review Workflow
    """
    nodes, edges, start = create_code_review_workflow()

    graph_id = save_graph({
        "nodes": nodes,
        "edges": edges,
        "start": start
    })

    return {"graph_id": graph_id}


@app.post("/graph/run")
def run_graph(request: RunRequest):
    """
    Runs the workflow graph with initial state.
    """
    graph = get_graph(request.graph_id)

    engine = WorkflowEngine(
        nodes=graph["nodes"],
        edges=graph["edges"],
        start_node=graph["start"]
    )

    result = engine.run(request.initial_state)

    run_id = save_run(result["final_state"])

    return {
        "run_id": run_id,
        "final_state": result["final_state"],
        "log": result["log"]
    }


@app.get("/graph/state/{run_id}")
def fetch_run_state(run_id: str):
    """
    Fetches the state of a previously executed workflow.
    """
    return get_run(run_id)
