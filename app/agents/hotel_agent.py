from app.agents.base_agent import BaseAgent
from app.protocol.message_schema import create_message, AgentMessage
import random


class HotelAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="hotel_agent")

    async def handle(self, message: AgentMessage) -> AgentMessage:
        nights = message.payload.get("nights", 3)

        max_budget = None
        if message.constraints:
            max_budget = message.constraints.get("max_hotel_cost")

        cost_per_night = random.randint(2000, 6000)
        total_cost = cost_per_night * nights

        if max_budget is not None:
            total_cost = min(total_cost, max_budget)

        return create_message(
            sender=self.name,
            receiver=message.sender,
            intent="RESPONSE",
            payload={
                "hotel_cost": total_cost,
                "hotel_name": "MockStay Hotel",
            },
        )