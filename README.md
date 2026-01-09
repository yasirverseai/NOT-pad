# NOT-Pad

A simple note-taking web application built with FastAPI, SQLAlchemy, and SQLite. Create, read, update, and delete notes via a RESTful API.

## Features

- **CRUD Operations**: Full Create, Read, Update, Delete functionality for notes
- **Persistent Storage**: SQLite database with automatic table creation
- **FastAPI**: Modern, fast web framework with automatic API documentation
- **Pydantic Validation**: Automatic request/response validation
- **SQLAlchemy ORM**: Type-safe database operations

## Tech Stack

- **Backend**: FastAPI
- **Database**: SQLite (via SQLAlchemy)
- **ORM**: SQLAlchemy
- **Validation**: Pydantic

## Project Structure

```
app/
├── main.py          # FastAPI app, routes, and dependencies
├── models.py        # SQLAlchemy & Pydantic models
├── database.py      # Database configuration and engine
├── crud.py          # CRUD operations
requirements.txt     # Python dependencies
```

## API Endpoints

| Method | Endpoint       | Description                  | Request Body                  |
|--------|----------------|------------------------------|-------------------------------|
| POST   | `/notes/`      | Create a new note            | `{title: str, content: str}` |
| GET    | `/notes/`      | Get all notes (paginated)    | Query: `skip`, `limit`       |
| GET    | `/notes/{id}`  | Get note by ID               | -                             |
| PUT    | `/notes/{id}`  | Update note by ID            | `{title: str, content: str}` |
| DELETE | `/notes/{id}`  | Delete note by ID            | -                             |

**Responses**: All endpoints return JSON with note data (`id`, `title`, `content`, `created_at`, `updated_at`).

Interactive docs available at `/docs` (Swagger) and `/redoc`.

## Quick Start

1. **Install dependencies**:
   ```bash
   pip install fastapi sqlalchemy aiosqlite uvicorn
   ```

2. **Run the application**:
   ```bash
   uvicorn app.main:app --reload
   ```

3. **Open in browser**:
   - API Docs: http://127.0.0.1:8000/docs
   - Test endpoints directly via the interactive UI

The SQLite database (`database.db`) is created automatically in the project root.

## Example Usage

**Create a note**:
```bash
curl -X POST "http://127.0.0.1:8000/notes/" \
     -H "Content-Type: application/json" \
     -d '{"title": "My First Note", "content": "Hello, NOT-Pad!"}'
```

**List notes**:
```bash
curl "http://127.0.0.1:8000/notes/"
```

## Database Schema

Notes table:
- `id` (Integer, Primary Key)
- `title` (String, Indexed)
- `content` (String)
- `created_at` (DateTime)
- `updated_at` (DateTime, auto-updates)

## Development

- Uses SQLite for simplicity (no separate DB setup required)
- Auto-creates tables on startup
- Hot reload with `--reload` flag

## License

MIT License - feel free to use and modify!