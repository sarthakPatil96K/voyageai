from app.agents.base_agent import BaseAgent
from app.protocol.message_schema import create_message, AgentMessage


class BudgetAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="budget_agent")

    async def handle(self, message: AgentMessage) -> AgentMessage:
        flight_cost = message.payload.get("flight_cost", 0)
        hotel_cost = message.payload.get("hotel_cost", 0)
        user_budget = message.payload.get("user_budget", 0)

        total_cost = flight_cost + hotel_cost

        status = "WITHIN_BUDGET"
        if total_cost > user_budget:
            status = "OVER_BUDGET"

        return create_message(
            sender=self.name,
            receiver=message.sender,
            intent="RESPONSE",
            payload={
                "total_cost": total_cost,
                "status": status,
            },
        )