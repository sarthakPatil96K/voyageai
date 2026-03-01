# app/agents/test_agent.py

from app.agents.base_agent import BaseAgent
from app.protocol.message_schema import create_message


class EchoAgent(BaseAgent):
    async def handle(self, message):
        return create_message(
            sender=self.name,
            receiver=message.sender,
            intent="RESPONSE",
            payload={"echo": message.payload},
        )