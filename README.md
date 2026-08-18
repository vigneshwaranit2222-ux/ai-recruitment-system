# AI Career Assistant Platform 🚀

[![Python Version](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-009688.svg)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16%20%2B%20pgvector-336791.svg)](https://github.com/pgvector/pgvector)
[![Redis](https://img.shields.io/badge/Redis-7-DC382D.svg)](https://redis.io/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](#license)

An enterprise-grade, multi-modal **AI Career Assistant Platform** engineered with an asynchronous Clean Architecture design using **FastAPI**, **SQLAlchemy 2.0 (asyncpg)**, **PostgreSQL with pgvector**, **Redis**, **Hugging Face Serverless Inference**, **OpenAI Embeddings**, and multi-interface support (FastAPI REST API, Static HTML5 SPA, and Streamlit Dashboard).

---

## 📌 Features & Core Capabilities

- 🤖 **Interactive AI Career Chatbot**: RAG-enhanced conversational agent powered by Hugging Face Serverless Router (`Qwen/Qwen2.5-72B-Instruct`) with streaming & non-streaming support.
- 📄 **Resume Parsing & Scoring**: Automated PDF & DOCX document processing with real-time feedback, skill extraction, and scoring against target job profiles.
- 🎯 **Job Matching & Skill Gap Analysis**: Intelligent skill matching engine utilizing structured occupational datasets (e.g. O*NET).
- 🗺️ **Personalized Career Roadmaps**: Dynamic career progression roadmap builder providing step-by-step milestones and target skill acquisition goals.
- 🎙️ **AI Mock Interview Simulator**: Interactive mock interview experience supporting speech-to-text (STT) and text-to-speech (TTS) workflows.
- 🧠 **Vector RAG Engine**: Native PostgreSQL `pgvector` vector store supporting cosine distance similarity (`<=>`) top-K retrieval and grounding metadata citations.
- ⚡ **Real-time WebSockets**: Async live streaming communication channel for real-time interaction.
- 🖥️ **Dual UI Interfaces**:
  - Web Single Page Application (HTML/CSS/JS) mounted at `/`.
  - Rich interactive Streamlit Dashboard (`streamlit_app.py`).

---

## 🛠️ Technology Stack

| Layer | Technology |
| :--- | :--- |
| **Framework / Server** | Python 3.11+, FastAPI 0.110+, Uvicorn |
| **Database & ORM** | PostgreSQL 16 (`pgvector`), SQLAlchemy 2.0 (asyncio), asyncpg, Alembic |
| **Cache & Queue** | Redis 7 |
| **LLM & AI Orchestration** | Hugging Face Router API (`Qwen/Qwen2.5-72B-Instruct`), OpenAI Embeddings (`text-embedding-3-small`), Pydantic v2 |
| **Speech & Vision** | Whisper / Speech Adapters, Gemini / Vision Adapters |
| **Frontend UI** | HTML5 / Vanilla CSS SPA, Streamlit Dashboard |
| **DevOps & Testing** | Docker, Docker Compose, Pytest (Asyncio), Pytest-Cov |

---

## 📁 Project Directory Structure

```text
AI_Career_Assistant/
├── app/
│   ├── main.py              # FastAPI application entry point & router mounting
│   ├── adapters/            # LLM, Speech, Vision, & external service adapters
│   ├── agents/              # Autonomous AI agent implementations
│   ├── ai/                  # Prompt builders & AI helpers
│   ├── core/                # System configuration, security, & logging
│   ├── database/            # Database session, base models, & migration initializers
│   ├── domain/              # Business logic entities & domain definitions
│   ├── middleware/          # Request context & correlation tracking middleware
│   ├── models/              # SQLAlchemy 2.0 ORM models
│   ├── orchestrators/       # Chat & multi-modal orchestrators
│   ├── rag/                 # Vector retriever, text splitters, & RAG pipelines
│   ├── repositories/        # Database & Vector storage repositories
│   ├── routers/             # API endpoint routers (Auth, Chat, Resume, Jobs, etc.)
│   ├── schemas/             # Pydantic data validation schemas
│   ├── security/            # JWT authentication & password hashing utilities
│   └── services/            # Core business services
├── static/                  # Single Page Application (HTML/CSS/JS)
├── scripts/                 # Ingestion & maintenance scripts
├── datasets/                # O*NET & technical career datasets
├── tests/                   # Automated Pytest suite (33+ test suites)
├── Dockerfile               # Production Docker image configuration
├── docker-compose.yml       # Multi-container orchestration (App, PGVector, Redis)
├── pyproject.toml           # Project metadata & dependencies
├── requirements.txt         # Pip dependency locks
└── streamlit_app.py         # Interactive Streamlit dashboard
```

---

## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed on your system:
- **Python 3.11+**
- **Docker Desktop** (for containerized PostgreSQL + pgvector and Redis)
- **Git**

---

### 1. Environment Configuration

Copy `.env.example` to `.env` and update the environment variables:

```bash
cp .env.example .env
```

Configure key variables in `.env`:

```env
# App Settings
APP_NAME="AI Career Assistant Platform"
ENVIRONMENT="development"
DEBUG=true

# Database (PostgreSQL with pgvector)
DATABASE_URL="postgresql+asyncpg://postgres:Vignesh%40123@localhost:5433/chatbot_db"

# Redis
REDIS_URL="redis://localhost:6379/0"

# AI & LLM Integration
LLM_PROVIDER="huggingface" # options: huggingface, openai, mock
HF_TOKEN="your-huggingface-api-token"
LLM_MODEL="Qwen/Qwen2.5-72B-Instruct"

# Vector Embeddings
EMBEDDING_PROVIDER="openai" # options: openai, sentence_transformers, mock
OPENAI_API_KEY="your-openai-api-key"
EMBEDDING_MODEL="text-embedding-3-small"
```

---

### 2. Running with Docker Compose (Recommended)

To start the database (`pgvector`), Redis server, and the application container together:

```bash
docker-compose up -d --build
```

Access the application at:
- **Web SPA Interface**: [http://localhost:8000/](http://localhost:8000/)
- **Interactive OpenAPI Documentation**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc Documentation**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

### 3. Local Development Setup

If you prefer to run the FastAPI app directly on your host machine:

#### Step 1: Start Infrastructure Containers

Start PostgreSQL + pgvector and Redis using Docker Compose:

```bash
docker-compose up -d db redis
```

#### Step 2: Set Up Python Virtual Environment

```bash
python -m venv .venv

# On Windows (PowerShell):
.venv\Scripts\Activate.ps1

# On Linux/macOS:
source .venv/bin/activate
```

#### Step 3: Install Dependencies

```bash
pip install -e .
```

#### Step 4: Launch FastAPI Backend Server

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

---

### 4. Running the Streamlit Dashboard

To launch the multi-modal Streamlit UI dashboard:

```bash
streamlit run streamlit_app.py
```

Streamlit will open automatically at [http://localhost:8501](http://localhost:8501).

---

## 📡 API Endpoint Overview

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/health` | Application health & database readiness check |
| `POST` | `/api/v1/auth/register` | Register a new user account |
| `POST` | `/api/v1/auth/token` | Authenticate user & obtain JWT access token |
| `POST` | `/api/v1/chat/` | Send message to AI Career Assistant (RAG context) |
| `POST` | `/api/v1/resume/upload` | Upload & parse resume document (PDF/DOCX) |
| `POST` | `/api/v1/jobs/match` | Perform job matching & skill gap analysis |
| `POST` | `/api/v1/roadmap/generate` | Generate personalized career acquisition roadmap |
| `POST` | `/api/v1/interview/session` | Initialize AI Mock Interview practice session |
| `POST` | `/api/v1/documents/ingest` | Ingest RAG documents into vector store |
| `GET` | `/api/v1/rag/search` | Execute vector similarity search |
| `WS` | `/api/v1/ws` | Real-time WebSocket connection for streaming chat |

---

## 🧪 Running Tests

The test suite covers endpoints, authentication, database ORM, RAG retriever, and service layers.

Run all tests with `pytest`:

```bash
pytest
```

Run tests with code coverage report:

```bash
pytest --cov=app --cov-report=term-missing
```

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).
