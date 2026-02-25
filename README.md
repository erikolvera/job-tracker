# Job Tracker API

A RESTful API built with FastAPI and SQLAlchemy to track job applications. Supports full CRUD operations with persistent SQLite storage.

## Tech Stack

- **FastAPI** — Python web framework for building APIs
- **SQLAlchemy** — ORM for database interactions
- **SQLite** — Lightweight persistent database
- **Uvicorn** — ASGI server
- **Pydantic** — Data validation

## Features

- Add, retrieve, update, and delete job applications
- Persistent storage — data survives server restarts
- Auto-generated interactive API documentation at `/docs`
- Input validation via Pydantic models

## Getting Started

### Prerequisites

- Python 3.8+

### Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/job-tracker.git
cd job-tracker
```

2. Install dependencies
```bash
pip install fastapi uvicorn sqlalchemy
```

3. Start the server
```bash
uvicorn main:app --reload
```

4. Open your browser and navigate to:
- API: `http://localhost:8000`
- Interactive docs: `http://localhost:8000/docs`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| POST | `/applications` | Add a new job application |
| GET | `/applications` | Get all applications |
| GET | `/applications/{id}` | Get a specific application |
| PUT | `/applications/{id}?status=value` | Update application status |
| DELETE | `/applications/{id}` | Delete an application |

## Example Request

```json
POST /applications
{
  "company": "Charles Schwab",
  "role": "Associate Software Development Engineer",
  "status": "applied",
  "notes": "Applied through NERD program"
}
```

## Example Response

```json
{
  "id": 1,
  "company": "Charles Schwab",
  "role": "Associate Software Development Engineer",
  "status": "applied",
  "notes": "Applied through NERD program"
}
```

## Project Structure

```
job-tracker/
├── main.py         # API routes and request handlers
├── database.py     # Database setup, models, and session management
├── jobs.db         # SQLite database (auto-generated, not tracked in git)
└── README.md
```

## Author

Erik Olvera — [GitHub](https://github.com/yourusername) | [LinkedIn](https://linkedin.com/in/yourusername)
