from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpStatus, value


class BudgetOptimizer:
    def optimize(
        self,
        flight_cost: float,
        hotel_cost: float,
        user_budget: float,
    ):
        # Create LP problem
        problem = LpProblem("TravelBudgetOptimization", LpMinimize)

        # Decision variables
        x_flight = LpVariable("flight_cost", lowBound=3000)
        x_hotel = LpVariable("hotel_cost", lowBound=5000)

        # Objective: minimize total cost
        problem += lpSum([x_flight, x_hotel])

        # Constraints
        problem += x_flight + x_hotel <= user_budget
        problem += x_flight <= flight_cost
        problem += x_hotel <= hotel_cost

        # Solve
        problem.solve()

        if LpStatus[problem.status] != "Optimal":
            return None

        return {
            "flight_cost": value(x_flight),
            "hotel_cost": value(x_hotel),
            "total_cost": value(x_flight) + value(x_hotel),
        }