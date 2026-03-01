from abc import ABC, abstractmethod
from app.protocol.message_schema import AgentMessage
from app.utils.logger import get_logger


class BaseAgent(ABC):
    def __init__(self, name: str):
        self.name = name
        self.logger = get_logger(name)

    async def receive(self, message: AgentMessage) -> AgentMessage:
        self.logger.info(
            f"Received message from {message.sender} | Intent: {message.intent}"
        )
        response = await self.handle(message)
        return response

    @abstractmethod
    async def handle(self, message: AgentMessage) -> AgentMessage:
        """
        Every agent must implement its own logic here.
        """
        pass