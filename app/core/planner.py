from datetime import datetime
from app.protocol.message_schema import create_message
from app.agents.flight_agent import FlightAgent
from app.agents.hotel_agent import HotelAgent
from app.agents.weather_agent import WeatherAgent
from app.agents.itinerary_agent import ItineraryAgent
from app.optimization.budget_optimizer import BudgetOptimizer


class Planner:
    def __init__(self):
        self.flight_agent = FlightAgent()
        self.hotel_agent = HotelAgent()
        self.weather_agent = WeatherAgent()
        self.itinerary_agent = ItineraryAgent()
        self.optimizer = BudgetOptimizer()

    async def plan_trip(self, request):
        start = datetime.strptime(request.start_date, "%Y-%m-%d")
        end = datetime.strptime(request.end_date, "%Y-%m-%d")
        nights = (end - start).days

        # Flight
        flight_msg = create_message(
            sender="planner",
            receiver="flight_agent",
            intent="REQUEST",
            payload={"destination": request.destination},
        )
        flight_response = await self.flight_agent.receive(flight_msg)

        # Hotel
        hotel_msg = create_message(
            sender="planner",
            receiver="hotel_agent",
            intent="REQUEST",
            payload={"nights": nights},
        )
        hotel_response = await self.hotel_agent.receive(hotel_msg)

        # Weather
        weather_msg = create_message(
            sender="planner",
            receiver="weather_agent",
            intent="REQUEST",
            payload={"destination": request.destination},
        )
        weather_response = await self.weather_agent.receive(weather_msg)

        flight_cost = flight_response.payload["flight_cost"]
        hotel_cost = hotel_response.payload["hotel_cost"]

        flight_quality = flight_response.payload["flight_quality"]
        hotel_quality = hotel_response.payload["hotel_quality"]

        # Optimization
        optimized = self.optimizer.optimize(
            flight_cost=flight_cost,
            hotel_cost=hotel_cost,
            flight_quality=flight_quality,
            hotel_quality=hotel_quality,
            user_budget=request.budget,
            alpha=request.alpha or 1.0,
            beta=request.beta or 2000.0,
        )

        if optimized:
            flight_cost = optimized["flight_cost"]
            hotel_cost = optimized["hotel_cost"]
            final_total = optimized["total_cost"]
            status = "WITHIN_BUDGET"
        else:
            final_total = flight_cost + hotel_cost
            status = "OVER_BUDGET"

        # Sensitivity Analysis
        sensitivity = self.optimizer.sensitivity_analysis(
            flight_cost=flight_cost,
            hotel_cost=hotel_cost,
            flight_quality=flight_quality,
            hotel_quality=hotel_quality,
            user_budget=request.budget,
        )

        # Itinerary
        itinerary_msg = create_message(
            sender="planner",
            receiver="itinerary_agent",
            intent="REQUEST",
            payload={
                "destination": request.destination,
                "forecast": weather_response.payload["forecast"],
            },
        )
        itinerary_response = await self.itinerary_agent.receive(itinerary_msg)

        return {
            "destination": request.destination,
            "total_budget": final_total,
            "status": status,
            "flight_cost": flight_cost,
            "hotel_cost": hotel_cost,
            "itinerary": itinerary_response.payload["itinerary"],
            "sensitivity_analysis": sensitivity,
        }