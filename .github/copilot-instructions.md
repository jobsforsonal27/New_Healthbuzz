# HealthBuzz AI Coding Agent Instructions

## Architecture Overview

**HealthBuzz** is a FastAPI-based healthcare management system with a React frontend. The backend follows a layered architecture:

- **API Layer** (`app/api/`): FastAPI routers handling HTTP endpoints (auth, patient, doctor, appointment)
- **CRUD Layer** (`app/crud/`): Database operations (query, create, modify)
- **Models Layer** (`app/models/`): SQLAlchemy ORM models with UUID primary keys
- **Schemas Layer** (`app/schemas/`): Pydantic models for request/response validation
- **Core Layer** (`app/core/`): Database connection, security (JWT + bcrypt), config

**Key principle**: Data flows through models → schemas → CRUD → API endpoints.

## Critical Dependencies & Setup

- **Backend**: FastAPI, SQLAlchemy, PostgreSQL (psycopg2), PyJWT, bcrypt
- **Frontend**: React (Create React App) on port 3000
- **Database**: PostgreSQL at `postgresql://test:test123@localhost/New_healthbuzz`
- **Migrations**: Alembic (`alembic/versions/`) - auto-generated but may contain duplicates
- **CORS**: Enabled for `http://localhost:3000` in [main.py](app/main.py#L14-L18)

## Essential Patterns & Conventions

### 1. User Roles & Authentication
- Users stored in [users.py](app/models/users.py) with enum roles: `patient`, `doctor`, `pharmacy`, `insurance`, `admin`
- Authentication: Email-based with bcrypt hashing + JWT tokens (10min expiry)
- All CRUD routes require `Depends(get_db)` for session injection from [database.py](app/core/database.py)

### 2. Model Design
- All models use `uuid.uuid4()` as default primary key (String type, not GUID)
- Example: [Patient](app/models/patients.py) has `user_id` (FK to User)
- Pattern: `id` (PK) + `user_id` (FK to User) for domain models

### 3. CRUD Naming Convention
- File per entity: `app/crud/user.py`, `app/crud/patient.py`, `app/crud/appointment.py`
- Function naming: `create_*`, `get_*`, `modify_*` (not `update_*`)
- Signature: Always `db:Session` as first param
- Example: [appointment.py](app/crud/appointment.py#L5-L6) - `get_appointment_by_id(db, patient_id)`

### 4. API Route Pattern
- Router prefix in all files: `/auth`, `/patients`, `/doctors`, `/appointments`
- Response models must match schema: `@router.post("/create", response_model=PatientResponse)`
- All endpoints depend on `get_db()` for session injection
- See [auth.py](app/api/auth.py#L15-L18) for complete example

### 5. Pydantic Schemas
- Inherit from `BaseModel`
- Use `EmailStr` for email validation (from pydantic)
- Separate Create vs Response schemas (Patient vs PatientResponse)
- See [user.py](app/schemas/user.py) for token, login, create schemas

## Common Tasks & Commands

### Run Backend
```bash
# From app/ directory with virtual env activated
uvicorn app.main:app --reload
```

### Database Migrations
```bash
# From repo root
alembic revision --autogenerate -m "description"
alembic upgrade head
```

### Frontend Development
```bash
# From frontend/ directory
npm start  # Runs on http://localhost:3000
npm run build
```

## Code Smells to Avoid

- Hardcoded secrets: Use [config.py](app/core/config.py) (`JWT_SECRET_KEY`, `DATABASE_URL`)
- Duplicate CRUD logic: Check existing crud/ files before writing new functions
- Missing db.close() or exception handling: Use [database.py](app/core/database.py) pattern (`try/finally`)
- Response models without Pydantic validation: Always use schema response models in decorators

## File Organization Rules

- **New endpoint?** Add route to existing file in `api/` or create new one
- **New model?** Create in `models/`, add schema in `schemas/`, add CRUD in `crud/`, add API in `api/`
- **Database change?** Run alembic revision, never modify schema directly
- **Security functions?** Add to [security.py](app/core/security.py) (password hashing, token creation)
