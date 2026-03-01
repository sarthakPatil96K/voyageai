from fastapi import APIRouter
from app.api.schemas import TravelRequest, TravelResponse

router = APIRouter()


@router.get("/")
async def health_check():
    return {"status": "VoyageAI running 🚀"}


from app.core.planner import Planner

planner = Planner()


@router.post("/plan")
async def plan_trip(request: TravelRequest):
    result = await planner.plan_trip(request)
    return result

from app.core.planner import Planner
from app.api.schemas import TravelRequest

planner = Planner()

@router.post("/optimize-only")
async def optimize_only(request: TravelRequest):
    result = await planner.plan_trip(request)

    return {
        "flight_cost": result.get("flight_cost"),
        "hotel_cost": result.get("hotel_cost"),
        "total_budget": result.get("total_budget"),
        "status": result.get("status"),
        "sensitivity_analysis": result.get("sensitivity_analysis"),
    }