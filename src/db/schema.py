CAMPAIGNS_TABLE = """
CREATE TABLE IF NOT EXISTS campaigns (
    campaign_id SERIAL PRIMARY KEY,
    company VARCHAR(255),
    campaign_type VARCHAR(100),
    target_audience VARCHAR(255),
    duration INT,
    channel_used VARCHAR(100),
    conversion_rate FLOAT,
    acquisition_cost FLOAT,
    roi FLOAT,
    location VARCHAR(100),
    language VARCHAR(50),
    clicks INT,
    impressions INT,
    engagement_score FLOAT,
    customer_segment VARCHAR(100),
    campaign_date DATE,
    revenue FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

INDEXES = [
    "CREATE INDEX IF NOT EXISTS idx_channel ON campaigns(channel_used);",
    "CREATE INDEX IF NOT EXISTS idx_date ON campaigns(campaign_date);",
]

def get_schema_sql():
    return CAMPAIGNS_TABLE + "\n" + "\n".join(INDEXES)
