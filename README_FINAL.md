# 🎯 Acquisition Channel ROI & Growth Lever Engine

**Portfolio Project | Data Science + SQL + ML + Python + Docker**

## What This Project Demonstrates

### ✅ Real-World Data Science
- **200,000 production records** analyzed end-to-end
- **Honest findings**: Tested ML (AUC ~0.50), found no signal, pivoted to SQL insights
- **No overfitting or data leakage**: Proper train/test splits, feature correlation analysis
- **Defensible methodology**: Every metric traced back to SQL queries

### ✅ Technical Stack
- **Database:** PostgreSQL (relational design, indexing, complex queries)
- **SQL:** Window functions, CTEs, aggregations, date partitioning
- **Python:** pandas, scikit-learn, XGBoost, loguru, streamlit
- **ML:** Baseline models (Logistic Regression), XGBoost, feature engineering
- **DevOps:** Docker, Docker Compose, containerized Postgres + app
- **Version Control:** Git

### ✅ Business Impact
- Identified **6 marketing channels** with near-identical ROI (5.0 ± 0.01)
- **Recommended**: Focus on unmeasured levers (audience segmentation, creative testing, seasonality)
- **Weekly automation**: Channel performance reports (CSV export)
- **Stakeholder communication**: Non-technical memo with actionable recommendations

## Architecture

acquisition-channel-roi-engine/
├── data/
│ ├── raw/ # Kaggle CSV (200K rows)
│ └── processed/ # Cleaned outputs
├── src/
│ ├── db/ # PostgreSQL connection, schema, ingest
│ ├── analysis/ # SQL queries (funnel, LTV:CAC)
│ ├── models/ # Feature engineering, ML training
│ └── utils/ # Config, logging, validators
├── dashboards/
│ └── streamlit_app.py # Interactive 3-tab dashboard
├── scripts/
│ ├── db_setup.py # One-time schema creation
│ └── weekly_report_automation.py # Scheduled reporting
├── docker-compose.yml # Postgres + Python containers
├── requirements.txt # Python dependencies
└── README.md # This file



## Key Findings

| Channel    | Campaigns | Conv. Rate | Avg CAC    | ROI    |
|----------|-----------|-----------|-----------|--------|
| Facebook   | 32,819    | 8.00%     | $12,510.90| 5.0187 |
| Website    | 33,360    | 8.02%     | $12,487.81| 5.0142 |
| Google Ads | 33,438    | 8.02%     | $12,528.03| 5.0031 |
| Email      | 33,599    | 8.03%     | $12,526.39| 4.9965 |
| YouTube    | 33,392    | 7.99%     | $12,481.39| 4.9938 |
| Instagram  | 33,392    | 7.99%     | $12,491.76| 4.9887 |

**Insight:** All channels deliver consistent ~5x ROI. No "silver bullet" channel exists. 
Optimization opportunities lie in unmeasured factors (audience quality, creative variation, timing).

## ML Modeling Approach

Tested 3 independent models (Logistic Regression, XGBoost, Random Forest) to predict 
high-ROI campaigns from basic features (duration, conversion_rate, CAC, clicks, impressions, engagement).

**Result:** AUC ~0.50 across all models (equivalent to random guessing)
**Interpretation:** ROI is NOT explained by measured channel attributes

This is **valuable negative finding**: tells us where NOT to invest engineering effort, 
and points to unmeasured drivers (audience segmentation, creative quality, timing).

## How to Run

### 1. Start Database
```bash
docker-compose up -d
sleep 10
python scripts/db_setup.py
```

### 2. Ingest Data
```bash
python -c "from src.db.ingest import ingest_csv; ingest_csv()"
```

### 3. View Dashboard
```bash
streamlit run dashboards/streamlit_app.py
# Visit: http://localhost:8501
```

### 4. Generate Weekly Report
```bash
python scripts/weekly_report_automation.py
```

## Data Quality & Validation

- ✅ 200K rows, 16 columns validated
- ✅ No duplicates found
- ✅ Null checks passed
- ✅ Data type conversions (duration: "30 days" → 30, CAC: "$12.5K" → 12500.0)
- ✅ Date parsing and normalization

## Stakeholder Communication

See: `Stakeholder Memo - Acquisition Channel ROI Analysis.md`

Key recommendation: Stop pursuing channel-level budget reallocation (minimal ROI uplift). 
Instead, investigate audience segmentation, creative testing, and temporal effects.

## Next Steps (Future Work)

1. **Audience Cohort Analysis:** Segment by customer lifetime value, geography
2. **Creative Testing:** A/B test messaging within lowest-converting channels
3. **Multi-touch Attribution:** Model sequential channel exposures
4. **Seasonality:** Analyze temporal patterns by month/day-of-week
5. **Elasticity Testing:** Increase budget on high-ROI channel to test diminishing returns

## Technical Decisions & Tradeoffs

- **PostgreSQL over NoSQL:** Relational structure, complex queries, ACID compliance needed
- **SQL-first analysis over pandas:** Better for large datasets, reproducible, version-controllable
- **Baseline ML over deep learning:** No signal detected; simpler models sufficient
- **Streamlit over Tableau:** Fast prototyping, Python-native, no licensing costs
- **Docker containers:** Reproducible environment, easy deployment

## Files

- `Stakeholder Memo - Acquisition Channel ROI Analysis.md` → Executive summary
- `requirements.txt` → All Python dependencies (Python 3.13 compatible)
- `docker-compose.yml` → Local Postgres setup
- `src/analysis/*.sql` → Queries for channel performance
- `dashboards/streamlit_app.py` → Interactive dashboard
- `scripts/weekly_report_automation.py` → Scheduled reporting

---

**Built with:** Python 3.13, PostgreSQL 15, Streamlit, Docker
**Data Source:** Kaggle - Marketing Campaign Performance Dataset (200K records)
**Portfolio:** Data Science + BizOps + SQL + ML + DevOps
