# 🚀 VoyageAI

### Multi-Agent Autonomous Travel Planning System

**Negotiation-Driven | Budget Optimized | RAG-Powered | Production-Ready**

---

## 🌍 Overview

VoyageAI is an advanced AI-powered travel planning system built using a **Multi-Agent Agent-to-Agent (A2A) Protocol Architecture**.

Unlike traditional LLM chatbots, VoyageAI decomposes travel planning into specialized intelligent agents that collaborate, negotiate, and optimize to produce a fully structured travel plan.

This project demonstrates:

* Multi-agent orchestration
* Structured A2A communication protocol
* Autonomous negotiation loops
* Linear programming budget optimization
* Retrieval-Augmented Generation (RAG)
* Production-level system design

---

## 🧠 Architecture Overview

```
User Request
     ↓
Planner Agent (Orchestrator)
     ↓
--------------------------------------------------
| Flight Agent        → Cost & Timing
| Hotel Agent         → Stay Optimization
| Weather Agent       → Context Awareness
| Budget Agent        → LP Optimization
| Itinerary Agent     → RAG-Based Planning
--------------------------------------------------
     ↓
Negotiation Engine
     ↓
Optimized Travel Plan
```

---

## 🤖 Core Features

### 1️⃣ Multi-Agent System

Each domain is handled by a specialized AI agent:

* Flight Agent
* Hotel Agent
* Weather Agent
* Budget Optimization Agent
* Itinerary Generation Agent

Agents communicate via structured JSON-based A2A protocol.

---

### 2️⃣ Agent-to-Agent (A2A) Protocol

All agents exchange messages using structured schema:

```json
{
  "message_id": "uuid",
  "sender": "flight_agent",
  "receiver": "budget_agent",
  "intent": "REQUEST | RESPONSE | NEGOTIATE",
  "payload": {},
  "constraints": {},
  "timestamp": ""
}
```

This ensures:

* Deterministic behavior
* Debuggability
* Production scalability

---

### 3️⃣ Autonomous Negotiation Engine

If total trip cost exceeds budget:

* Budget Agent requests cost reduction
* Flight/Hotel Agents adjust options
* Loop continues until feasible solution is found
* Max retry limits ensure stability

This simulates intelligent collaborative agents.

---

### 4️⃣ Linear Programming Budget Optimization

The Budget Agent uses Linear Programming to:

* Minimize total trip cost
* Satisfy budget constraints
* Maintain quality thresholds (ratings, timing)

Powered by:

* PuLP / SciPy Optimization

---

### 5️⃣ Retrieval-Augmented Generation (RAG)

The Itinerary Agent uses:

* Embeddings
* Vector database (FAISS / Pinecone)
* Travel knowledge base

Flow:
User Context → Embedding → Vector Search → Retrieved Docs → Grounded Itinerary Generation

This ensures factual, location-specific plans.

---

### 6️⃣ Personalization Memory

User preferences are stored using embeddings:

* Preferred airlines
* Budget patterns
* Travel styles
* Past trips

Future plans become adaptive and personalized.

---

## 🏗️ Tech Stack

Backend:

* Python
* FastAPI
* AsyncIO

AI:

* OpenAI / LLM APIs
* LangGraph / Custom Orchestrator
* RAG with FAISS

Optimization:

* PuLP (Linear Programming)

Data:

* PostgreSQL
* Redis (Pub/Sub & Caching)

Deployment:

* Docker
* AWS (EC2 / ECS)

---

## 📂 Project Structure

```
voyageai/
│
├── app/
│   ├── agents/
│   ├── core/
│   ├── optimization/
│   ├── rag/
│   ├── memory/
│   ├── protocol/
│   └── services/
│
├── database/
├── tests/
├── docker/
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/voyageai.git
cd voyageai
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Server

```bash
uvicorn app.main:app --reload
```

---

## 🧪 Example Request

```
Plan a 5-day Goa trip from Mumbai under ₹30,000 in March.
```

System will:

* Extract constraints
* Query agents
* Optimize budget
* Run negotiation loop
* Retrieve local travel knowledge
* Generate structured day-wise itinerary

---

## 🎯 Why This Project Matters

This project demonstrates:

* Advanced multi-agent system design
* AI orchestration
* Optimization modeling
* Retrieval-based LLM grounding
* Production-level backend architecture
* Fault tolerance and scalability thinking

It is suitable for:

* AI/ML Engineer roles
* Applied LLM Engineer roles
* Backend Engineer roles
* System Design interviews
* Hackathons and research prototypes

---

## 🛣️ Roadmap

* [ ] Agent framework implementation
* [ ] Negotiation engine
* [ ] Budget LP model integration
* [ ] RAG knowledge base ingestion
* [ ] Async message broker integration
* [ ] Observability & logging
* [ ] Dockerized deployment
* [ ] AWS production deployment

---

## 👨‍💻 Author

Sarthak Patil
Computer Engineer 
