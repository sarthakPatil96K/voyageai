from app.agents.base_agent import BaseAgent
from app.protocol.message_schema import create_message, AgentMessage
import random


class WeatherAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="weather_agent")

    async def handle(self, message: AgentMessage) -> AgentMessage:
        forecast = random.choice(["Sunny", "Cloudy", "Rainy"])

        return create_message(
            sender=self.name,
            receiver=message.sender,
            intent="RESPONSE",
            payload={
                "forecast": forecast,
            },
        )