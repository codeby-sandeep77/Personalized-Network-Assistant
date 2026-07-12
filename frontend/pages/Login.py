"""Login page."""

import streamlit as st

st.set_page_config(page_title="Login", page_icon="🔐", layout="centered")

st.title("🔐 Login")
st.markdown("Sign in to access your networking assistant.")

with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Login", use_container_width=True)

    if submitted:
        st.info("Login functionality will be implemented in Epic 2.")

st.divider()
st.page_link("pages/Register.py", label="Don't have an account? Register here")
