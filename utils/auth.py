"""
Authentication utilities for Analah Capital Ops Platform.
"""

import streamlit as st
from typing import Optional, Dict, Any

# ============================================================
# HARDCODED USERS – Edit as needed
# ============================================================
USERS: Dict[str, Dict[str, Any]] = {
    "admin": {
        "password": "Analah@Admin2026",      # CHANGE THIS
        "name": "Administrator",
        "role": "admin",
        "email": "admin@analah.com",
    },
    "hitesh": {
        "password": "hitesh123",
        "name": "Hitesh Dhankani",
        "role": "user",
        "email": "hitesh@analah.com",
    },
    "vaishali": {
        "password": "vaishali123",
        "name": "Vaishali Dhankani",
        "role": "user",
        "email": "vaishali@analah.com",
    },
    "ops1": {
        "password": "ops123",
        "name": "Operations Lead",
        "role": "user",
        "email": "ops@analah.com",
    },
}


def check_login(username: str, password: str) -> Optional[Dict[str, Any]]:
    user = USERS.get(username.strip().lower())
    if user and user["password"] == password:
        return {
            "username": username.strip().lower(),
            "name": user["name"],
            "role": user["role"],
            "email": user.get("email", ""),
        }
    return None


def is_admin(user_info: Optional[Dict] = None) -> bool:
    if user_info is None:
        user_info = st.session_state.get("user_info")
    return bool(user_info and user_info.get("role") == "admin")


def logout():
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()


def init_auth_session():
    defaults = {
        "logged_in": False,
        "username": None,
        "user_info": None,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def get_current_user() -> Optional[Dict[str, Any]]:
    return st.session_state.get("user_info")
