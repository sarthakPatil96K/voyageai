import TravelForm from "../components/TravelForm";

export default function Home() {
  return (
    <div className="min-h-screen bg-gray-100 p-10">
      <h1 className="text-3xl font-bold text-center mb-8">
        VoyageAI ✈️
      </h1>
      <TravelForm />
    </div>
  );
}