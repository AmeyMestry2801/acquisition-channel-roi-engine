import pandas as pd
from src.db.connection import get_db_engine
from src.utils.config import config
from src.utils.logger import app_logger

def ingest_csv():
    app_logger.info("🚀 Starting CSV ingest...")
    
    try:
        df = pd.read_csv(config.RAW_DATA_PATH)
        app_logger.info(f"📖 Loaded {len(df)} rows")
    except FileNotFoundError:
        app_logger.error(f"❌ File not found: {config.RAW_DATA_PATH}")
        return False
    
    # Clean column names
    df.columns = [col.lower().replace(' ', '_') for col in df.columns]
    
    # Rename 'date' to 'campaign_date'
    if 'date' in df.columns:
        df.rename(columns={'date': 'campaign_date'}, inplace=True)
    
    # Clean data types
    try:
        # Extract numeric duration (e.g., "30 days" → 30)
        if 'duration' in df.columns:
            df['duration'] = df['duration'].str.extract(r'(\d+)')[0].astype('Int64')
        
        # Remove $ and commas from acquisition_cost
        if 'acquisition_cost' in df.columns:
            df['acquisition_cost'] = df['acquisition_cost'].str.replace('$', '').str.replace(',', '').astype('float64')
        
        # Convert campaign_date to datetime
        if 'campaign_date' in df.columns:
            df['campaign_date'] = pd.to_datetime(df['campaign_date']).dt.date
        
        # Ensure numeric columns
        if 'clicks' in df.columns:
            df['clicks'] = pd.to_numeric(df['clicks'], errors='coerce').fillna(0).astype('int64')
        
        if 'impressions' in df.columns:
            df['impressions'] = pd.to_numeric(df['impressions'], errors='coerce').fillna(0).astype('int64')
        
        if 'engagement_score' in df.columns:
            df['engagement_score'] = pd.to_numeric(df['engagement_score'], errors='coerce').fillna(0).astype('int64')
        
        if 'roi' in df.columns:
            df['roi'] = pd.to_numeric(df['roi'], errors='coerce').fillna(0).astype('float64')
        
        if 'conversion_rate' in df.columns:
            df['conversion_rate'] = pd.to_numeric(df['conversion_rate'], errors='coerce').fillna(0).astype('float64')
        
        app_logger.info(f"✅ Data cleaned and converted")
        
    except Exception as e:
        app_logger.error(f"❌ Data cleaning failed: {e}")
        return False
    
    try:
        engine = get_db_engine()
        df.to_sql('campaigns', engine, if_exists='append', index=False)
        app_logger.info(f"✅ Inserted {len(df)} rows into campaigns table")
        return True
    except Exception as e:
        app_logger.error(f"❌ Ingest failed: {e}")
        return False

if __name__ == "__main__":
    ingest_csv()
