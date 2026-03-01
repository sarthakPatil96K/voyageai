import { API_URL } from "./config";
import type { TravelRequest } from "../types/travel";

export async function planTrip(data: TravelRequest) {
  const response = await fetch(`${API_URL}/plan`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  if (!response.ok) {
    throw new Error("Failed to generate plan");
  }

  return response.json();
}
export async function optimizeOnly(data: TravelRequest) {
  const response = await fetch(`${API_URL}/optimize-only`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  if (!response.ok) {
    throw new Error("Optimization failed");
  }

  return response.json();
}