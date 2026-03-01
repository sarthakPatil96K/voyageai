from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpStatus, value


class BudgetOptimizer:
    def optimize(
        self,
        flight_cost: float,
        hotel_cost: float,
        flight_quality: float,
        hotel_quality: float,
        user_budget: float,
        alpha: float = 1.0,    # cost weight
        beta: float = 2000.0  # quality scaling weight
    ):
        problem = LpProblem("TravelBudgetOptimization", LpMinimize)

        # Decision variables
        x_flight = LpVariable("flight_cost", lowBound=3000)
        x_hotel = LpVariable("hotel_cost", lowBound=5000)

        # Multi-objective weighted function
        problem += (
            alpha * (x_flight + x_hotel)
            - beta * (flight_quality + hotel_quality)
        )

        # Constraints
        problem += x_flight + x_hotel <= user_budget
        problem += x_flight <= flight_cost
        problem += x_hotel <= hotel_cost

        problem.solve()

        if LpStatus[problem.status] != "Optimal":
            return None

        return {
            "flight_cost": float(value(x_flight)),
            "hotel_cost": float(value(x_hotel)),
            "total_cost": float(value(x_flight) + value(x_hotel)),
        }

    def sensitivity_analysis(
        self,
        flight_cost: float,
        hotel_cost: float,
        flight_quality: float,
        hotel_quality: float,
        user_budget: float,
    ):
        budgets = [
            int(user_budget * 0.8),
            user_budget,
            int(user_budget * 1.2),
        ]

        results = []

        for b in budgets:
            optimized = self.optimize(
                flight_cost=flight_cost,
                hotel_cost=hotel_cost,
                flight_quality=flight_quality,
                hotel_quality=hotel_quality,
                user_budget=b,
            )

            if optimized:
                results.append({
                    "budget": b,
                    "flight_cost": optimized["flight_cost"],
                    "hotel_cost": optimized["hotel_cost"],
                    "total_cost": optimized["total_cost"],
                })
            else:
                results.append({
                    "budget": b,
                    "status": "INFEASIBLE",
                })

        return results