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
        # ---------------- DATE HANDLING ----------------
        start = datetime.strptime(request.start_date, "%Y-%m-%d")
        end = datetime.strptime(request.end_date, "%Y-%m-%d")

        if end <= start:
            raise ValueError("End date must be after start date")

        nights = (end - start).days
        total_days = nights + 1  # Important for itinerary

        # ---------------- FLIGHT ----------------
        flight_msg = create_message(
            sender="planner",
            receiver="flight_agent",
            intent="REQUEST",
            payload={
                "destination": request.destination,
                "start_date": request.start_date,
                "end_date": request.end_date,
            },
        )
        flight_response = await self.flight_agent.receive(flight_msg)

        # ---------------- HOTEL ----------------
        hotel_msg = create_message(
            sender="planner",
            receiver="hotel_agent",
            intent="REQUEST",
            payload={
                "destination": request.destination,
                "nights": nights,
                "start_date": request.start_date,
                "end_date": request.end_date,
            },
        )
        hotel_response = await self.hotel_agent.receive(hotel_msg)

        # ---------------- WEATHER ----------------
        weather_msg = create_message(
            sender="planner",
            receiver="weather_agent",
            intent="REQUEST",
            payload={"destination": request.destination},
        )
        weather_response = await self.weather_agent.receive(weather_msg)

        # ---------------- COSTS ----------------
        flight_cost = flight_response.payload["flight_cost"]
        hotel_cost = hotel_response.payload["hotel_cost"]

        flight_quality = flight_response.payload["flight_quality"]
        hotel_quality = hotel_response.payload["hotel_quality"]

        # ---------------- OPTIMIZATION ----------------
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

        # ---------------- SENSITIVITY ----------------
        sensitivity = self.optimizer.sensitivity_analysis(
            flight_cost=flight_cost,
            hotel_cost=hotel_cost,
            flight_quality=flight_quality,
            hotel_quality=hotel_quality,
            user_budget=request.budget,
        )

        # ---------------- ITINERARY ----------------
        itinerary_msg = create_message(
            sender="planner",
            receiver="itinerary_agent",
            intent="REQUEST",
            payload={
                "destination": request.destination,
                "forecast": weather_response.payload["forecast"],
                "start_date": request.start_date,
                "end_date": request.end_date,
                "total_days": total_days,
                "budget_status": status,
                "allocated_budget": final_total,
            },
        )

        itinerary_response = await self.itinerary_agent.receive(itinerary_msg)

        # ---------------- FINAL RESPONSE ----------------
        return {
            "destination": request.destination,
            "start_date": request.start_date,
            "end_date": request.end_date,
            "total_days": total_days,
            "allocated_budget": final_total,
            "status": status,
            "flight_cost": flight_cost,
            "hotel_cost": hotel_cost,
            "itinerary": itinerary_response.payload["itinerary"],
            "sensitivity_analysis": sensitivity,
        }