# 🧠 AI Workflow Engine – Minimal Agent Graph System

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green?logo=fastapi)
![Workflow-Engine](https://img.shields.io/badge/Engine-Workflow%20Orchestration-orange)
![Assignment](https://img.shields.io/badge/Internship-Backend%20Assignment-blueviolet)

A lightweight, modular **workflow engine** inspired by LangGraph.  
Built as part of the **AI Engineering Internship Assignment**, this project demonstrates clean backend design, workflow orchestration, and API-driven execution.

---

## 📘 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Workflow Example](#workflow-example)
- [Tech Stack](#tech-stack)
- [API Endpoints](#api-endpoints)
- [Installation](#installation)
- [How It Works](#how-it-works)
- [Future Enhancements](#future-enhancements)
- [Author](#author)

---

## 1.🔍 Overview

This project implements a **minimal workflow/graph engine** where:

- Each step is a **node** (a Python function)  
- Nodes pass data via a shared **state dictionary**  
- Execution order is controlled using **edges**  
- The workflow can branch, loop, and update state  
- The entire system is exposed through a clean **FastAPI API**

---

## 2.🚀 Features

- 🧩 Create and execute workflows dynamically  
- 🔄 Step-by-step execution with shared state  
- 🌿 Branching & looping–ready design  
- 📝 Node-by-node execution logs  
- ⚡ FastAPI-powered REST endpoints  
- 🛠 Easily extend with custom tools/nodes  
- 📦 Clean, modular architecture  

---

## 3.🏗 Architecture

Client → FastAPI → Workflow Engine → Nodes → State → Output

### Components

| Component   | Description |
|-------------|-------------|
| **Nodes**   | Python functions performing tasks |
| **State**   | A dict passed between nodes |
| **Edges**   | Defines the workflow execution sequence |
| **Engine**  | Executes nodes in order and updates state |
| **Store**   | In-memory graph & run tracking |
| **API Layer** | FastAPI endpoints for graph CRUD & execution |

---

## 4🧪 Workflow Example: Code Review Mini-Agent

This project includes a ready-to-use workflow that:

1. Extracts function count  
2. Calculates code complexity  
3. Detects issues  
4. Suggests improvements  
5. Returns a final `quality_score`

### Example Output
```json```
{
"functions": 3,
"complexity": 6,
"issues": 2,
"quality_score": 74
}


---

## 5. 🧩 Tech Stack

| Layer       | Technology                        |
|-------------|------------------------------------|
| **Backend** | FastAPI                            |
| **Language** | Python 3.10+                      |
| **Server**  | Uvicorn                            |
| **Storage** | In-memory state store              |
| **Docs**    | Swagger UI (FastAPI)               |
| **Engine**  | Custom Workflow Orchestrator       |
| **Design**  | Node → State → Transition graph    |

---

## 6. 📡 API Endpoints

- **POST /graph/create** — Create a workflow graph (returns `graph_id`)  
- **POST /graph/run** — Run a saved graph with an initial state (returns `run_id`, `final_state`, `log`)  
- **GET /graph/state/{run_id}** — Fetch stored workflow result/state

Swagger docs available at: **http://127.0.0.1:8000/docs**

---

##  7. ⚙ Installation

```bash```
git clone https://github.com/<your-username>/ai-workflow-engine.git
cd ai-workflow-engine

python -m venv .venv
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
# macOS / Linux:
# source .venv/bin/activate

pip install -r requirements.txt

python -m uvicorn app.main:app --reload


---

## 8. 🧠 How It Works

### Node Example

```python```
def extract_functions(state):
    code = state.get("code", "")
    state["functions"] = code.count("def")
    return state

### Engine Flow

1.)Load workflow graph.

2.)Start at defined start node.

3.)Execute node → update shared state

4.)Follow edges to next node.

5.)Continue until end of workflow.

6.)Return final state + execution log.

7.)Execution sequence example:

extract → complexity → issues → suggest → final

### 9. Future Enhancements

🔁 Looping support (run-until conditions)

🌿 Conditional branching (if/else execution paths)

🧵 Async node execution for long-running tasks

📡 WebSocket real-time logs

🗄 Database-backed graph storage (SQLite/Postgres)

🤖 LLM-powered agent nodes

📊 Dashboard UI for workflow visualization

### 10. Author

Aryan Vimal Ejantkar
B.Tech AIML — VIT Bhopal
Passionate about backend engineering, workflow automation, and AI system design.




