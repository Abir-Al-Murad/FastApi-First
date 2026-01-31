Project1Fast — FastAPI learning project

Overview
- Minimal FastAPI app using SQLAlchemy and JWT auth.
- Files of interest:
  - app/main.py — creates FastAPI app and registers routers.
  - app/database.py — SQLAlchemy engine, `Base`, and `get_db()` dependency.
  - app/models.py — ORM models (`Course`, `User`).
  - app/schemas.py — Pydantic request/response models.
  - app/oauth2.py — JWT creation/verification and `get_current_user` dependency.
  - app/utils.py — password hashing helpers.
  - app/routers/auth.py — `/login` endpoint (returns JWT).
  - app/routers/user.py — `/users` endpoints (create account).
  - app/routers/course.py — `/course` CRUD endpoints (some protected).

Prerequisites
- Python 3.10+ recommended
- PostgreSQL running locally (or update connection string in `app/database.py`)

Install (example)
```bash
python -m venv .venv
.venv\Scripts\activate
pip install fastapi uvicorn sqlalchemy psycopg2-binary PyJWT pwdlib
```
Note: the code uses `jwt` (PyJWT) and `pwdlib` for password hashes — adjust packages if you use alternatives (e.g., `passlib`).

Database
- Default connection (in `app/database.py`): `postgresql://postgres:1234@localhost/sohojx`
- Create the DB (psql):
```sql
CREATE DATABASE sohojx;
```
- Create tables (quick way):
```bash
python -c "from app.database import engine; from app import models; models.Base.metadata.create_all(bind=engine)"
```

Run the app
```bash
uvicorn app.main:app --reload --port 8000
```
Open interactive docs: http://127.0.0.1:8000/docs

Authentication flow (short)
- Create a user: POST `/users/` with JSON `{ "email": "you@example.com", "password": "secret" }`.
- Login: POST `/login` with form data `username` and `password` (as `application/x-www-form-urlencoded`). Returns `access_token`.
- Use header `Authorization: Bearer <token>` for protected endpoints (e.g., POST `/course/`).

Endpoints & examples
- POST /users/
  - Create account (returns 201). Body JSON: `email`, `password`.

- POST /login
  - Obtain JWT. Example curl:
```bash
curl -X POST "http://127.0.0.1:8000/login" -H "Content-Type: application/x-www-form-urlencoded" -d "username=you@example.com&password=secret"
```

- GET /course/
  - List all courses.

- POST /course/  (protected)
  - Create a course. Body JSON: `{ "name": "Name", "instructor": "Inst", "duration": 3.5, "website": "http://example.com" }`
  - Example:
```bash
curl -X POST "http://127.0.0.1:8000/course/" -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{"name":"X","instructor":"Y","duration":10,"website":"http://example.com"}'
```

- GET /course/{id}
  - Get course by id.

- PUT /course/{id}
  - Update an existing course. Body same as create.

- DELETE /course/{id}
  - Delete a course (204 on success).

Common gotchas
- Ensure PostgreSQL is running and DB exists; update credentials in `app/database.py` if needed.
- JWT expiry is short (1 minute by default in `app/oauth2.py`) — tokens may expire quickly while testing.
- Password hashing uses `pwdlib`; if you get import errors, replace with `passlib.hash` (e.g., `bcrypt`).

Next steps
- If you want, I can add a runnable `requirements.txt`, or walk through any file line-by-line.
