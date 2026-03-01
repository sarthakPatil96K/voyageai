import type { TravelResponse } from "../types/travel";

interface Props {
  result: TravelResponse;
}

export default function TravelResult({ result }: Props) {
  return (
    <div className="mt-6 p-4 bg-green-50 rounded">
      <h3 className="text-lg font-semibold">
        Trip to {result.destination}
      </h3>

      <p>Flight Cost: ₹{result.flight_cost}</p>
      <p>Hotel Cost: ₹{result.hotel_cost}</p>
      <p>Total Cost: ₹{result.total_budget}</p>
      <p>Status: {result.status}</p>

      <div className="mt-4 whitespace-pre-line">
        {result.itinerary}
      </div>
    </div>
  );
}