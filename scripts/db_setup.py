#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

from src.db.connection import get_db_engine
from src.db.schema import get_schema_sql
from src.utils.logger import app_logger
from sqlalchemy import text

def create_schema():
    app_logger.info("📋 Creating database schema...")
    
    try:
        engine = get_db_engine()
        schema_sql = get_schema_sql()
        
        with engine.begin() as conn:
            conn.execute(text(schema_sql))
        
        app_logger.info("✅ Schema created successfully")
        return True
    except Exception as e:
        app_logger.error(f"❌ Schema creation failed: {e}")
        return False

if __name__ == "__main__":
    create_schema()
