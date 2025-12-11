from typing import Callable, Dict, Optional


class WorkflowEngine:
    """
    Executes a workflow graph by running nodes in a specified order.
    """

    def __init__(self, nodes: Dict[str, Callable], edges: Dict[str, Optional[str]], start_node: str):
        self.nodes = nodes
        self.edges = edges
        self.start_node = start_node

    def run(self, state: Dict):
        log = []
        current = self.start_node

        while current is not None:
            log.append(f"Running node: {current}")

            node_fn = self.nodes[current]
            output = node_fn(state)

            # Merge output into the state
            if output:
                state.update(output)

            current = self.edges.get(current)

        return {"final_state": state, "log": log}
