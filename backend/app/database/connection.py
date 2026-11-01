from sqlalchemy import create_engine, text
from app.core.config import settings

engine = None

if settings.database_url:
    database_url = settings.database_url.replace(
        "postgresql://",
        "postgresql+psycopg://",
        1
    )
    engine = create_engine(
        database_url,
        pool_pre_ping=True,
        connect_args={"sslmode": "require"}
    )

def check_database():
    if engine is None:
        return "not_configured"

    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return "connected"
    except Exception:
        return "disconnected"