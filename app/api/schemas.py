from pydantic import BaseModel
from typing import Optional


class TravelRequest(BaseModel):
    source: str
    destination: str
    start_date: str
    end_date: str
    budget: float
    preferences: Optional[str] = None


class TravelResponse(BaseModel):
    destination: str
    total_budget: float
    status: str
    flight_cost: float
    hotel_cost: float
    itinerary: str