#!/usr/bin/env python3
"""Generate weekly channel performance report"""
import sys
sys.path.insert(0, '.')

import pandas as pd
from datetime import datetime
from src.analysis.sql_runner import run_query
from src.analysis.funnel import CHANNEL_FUNNEL_QUERY
from src.analysis.ltv_cac import LTV_CAC_RATIO
from src.utils.logger import app_logger

def generate_weekly_report():
    """Generate and save weekly report"""
    app_logger.info("📊 Generating weekly channel performance report...")
    
    # Run queries
    df_funnel = run_query(CHANNEL_FUNNEL_QUERY)
    df_ltv = run_query(LTV_CAC_RATIO)
    
    # Create report
    report_date = datetime.now().strftime("%Y-%m-%d")
    report_path = f"reports/weekly_report_{report_date}.csv"
    
    # Merge and save
    df_report = df_funnel.merge(df_ltv[['channel_used', 'profitability_tier']], on='channel_used')
    df_report.to_csv(report_path, index=False)
    
    app_logger.info(f"✅ Report saved: {report_path}")
    
    # Print summary
    print(f"\n{'='*80}")
    print(f"📋 WEEKLY REPORT - {report_date}")
    print(f"{'='*80}\n")
    print(df_report.to_string(index=False))
    print(f"\n{'='*80}\n")
    
    return report_path

if __name__ == "__main__":
    generate_weekly_report()
