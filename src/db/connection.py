from sqlalchemy import create_engine, text
from src.utils.config import config
from src.utils.logger import app_logger

def get_db_engine():
    connection_string = f"postgresql+psycopg://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}"
    
    try:
        engine = create_engine(connection_string, echo=False, pool_pre_ping=True)
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        app_logger.info(f"✅ Connected to {config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}")
        return engine
    except Exception as e:
        app_logger.error(f"❌ Database connection failed: {e}")
        raise
