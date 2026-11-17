import streamlit as st
from src.ui import render_churn
st.set_page_config(page_title="Customer Churn Prediction", page_icon="📉", layout="wide")
render_churn()
