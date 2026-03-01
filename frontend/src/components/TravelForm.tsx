import { useState } from "react";
import { planTrip } from "../api/travelApi";
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
    budget: 0,
    preferences: "",
  });

  const [result, setResult] = useState<TravelResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleChange = (e: any) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e: any) => {
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

        <input
          type="number"
          name="budget"
          placeholder="Budget"
          className="w-full border p-2 rounded"
          onChange={handleChange}
          required
        />

        <textarea
          name="preferences"
          placeholder="Preferences (optional)"
          className="w-full border p-2 rounded"
          onChange={handleChange}
        />

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