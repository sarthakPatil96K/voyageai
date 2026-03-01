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