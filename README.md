# ReachJobAI

AI-powered job discovery and personalized cold email outreach automation platform for software developers.

## Overview

ReachJobAI helps software developers discover relevant companies, research decision-makers, identify professional contact information, generate personalized cold emails using AI, and manage outreach campaigns.

## Technology Stack

### Backend
- Python 3.11+
- FastAPI
- Pydantic v2
- SQLAlchemy 2.0
- PostgreSQL (Neon-compatible)
- Alembic
- Uvicorn

### Frontend
- React 18
- TypeScript
- Vite
- Tailwind CSS
- shadcn/ui
- React Router
- TanStack Query
- Axios

### Database
- PostgreSQL
- SQLAlchemy ORM
- Alembic migrations

## Project Structure

```
ReachJobAI/
├── backend/           # FastAPI backend application
│   ├── app/
│   │   ├── api/      # API routes and endpoints
│   │   ├── core/     # Configuration, security, logging
│   │   ├── db/       # Database setup and session management
│   │   ├── models/   # SQLAlchemy models
│   │   ├── schemas/  # Pydantic schemas
│   │   ├── services/ # Business logic
│   │   ├── repositories/ # Data access layer
│   │   ├── integrations/ # External service integrations
│   │   └── main.py   # Application entry point
│   ├── alembic/      # Database migrations
│   └── tests/        # Backend tests
├── frontend/         # React frontend application
│   └── src/
│       ├── app/      # Application setup
│       ├── components/ # Reusable components
│       ├── features/ # Feature-specific components
│       ├── hooks/    # Custom React hooks
│       ├── lib/      # Utilities and helpers
│       ├── services/ # API client services
│       └── types/    # TypeScript type definitions
└── README.md
```

## Prerequisites

- Python 3.11 or higher
- Node.js 18+ and npm
- PostgreSQL database (local or Neon cloud)
- Git

## Backend Setup

### 1. Create Virtual Environment

```powershell
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 2. Install Dependencies

```powershell
pip install -e .
```

### 3. Configure Environment

Copy `.env.example` to `.env` and configure:

```
APP_NAME=ReachJobAI
APP_ENV=development
DEBUG=true
API_V1_PREFIX=/api/v1
DATABASE_URL=postgresql://user:password@localhost:5432/reachjobai
JWT_SECRET_KEY=your-secret-key-here
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
GEMINI_API_KEY=your-gemini-api-key
FRONTEND_URL=http://localhost:5173
BACKEND_CORS_ORIGINS=["http://localhost:5173"]
```

### 4. Run Database Migrations

```powershell
alembic upgrade head
```

### 5. Start Development Server

```powershell
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Backend will be available at http://localhost:8000

API documentation: http://localhost:8000/docs

## Frontend Setup

### 1. Install Dependencies

```powershell
cd frontend
npm install
```

### 2. Configure Environment

Copy `.env.example` to `.env`:

```
VITE_API_BASE_URL=http://localhost:8000
```

### 3. Start Development Server

```powershell
npm run dev
```

Frontend will be available at http://localhost:5173

### 4. Build for Production

```powershell
npm run build
```

## Development Commands

### Backend

```powershell
# Install dependencies
pip install -e .

# Run development server
uvicorn app.main:app --reload

# Create new migration
alembic revision --autogenerate -m "description"

# Apply migrations
alembic upgrade head

# Rollback migration
alembic downgrade -1

# Run tests
pytest
```

### Frontend

```powershell
# Install dependencies
npm install

# Run development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Type check
npm run type-check

# Lint
npm run lint
```

## API Endpoints

### Health

- `GET /api/v1/health` - Application health status
- `GET /api/v1/health/db` - Database connectivity status

## Environment Variables

### Backend

| Variable | Description | Required |
|----------|-------------|----------|
| APP_NAME | Application name | Yes |
| APP_ENV | Environment (development/production) | Yes |
| DEBUG | Debug mode | Yes |
| API_V1_PREFIX | API version prefix | Yes |
| DATABASE_URL | PostgreSQL connection string | Yes |
| JWT_SECRET_KEY | Secret key for JWT tokens | Yes |
| JWT_ALGORITHM | JWT algorithm (HS256) | Yes |
| ACCESS_TOKEN_EXPIRE_MINUTES | Token expiration time | Yes |
| GEMINI_API_KEY | Google Gemini API key | No* |
| FRONTEND_URL | Frontend application URL | Yes |
| BACKEND_CORS_ORIGINS | Allowed CORS origins (JSON array) | Yes |

\* Required for AI features but not for initial startup

### Frontend

| Variable | Description | Required |
|----------|-------------|----------|
| VITE_API_BASE_URL | Backend API base URL | Yes |

## Security Notes

- Never commit `.env` files to version control
- Use strong, randomly generated JWT secret keys
- Configure CORS origins appropriately for production
- Use environment-specific configuration files
- Store API keys securely

## What's Implemented

This foundation phase includes:

- ✅ FastAPI application structure
- ✅ Pydantic Settings configuration management
- ✅ SQLAlchemy 2.0 + PostgreSQL setup
- ✅ Alembic migration framework
- ✅ CORS configuration
- ✅ Health check endpoints
- ✅ JWT security utilities
- ✅ React + TypeScript frontend
- ✅ Vite build system
- ✅ Tailwind CSS styling
- ✅ React Router navigation
- ✅ TanStack Query data fetching
- ✅ Axios API client
- ✅ Responsive dashboard layout
- ✅ Professional SaaS UI components

## What's NOT Implemented Yet

The following features are planned for future phases:

- ❌ User authentication and registration
- ❌ Company discovery integration
- ❌ Lead research functionality
- ❌ AI-powered email generation
- ❌ Gmail OAuth integration
- ❌ Email scheduling and sending
- ❌ Campaign management
- ❌ Analytics and reporting
- ❌ LinkedIn OAuth integration
- ❌ Redis caching
- ❌ Celery background tasks
- ❌ Comprehensive test coverage

## Contributing

This is a development foundation. Features will be added incrementally through controlled development phases.

## License

Proprietary
