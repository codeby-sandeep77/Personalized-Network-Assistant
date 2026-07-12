"""Personalized Networking Assistant — Streamlit frontend."""

import streamlit as st

st.set_page_config(
    page_title="Networking Assistant",
    page_icon="🤝",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("🤝 Personalized Networking Assistant")
st.markdown(
    """
    Welcome! This AI-powered assistant helps you prepare for networking events by:

    - **Extracting themes** from event descriptions
    - **Generating conversation starters** tailored to the event
    - **Verifying facts** via Wikipedia

    Use the sidebar to navigate between pages.
    """
)

col1, col2, col3 = st.columns(3)

with col1:
    st.info("📋 **Dashboard**\n\nGenerate conversation starters for your next event.")

with col2:
    st.info("📜 **History**\n\nReview your past event preparations.")

with col3:
    st.info("👤 **Account**\n\nLogin or register to save your history.")

st.divider()
st.caption("Epic 1 — Project Initialization complete. Full features coming in upcoming epics.")
