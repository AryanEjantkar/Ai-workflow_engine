from pydantic import BaseModel
from typing import Dict


class RunRequest(BaseModel):
    graph_id: str
    initial_state: Dict
