from app.graph_engine.nodes import (
    extract_functions,
    check_complexity,
    detect_issues,
    suggest_improvements
)


def create_code_review_workflow():
    nodes = {
        "extract": extract_functions,
        "complexity": check_complexity,
        "issues": detect_issues,
        "suggest": suggest_improvements
    }

    edges = {
        "extract": "complexity",
        "complexity": "issues",
        "issues": "suggest",
        "suggest": None
    }

    start = "extract"

    return nodes, edges, start
