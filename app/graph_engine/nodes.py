def extract_functions(state):
    """
    Count function definitions in the code.
    """
    code = state.get("code", "")
    functions = code.count("def")

    return {"functions": functions}


def check_complexity(state):
    """
    Fake rule: complexity = number of functions * 2
    """
    complexity = state["functions"] * 2
    return {"complexity": complexity}


def detect_issues(state):
    """
    Fake rule: more functions = fewer issues
    """
    issues = max(0, 5 - state["functions"])
    return {"issues": issues}


def suggest_improvements(state):
    """
    Final quality score based on simple heuristics
    """
    score = 100 - (state["complexity"] + state["issues"] * 10)
    return {"quality_score": score}
