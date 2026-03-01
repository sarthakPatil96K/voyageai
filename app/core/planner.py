from datetime import datetime
from app.protocol.message_schema import create_message
from app.agents.flight_agent import FlightAgent
from app.agents.hotel_agent import HotelAgent
from app.agents.weather_agent import WeatherAgent
from app.agents.budget_agent import BudgetAgent
from app.agents.itinerary_agent import ItineraryAgent


class Planner:
    def __init__(self):
        self.flight_agent = FlightAgent()
        self.hotel_agent = HotelAgent()
        self.weather_agent = WeatherAgent()
        self.budget_agent = BudgetAgent()
        self.itinerary_agent = ItineraryAgent()

    async def plan_trip(self, request):
        # Calculate nights
        start = datetime.strptime(request.start_date, "%Y-%m-%d")
        end = datetime.strptime(request.end_date, "%Y-%m-%d")
        nights = (end - start).days

        # --- Flight Agent ---
        flight_msg = create_message(
            sender="planner",
            receiver="flight_agent",
            intent="REQUEST",
            payload={"destination": request.destination},
        )
        flight_response = await self.flight_agent.receive(flight_msg)

        # --- Hotel Agent ---
        hotel_msg = create_message(
            sender="planner",
            receiver="hotel_agent",
            intent="REQUEST",
            payload={"nights": nights},
        )
        hotel_response = await self.hotel_agent.receive(hotel_msg)

        # --- Weather Agent ---
        weather_msg = create_message(
            sender="planner",
            receiver="weather_agent",
            intent="REQUEST",
            payload={"destination": request.destination},
        )
        weather_response = await self.weather_agent.receive(weather_msg)

        # --- Initial Cost Calculation ---
        flight_cost = flight_response.payload["flight_cost"]
        hotel_cost = hotel_response.payload["hotel_cost"]

        max_attempts = 4
        attempt = 0

        while attempt < max_attempts:
            total_cost = flight_cost + hotel_cost

            if total_cost <= request.budget:
                break

            # Determine highest contributor
            if hotel_cost >= flight_cost:
                # Ask hotel agent to reduce cost
                reduction_target = request.budget - flight_cost

                hotel_msg = create_message(
                    sender="planner",
                    receiver="hotel_agent",
                    intent="NEGOTIATE",
                    payload={"nights": nights},
                    constraints={"max_hotel_cost": reduction_target},
                )

                hotel_response = await self.hotel_agent.receive(hotel_msg)
                hotel_cost = hotel_response.payload["hotel_cost"]

            else:
                # Ask flight agent to reduce cost
                reduction_target = request.budget - hotel_cost

                flight_msg = create_message(
                    sender="planner",
                    receiver="flight_agent",
                    intent="NEGOTIATE",
                    payload={"destination": request.destination},
                    constraints={"max_flight_cost": reduction_target},
                )

                flight_response = await self.flight_agent.receive(flight_msg)
                flight_cost = flight_response.payload["flight_cost"]

            attempt += 1

        # Final status
        final_total = flight_cost + hotel_cost
        status = "WITHIN_BUDGET" if final_total <= request.budget else "OVER_BUDGET"

        # --- Itinerary Agent ---
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
        }