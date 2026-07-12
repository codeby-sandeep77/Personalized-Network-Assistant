"""Registration page."""

import streamlit as st

st.set_page_config(page_title="Register", page_icon="📝", layout="centered")

st.title("📝 Register")
st.markdown("Create an account to save your event history and preferences.")

with st.form("register_form"):
    full_name = st.text_input("Full Name")
    email = st.text_input("Email")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    submitted = st.form_submit_button("Register", use_container_width=True)

    if submitted:
        st.info("Registration functionality will be implemented in Epic 2.")

st.divider()
st.page_link("pages/Login.py", label="Already have an account? Login here")
