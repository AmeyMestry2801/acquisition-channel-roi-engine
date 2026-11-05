import pandas as pd
from sqlalchemy import text
from src.db.connection import get_db_engine
from src.utils.logger import app_logger

def run_query(query_sql):
    try:
        engine = get_db_engine()
        df = pd.read_sql(query_sql, engine)
        app_logger.info(f"✅ Query executed: {len(df)} rows")
        return df
    except Exception as e:
        app_logger.error(f"❌ Query failed: {e}")
        return pd.DataFrame()
