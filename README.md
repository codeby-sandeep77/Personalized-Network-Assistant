# Personalized Networking Assistant

An AI-powered networking assistant that helps professionals prepare for events by extracting themes from event descriptions, generating conversation starters, and verifying facts via Wikipedia.

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | FastAPI |
| Frontend | Streamlit |
| Database | PostgreSQL (SQLite for local dev) |
| AI Models | DistilBERT + Google Gemini API |
| Testing | pytest |
| Deployment | Render + Streamlit Cloud |

## Project Structure

```
personalized-networking-assistant/
├── backend/           # FastAPI application
│   ├── api/           # API route handlers
│   ├── core/          # Config, security
│   ├── database/      # DB connection & models
│   ├── services/      # AI & external services
│   └── schemas/       # Pydantic schemas
├── frontend/          # Streamlit UI
│   └── pages/         # Multi-page app views
├── tests/             # pytest test suite
├── docs/              # Documentation
├── deployment/        # Docker & deployment configs
└── requirements.txt
```

## Setup

### 1. Clone and create virtual environment

```bash
python -m venv venv
```

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/macOS:**
```bash
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Environment variables

Create a `.env` file in the project root:

```env
DATABASE_URL=sqlite:///./networking_assistant.db
SECRET_KEY=your-secret-key-change-in-production
GEMINI_API_KEY=your-gemini-api-key
```

### 4. Run the backend

```bash
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

API docs: http://localhost:8000/docs

### 5. Run the frontend

```bash
streamlit run frontend/app.py
```

## Development Roadmap

- [x] Epic 1 — Project Initialization
- [ ] Epic 2 — User Management
- [ ] Epic 3 — Theme Extraction
- [ ] Epic 4 — Conversation Generator
- [ ] Epic 5 — Wikipedia Fact Checker
- [ ] Epic 6 — History Module
- [ ] Epic 7 — Feedback Module
- [ ] Epic 8 — Frontend Dashboard
- [ ] Epic 9 — Testing & Deployment

## License

MIT
