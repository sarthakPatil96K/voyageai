from pydantic import BaseModel
from typing import Any, Dict
from uuid import uuid4
from datetime import datetime


class AgentMessage(BaseModel):
    message_id: str
    sender: str
    receiver: str
    intent: str  # REQUEST | RESPONSE | NEGOTIATE
    payload: Dict[str, Any]
    constraints: Dict[str, Any] | None = None
    timestamp: str


def create_message(
    sender: str,
    receiver: str,
    intent: str,
    payload: Dict[str, Any],
    constraints: Dict[str, Any] | None = None,
) -> AgentMessage:
    return AgentMessage(
        message_id=str(uuid4()),
        sender=sender,
        receiver=receiver,
        intent=intent,
        payload=payload,
        constraints=constraints,
        timestamp=str(datetime.utcnow()),
    )