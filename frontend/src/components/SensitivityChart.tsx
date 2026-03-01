import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";

interface Props {
  data: {
    budget: number;
    flight_cost?: number;
    hotel_cost?: number;
    total_cost?: number;
  }[];
}

export default function SensitivityChart({ data }: Props) {
  return (
    <div className="mt-8 bg-white p-4 rounded shadow">
      <h3 className="text-lg font-semibold mb-4">
        Budget Sensitivity Analysis
      </h3>

      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="budget" />
          <YAxis />
          <Tooltip />
          <Legend />

          <Line
            type="monotone"
            dataKey="flight_cost"
            stroke="#3b82f6"
            strokeWidth={2}
            name="Flight Cost"
          />
          <Line
            type="monotone"
            dataKey="hotel_cost"
            stroke="#10b981"
            strokeWidth={2}
            name="Hotel Cost"
          />
          <Line
            type="monotone"
            dataKey="total_cost"
            stroke="#ef4444"
            strokeWidth={2}
            name="Total Cost"
          />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}