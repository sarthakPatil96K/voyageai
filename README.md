🚀 VoyageAI

Multi-Agent Autonomous Travel Planning System

🌍 Overview

VoyageAI is an advanced AI-powered travel planner built using a Multi-Agent A2A Protocol Architecture.

It features:

🤖 Multi-agent collaboration

🔁 Autonomous negotiation loop

🧮 Linear Programming budget optimization

📚 RAG-based itinerary generation

🧠 User memory personalization

⚡ Production-ready async FastAPI backend

🧠 System Architecture
User
  ↓
Planner Agent
  ↓
------------------------------------------------
| Flight Agent
| Hotel Agent
| Weather Agent
| Budget Optimizer
| Itinerary Agent (RAG)
------------------------------------------------
  ↓
Negotiation Engine
  ↓
Final Optimized Travel Plan

🏗️ Core Features
1️⃣ Multi-Agent Architecture

Each domain (Flights, Hotels, Weather, Budget, Itinerary) is handled by an independent intelligent agent.

2️⃣ A2A Protocol

Agents communicate via structured JSON messages:

REQUEST

RESPONSE

NEGOTIATE

3️⃣ Budget Optimization

Uses Linear Programming to:

Minimize cost

Satisfy user constraints

Optimize allocation

4️⃣ RAG-Based Itinerary Generation

Embedding-based document retrieval

Context-aware generation

Grounded recommendations

5️⃣ Autonomous Negotiation

Agents collaboratively adjust:

Flight pricing

Hotel selection

Schedule optimization

🛠️ Tech Stack

Python

FastAPI

PostgreSQL

Redis

FAISS / Pinecone

Docker

OpenAI / LLM API

🚀 Getting Started
git clone https://github.com/your-username/voyageai.git
cd voyageai
pip install -r requirements.txt
uvicorn app.main:app --reload
📂 Project Structure

See /app directory for:

Agents

Negotiation engine

Optimization module

RAG pipeline

🎯 Roadmap

 Agent communication layer

 Budget optimizer integration

 RAG knowledge base

 Async negotiation engine

 Docker deployment

 AWS deployment

👨‍💻 Author

Sarthak Patil

AI/ML Engineer 