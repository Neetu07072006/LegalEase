from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.database.connection import check_database
from app.routes.documents import router as documents_router

app = FastAPI(
    title=settings.app_name,
    description="AI-powered legal document intelligence platform",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        settings.frontend_url,
        "http://127.0.0.1:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(documents_router)

@app.get("/")
def root():
    return {
        "message": "Welcome to LegalEase API",
        "status": "online"
    }

@app.get("/api/health")
def health():
    return {
        "status": "online",
        "service": "LegalEase API",
        "database": check_database()
    }