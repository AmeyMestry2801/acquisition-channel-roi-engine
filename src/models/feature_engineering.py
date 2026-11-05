import pandas as pd
import numpy as np
from src.utils.logger import app_logger

def engineer_features(df):
    """Create features for ML model"""
    app_logger.info("🔧 Engineering features...")
    
    df_feat = df.copy()
    
    # Create interaction features
    df_feat['ctr'] = df_feat['clicks'] / (df_feat['impressions'] + 1)
    df_feat['revenue_per_click'] = df_feat['acquisition_cost'] / (df_feat['clicks'] + 1)
    df_feat['spend_per_impression'] = df_feat['acquisition_cost'] / (df_feat['impressions'] + 1)
    
    app_logger.info(f"✅ Created {len(df_feat.columns)} features")
    return df_feat
