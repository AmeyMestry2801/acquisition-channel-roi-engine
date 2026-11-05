import sys
import os

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
from src.analysis.sql_runner import run_query
from src.analysis.funnel import CHANNEL_FUNNEL_QUERY
from src.analysis.ltv_cac import LTV_CAC_RATIO, CHANNEL_BUDGET_ALLOCATION
import plotly.express as px

st.set_page_config(page_title="Acquisition ROI Engine", layout="wide")

st.title("🎯 Acquisition Channel ROI & Growth Lever Engine")
st.markdown("**Data-driven marketing channel analysis | 200K campaigns analyzed**")
st.markdown("---")

# Load data
@st.cache_data
def load_funnel():
    return run_query(CHANNEL_FUNNEL_QUERY)

@st.cache_data
def load_ltv():
    return run_query(LTV_CAC_RATIO)

@st.cache_data
def load_budget():
    return run_query(CHANNEL_BUDGET_ALLOCATION)

df_funnel = load_funnel()
df_ltv = load_ltv()
df_budget = load_budget()

# Tabs
tab1, tab2, tab3 = st.tabs(["📊 Channel Performance", "💰 LTV:CAC Analysis", "💵 Budget Allocation"])

with tab1:
    st.subheader("Channel Funnel Metrics")
    st.dataframe(df_funnel, use_container_width=True)
    
    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.bar(df_funnel, x='channel_used', y='avg_roi', title='ROI by Channel')
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        fig2 = px.bar(df_funnel, x='channel_used', y='avg_conversion_rate', title='Conversion Rate by Channel')
        st.plotly_chart(fig2, use_container_width=True)

with tab2:
    st.subheader("LTV:CAC Ratio Analysis")
    st.dataframe(df_ltv, use_container_width=True)

with tab3:
    st.subheader("Budget Allocation by Channel")
    st.dataframe(df_budget, use_container_width=True)
    
    fig3 = px.pie(df_budget, values='total_spend', names='channel_used', title='% of Total Spend by Channel')
    st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")
st.markdown("**Methodology:** SQL funnel analysis + ML signal testing (AUC ~0.50 indicates ROI driven by unmeasured factors)")
