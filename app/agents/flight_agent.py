from app.agents.base_agent import BaseAgent
from app.protocol.message_schema import create_message, AgentMessage
import random


class FlightAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="flight_agent")

    async def handle(self, message: AgentMessage) -> AgentMessage:
        destination = message.payload.get("destination")

        max_budget = None
        if message.constraints:
            max_budget = message.constraints.get("max_flight_cost")

        base_price = random.randint(5000, 15000)
        quality_score = random.uniform(3.0, 5.0)

        if max_budget is not None:
            base_price = min(base_price, max_budget)

        return create_message(
            sender=self.name,
            receiver=message.sender,
            intent="RESPONSE",
            payload={
                "destination": destination,
                "flight_cost": base_price,
                "flight_quality": quality_score,
                "airline": "MockAir",
            },
        )