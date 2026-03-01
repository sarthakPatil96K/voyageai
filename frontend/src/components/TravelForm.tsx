import { useState, useEffect } from "react";
import { planTrip, optimizeOnly } from "../api/travelApi";
import type { TravelRequest, TravelResponse } from "../types/travel";
import Loader from "./Loader";
import ErrorMessage from "./ErrorMessage";
import TravelResult from "./TravelResult";

export default function TravelForm() {
  const [formData, setFormData] = useState<TravelRequest>({
    source: "",
    destination: "",
    start_date: "",
    end_date: "",
    budget: 30000,
    preferences: "",
    alpha: 1,
    beta: 2000,
  });

  const [result, setResult] = useState<TravelResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>
  ) => {
    const { name, value, type } = e.target;

    setFormData((prev) => ({
      ...prev,
      [name]:
        type === "number" || type === "range"
          ? Number(value)
          : value,
    }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError("");
    setResult(null);

    try {
      const response = await planTrip(formData);
      setResult(response);
    } catch (err: any) {
      setError(err.message);
    }

    setLoading(false);
  };

  // 🔥 Dynamic Budget Optimization
  useEffect(() => {
    if (!result) return; // Only after initial plan

    const timeout = setTimeout(async () => {
      try {
        const optimized = await optimizeOnly(formData);
        setResult((prev) =>
          prev
            ? {
                ...prev,
                flight_cost: optimized.flight_cost,
                hotel_cost: optimized.hotel_cost,
                total_budget: optimized.total_budget,
                status: optimized.status,
                sensitivity_analysis:
                  optimized.sensitivity_analysis,
              }
            : null
        );
      } catch (err) {
        console.error("Live optimization failed");
      }
    }, 500); // debounce

    return () => clearTimeout(timeout);
  }, [formData.budget, formData.beta]);

  const betaValue = formData.beta ?? 2000;

  const preferenceLabel =
    betaValue < 1500
      ? "Budget Focused"
      : betaValue < 3000
      ? "Balanced"
      : "Luxury Focused";

  return (
    <div className="bg-white p-6 rounded-lg shadow-md max-w-xl mx-auto">
      <form onSubmit={handleSubmit} className="space-y-4">

        <input
          type="text"
          name="source"
          placeholder="Source"
          className="w-full border p-2 rounded"
          onChange={handleChange}
          required
        />

        <input
          type="text"
          name="destination"
          placeholder="Destination"
          className="w-full border p-2 rounded"
          onChange={handleChange}
          required
        />

        <input
          type="date"
          name="start_date"
          className="w-full border p-2 rounded"
          onChange={handleChange}
          required
        />

        <input
          type="date"
          name="end_date"
          className="w-full border p-2 rounded"
          onChange={handleChange}
          required
        />

        {/* 🎚 Budget Slider */}
        <div>
          <label className="block text-sm font-medium">
            Budget: ₹{formData.budget}
          </label>
          <input
            type="range"
            min="10000"
            max="100000"
            step="1000"
            name="budget"
            value={formData.budget}
            onChange={handleChange}
            className="w-full mt-2"
          />
        </div>

        {/* 🎚 Luxury Slider */}
        <div>
          <label className="block text-sm font-medium">
            Cost ↔ Luxury Preference
          </label>
          <input
            type="range"
            min="500"
            max="5000"
            step="100"
            name="beta"
            value={formData.beta}
            onChange={handleChange}
            className="w-full mt-2"
          />
          <div className="text-sm mt-1 font-medium">
            {preferenceLabel}
          </div>
        </div>

        <button
          type="submit"
          className="bg-blue-600 text-white px-4 py-2 rounded w-full hover:bg-blue-700"
        >
          Generate Plan
        </button>
      </form>

      {loading && <Loader />}
      {error && <ErrorMessage message={error} />}
      {result && <TravelResult result={result} />}
    </div>
  );
}