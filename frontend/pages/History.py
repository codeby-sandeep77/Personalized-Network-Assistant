"""History page."""

import streamlit as st

st.set_page_config(page_title="History", page_icon="📜", layout="wide")

st.title("📜 History")
st.markdown("View and search your past event preparations.")

search_query = st.text_input("Search history", placeholder="Search by event name or keywords...")

col1, col2 = st.columns([3, 1])
with col2:
    if st.button("Search", use_container_width=True):
        st.info("History search will be implemented in Epic 6.")

st.divider()
st.info("No history yet. Generate conversation starters from the Dashboard to see them here.")
