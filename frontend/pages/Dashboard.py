"""Main dashboard page."""

import streamlit as st

st.set_page_config(page_title="Dashboard", page_icon="📋", layout="wide")

st.title("📋 Dashboard")
st.markdown("Enter an event description to generate personalized conversation starters.")

with st.sidebar:
    st.header("Settings")
    st.text_input("Event Name", placeholder="e.g. Tech Conference 2026")
    st.selectbox("Event Type", ["Conference", "Meetup", "Workshop", "Networking Event", "Other"])

event_description = st.text_area(
    "Event Description",
    placeholder="Describe the event, topics, speakers, and audience...",
    height=200,
)

col1, col2 = st.columns(2)

with col1:
    if st.button("Extract Themes", use_container_width=True):
        st.info("Theme extraction will be implemented in Epic 3.")

with col2:
    if st.button("Generate Starters", use_container_width=True):
        st.info("Conversation generation will be implemented in Epic 4.")

st.divider()
st.subheader("Results")
st.empty()
