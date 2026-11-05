import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DB_USER = os.getenv("DB_USER", "airflow")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "airflow_pwd")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "5432")
    DB_NAME = os.getenv("DB_NAME", "marketing_db")
    
    RAW_DATA_PATH = "data/raw/marketing_campaign_dataset.csv"
    PROCESSED_DATA_PATH = "data/processed/"
    TEST_SIZE = 0.2
    RANDOM_STATE = 42

config = Config()
