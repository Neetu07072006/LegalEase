# LegalEase

AI-powered legal document understanding and management platform.

## Technology

- Next.js
- TypeScript
- Python FastAPI
- PostgreSQL
- Supabase
- SQLAlchemy

## Frontend Setup

cd frontend
npm install
npm run dev

Frontend: http://localhost:3000

## Backend Setup

cd backend
python -m venv venv

Windows:
venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Start server:
uvicorn app.main:app --reload --port 8000

Backend: http://127.0.0.1:8000

API documentation:
http://127.0.0.1:8000/docs