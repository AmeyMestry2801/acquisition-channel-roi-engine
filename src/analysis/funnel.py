CHANNEL_FUNNEL_QUERY = """
SELECT 
    channel_used,
    COUNT(*) as total_campaigns,
    ROUND(AVG(conversion_rate)::numeric, 4) as avg_conversion_rate,
    ROUND(AVG(acquisition_cost)::numeric, 2) as avg_cac,
    ROUND(AVG(roi)::numeric, 4) as avg_roi,
    ROUND(SUM(acquisition_cost)::numeric, 2) as total_spend
FROM campaigns
WHERE channel_used IS NOT NULL
GROUP BY channel_used
ORDER BY avg_roi DESC;
"""

CAMPAIGN_TYPE_QUERY = """
SELECT 
    campaign_type,
    COUNT(*) as campaigns,
    ROUND(AVG(conversion_rate)::numeric, 4) as avg_conversion_rate,
    ROUND(AVG(acquisition_cost)::numeric, 2) as avg_cac,
    ROUND(AVG(roi)::numeric, 4) as avg_roi
FROM campaigns
GROUP BY campaign_type
ORDER BY avg_roi DESC;
"""
