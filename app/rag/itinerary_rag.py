import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


class ItineraryRAG:
    def __init__(self):
        # GROQ CLIENT
        self.client = OpenAI(
            api_key=os.getenv("GROQ_API_KEY"),
            base_url="https://api.groq.com/openai/v1",
        )

    def generate_itinerary(
        self,
        destination,
        forecast,
        start_date,
        end_date,
        total_days,
        budget_status,
        allocated_budget,
    ):
        prompt = f"""
You are a professional global travel planner.

Destination: {destination}
Travel Dates: {start_date} to {end_date}
Trip Duration: {total_days} days
Weather Forecast: {forecast}
Budget Status: {budget_status}
Allocated Budget: ₹{allocated_budget}

IMPORTANT INSTRUCTIONS:

1. Generate EXACTLY {total_days} days.
2. Adapt activities based on weather.
3. If budget is WITHIN_BUDGET → suggest premium experiences.
4. If OVER_BUDGET → suggest affordable alternatives.
5. Keep each day balanced (morning, afternoon, evening).
6. Do NOT mention internal reasoning.
7. Keep formatting clean and structured.

FORMAT STRICTLY LIKE THIS:

## Trip Overview
Short 3-4 line overview.

## Day 1 - Title
**Morning:** ...
**Afternoon:** ...
**Evening:** ...
**Estimated Daily Spend:** ₹XXXX

## Day 2 - Title
...

(Continue until Day {total_days})

## Travel Tips
- Tip 1
- Tip 2
- Tip 3

## Estimated Total On-Ground Spend
Approximate realistic estimate for food, local travel and activities.
IMPORTANT:
Do NOT use markdown.
Do NOT use hashtags (#) or asterisks (*).
Return clean structured text only.
"""

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You generate structured, professional travel itineraries.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.6,
        )

        return response.choices[0].message.content