from app.agents.base_agent import BaseAgent
from app.protocol.message_schema import create_message, AgentMessage
from app.rag.itinerary_rag import ItineraryRAG


class ItineraryAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="itinerary_agent")
        self.rag = ItineraryRAG()

    async def handle(self, message: AgentMessage) -> AgentMessage:
        data = message.payload  # ✅ Proper extraction

        itinerary = self.rag.generate_itinerary(
            destination=data.get("destination"),
            forecast=data.get("forecast"),
            start_date=data.get("start_date"),
            end_date=data.get("end_date"),
            total_days=data.get("total_days"),
            budget_status=data.get("budget_status"),
            allocated_budget=data.get("allocated_budget"),
        )

        return create_message(
            sender=self.name,
            receiver=message.sender,
            intent="RESPONSE",
            payload={"itinerary": itinerary},
        )