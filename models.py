from pydantic import BaseModel
from typing import Optional

class Observation(BaseModel):
    log: str
    system_health: float
    step: int
    task: str


class Action(BaseModel):
    action_type: str  # scale_up, restart_service, cleanup, monitor


class Reward(BaseModel):
    value: float
    reason: str