# MEMO

**TO:** Growth Leadership  
**FROM:** Data Science / BizOps  
**DATE:** September 1, 2026  
**RE:** Acquisition Channel ROI & Growth Lever Analysis

---

## EXECUTIVE SUMMARY

We analyzed 200,000 campaign records across 6 marketing channels (Facebook, Website, Google Ads, Email, YouTube, Instagram) to identify budget reallocation opportunities and growth levers.

**Key Finding:** All channels deliver statistically similar ROI (5.0 ± 0.01) and conversion rates (8.0 ± 0.04%), suggesting the portfolio is well-balanced OR optimization opportunities lie outside channel selection.

---

## METHODOLOGY

**Data:** 200K campaigns (Jan-Dec 2021)  
**Approach:**
- SQL funnel analysis (channel-level metrics)
- ML conversion propensity modeling (tested for signal)
- LTV:CAC ratio analysis
- Budget allocation review

**ML Findings:** Logistic Regression & XGBoost both achieved AUC ~0.50, indicating ROI is **not predictable from basic campaign attributes** (duration, conversion_rate, CAC, clicks, impressions, engagement). This suggests ROI variance is driven by factors outside our measured features (timing, audience quality, creative content, competitive context).

---

## CHANNEL PERFORMANCE SCORECARD

| Channel    | Campaigns | Conv. Rate | Avg CAC    | Avg ROI | Total Spend    |
|----------|-----------|-----------|-----------|---------|----------------|
| Facebook   | 32,819    | 8.00%     | $12,510.90| 5.0187  | $410.6M        |
| Website    | 33,360    | 8.02%     | $12,487.81| 5.0142  | $416.6M        |
| Google Ads | 33,438    | 8.02%     | $12,528.03| 5.0031  | $418.9M        |
| Email      | 33,599    | 8.03%     | $12,526.39| 4.9965  | $420.9M        |
| YouTube    | 33,392    | 7.99%     | $12,481.39| 4.9938  | $416.8M        |
| Instagram  | 33,392    | 7.99%     | $12,491.76| 4.9887  | $417.1M        |

**Observation:** Metrics are tightly clustered. ROI spread is only 0.30 percentage points (5.0187 - 4.9887).

---

## WHAT THE DATA IS TELLING US

### ✅ What's Working
- All six channels deliver consistent, positive ROI (~5x)
- Conversion rates converge around 8%
- CAC is stable ($12.5K ± $25)
- Portfolio appears well-balanced

### ⚠️ What This Means
Traditional budget reallocation (moving 15% from worst to best performer) would yield **only +0.09% portfolio ROI improvement**—minimal impact. This is **not a problem**; it indicates the portfolio is optimized or constrained by non-channel factors.

### 🔍 What We Didn't Find
- No "silver bullet" channel
- No dramatic CAC or conversion differences
- No predictive signal from channel attributes alone

---

## ALTERNATIVE LEVERS (BEYOND CHANNEL SELECTION)

Since channel-level factors show limited variance, investigate:

1. **Audience Segmentation:** Do some customer cohorts convert better on specific channels?
2. **Temporal Effects:** Do channels perform differently by season, day-of-week, or time-of-day?
3. **Creative Variation:** Does messaging quality or format vary within channels?
4. **Channel Interactions:** Do sequential exposures (e.g., Google Ads → Email) outperform single-channel?
5. **Attribution Window:** Are we measuring the right conversion window?

---

## RECOMMENDATIONS

### Immediate (No ROI Lift Expected)
- Monitor channel performance weekly; alert if any channel ROI drifts >2%
- Document conversion-to-revenue funnel to calculate true LTV:CAC ratios
- Segment by audience cohort to identify latent differences

### Medium-term (2-4 weeks)
- A/B test creative messaging within lowest-performing channel (YouTube, 7.99% conv)
- Investigate seasonal/temporal patterns in conversion data
- Model channel synergies (multi-touch attribution)

### Long-term (1-2 months)
- Build cohort-based ROI models (LTV by acquisition channel + customer segment)
- Test budget increases on highest-ROI channel (Facebook) to test elasticity
- Explore new channels or sub-segments not currently tracked

---

## APPENDIX

**ML Model Justification:**  
We tested logistic regression and XGBoost to predict high-ROI campaigns from channel features. Both models achieved AUC = 0.50, equivalent to random guessing. This is **expected and informative**: it tells us ROI is not driven by measured channel-level attributes, but by unmeasured factors (audience quality, competitive timing, creative resonance, etc.). Therefore, **further investment in channel-level ML is not recommended**. Instead, focus on the levers above.

**Data Quality:**  
All 200K records passed validation (no nulls >50%, no duplicates, data type consistency post-cleaning). Dataset spans full calendar year (2021).

---

**Questions? Contact Data Science.**
