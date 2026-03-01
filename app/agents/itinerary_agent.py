from app.agents.base_agent import BaseAgent
from app.protocol.message_schema import create_message, AgentMessage


class ItineraryAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="itinerary_agent")

    async def handle(self, message: AgentMessage) -> AgentMessage:
        destination = message.payload.get("destination")
        forecast = message.payload.get("forecast")

        plan = f"""
Day 1: Explore main attractions in {destination}
Day 2: Enjoy local cuisine
Day 3: Relax and shopping
Weather Forecast: {forecast}
"""

        return create_message(
            sender=self.name,
            receiver=message.sender,
            intent="RESPONSE",
            payload={
                "itinerary": plan.strip(),
            },
        )