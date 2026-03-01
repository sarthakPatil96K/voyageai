from pydantic import BaseModel
from typing import List, Dict, Any

alpha: float | None = 1.0
beta: float | None = 2000.0

class TravelRequest(BaseModel):
    source: str
    destination: str
    start_date: str
    end_date: str
    budget: float
    preferences: str | None = None
    alpha: float | None = 1.0
    beta: float | None = 2000.0


class TravelResponse(BaseModel):
    destination: str
    total_budget: float
    status: str
    flight_cost: float
    hotel_cost: float
    itinerary: str
    sensitivity_analysis: List[Dict[str, Any]]