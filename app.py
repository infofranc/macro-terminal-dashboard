import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Configurazione Pagina
st.set_page_config(page_title="Macro Terminal", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS per UI/UX Macro Terminal
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stMetric { background-color: #1a1c24; border-radius: 10px; padding: 15px; border: 1px solid #30363d; }
    .stPlotlyChart { border-radius: 10px; border: 1px solid #30363d; background-color: #1a1c24; }
    h1, h2, h3 { color: #58a6ff; }
    </style>
    """, unsafe_allow_html=True)

st.title("📊 Macro Terminal - Analisi Ciclica")
st.markdown("Confronto tra lo scenario **2022 (Shock Ucraina)** e lo scenario **2025-26 (Attuale)**")

# Funzione per simulare caricamento dati FRED (in produzione usare fredapi)
def get_mock_data():
    dates_2022 = pd.date_range('2022-02-01', periods=24, freq='MS')
    dates_2026 = pd.date_range('2025-01-01', periods=16, freq='MS')
    return dates_2022, dates_2026

d22, d26 = get_mock_data()

col1, col2 = st.columns(2)

with col1:
    st.subheader("VIX: 2022 vs 2026")
    vix_fig = go.Figure()
    vix_fig.add_trace(go.Scatter(y=[35,32,28,25,22,20,18,17,16,18,20,19], name="2022 (da Feb)", line=dict(color='#58a6ff')))
    vix_fig.add_trace(go.Scatter(y=[25.25, 27, 30, 28, 26, 25.25], name="2025-26 (da Gen)", line=dict(color='#ff7b72', dash='dash')))
    vix_fig.update_layout(template="plotly_dark", margin=dict(l=20, r=20, t=20, b=20), height=350)
    st.plotly_chart(vix_fig, use_container_width=True)

with col2:
    st.subheader("Equity Indices (% Change)")
    eq_fig = go.Figure()
    eq_fig.add_trace(go.Scatter(y=[0, -5, -8, -2, 5, 12, 18], name="S&P 2022", line=dict(color='#79c0ff')))
    eq_fig.add_trace(go.Scatter(y=[0, 2, 5, 10, 15, 22], name="S&P 2025-26", line=dict(color='#ff7b72')))
    eq_fig.update_layout(template="plotly_dark", margin=dict(l=20, r=20, t=20, b=20), height=350)
    st.plotly_chart(eq_fig, use_container_width=True)

col3, col4 = st.columns(2)

with col3:
    st.subheader("HY Credit Spreads")
    hy_fig = go.Figure()
    hy_fig.add_trace(go.Scatter(y=[5.5, 5.0, 4.5, 4.0, 3.5], name="HY 2022", line=dict(color='#d2a8ff')))
    hy_fig.add_trace(go.Scatter(y=[3.28, 3.2, 3.1, 3.0, 2.9], name="HY 2025-26", line=dict(color='#ff7b72')))
    hy_fig.update_layout(template="plotly_dark", margin=dict(l=20, r=20, t=20, b=20), height=350)
    st.plotly_chart(hy_fig, use_container_width=True)

with col4:
    st.subheader("IG BBB Spreads")
    ig_fig = go.Figure()
    ig_fig.add_trace(go.Scatter(y=[2.5, 2.2, 1.8, 1.5, 1.3], name="IG 2022", line=dict(color='#3fb950')))
    ig_fig.add_trace(go.Scatter(y=[1.14, 1.1, 1.12, 1.1, 1.09], name="IG 2025-26", line=dict(color='#ff7b72')))
    ig_fig.update_layout(template="plotly_dark", margin=dict(l=20, r=20, t=20, b=20), height=350)
    st.plotly_chart(ig_fig, use_container_width=True)

st.sidebar.markdown("### Filtri & Analisi")
st.sidebar.info("Dati allineati per mesi dall'evento shock.")
