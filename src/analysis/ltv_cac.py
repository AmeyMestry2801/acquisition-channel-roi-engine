LTV_CAC_RATIO = """
SELECT 
    channel_used,
    COUNT(*) as campaigns,
    ROUND(AVG(acquisition_cost)::numeric, 2) as avg_cac,
    ROUND(AVG(roi)::numeric, 4) as avg_roi,
    ROUND((AVG(roi) * AVG(acquisition_cost))::numeric, 2) as implied_ltv,
    ROUND((AVG(roi) * AVG(acquisition_cost) / NULLIF(AVG(acquisition_cost), 0))::numeric, 2) as ltv_cac_ratio,
    CASE 
        WHEN AVG(roi) >= 5 THEN 'Excellent'
        WHEN AVG(roi) >= 4 THEN 'Good'
        WHEN AVG(roi) >= 3 THEN 'Fair'
        ELSE 'Poor'
    END as profitability_tier
FROM campaigns
GROUP BY channel_used
ORDER BY avg_roi DESC;
"""

CHANNEL_BUDGET_ALLOCATION = """
SELECT 
    channel_used,
    COUNT(*) as campaigns,
    ROUND(SUM(acquisition_cost)::numeric, 2) as total_spend,
    ROUND(AVG(acquisition_cost)::numeric, 2) as avg_cac,
    ROUND(AVG(roi)::numeric, 4) as avg_roi,
    ROUND((SUM(acquisition_cost) / (SELECT SUM(acquisition_cost) FROM campaigns) * 100)::numeric, 2) as pct_of_total_spend
FROM campaigns
GROUP BY channel_used
ORDER BY total_spend DESC;
"""
