export interface TravelRequest {
  source: string;
  destination: string;
  start_date: string;
  end_date: string;
  budget: number;
  preferences?: string;
}

export interface TravelResponse {
  destination: string;
  total_budget: number;
  status: string;
  flight_cost: number;
  hotel_cost: number;
  itinerary: string;
}