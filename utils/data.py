"""
Data layer for Analah Capital Ops Platform
Uses Supabase (PostgreSQL) for permanent storage
"""

import streamlit as st
import pandas as pd
from datetime import datetime, date
from typing import Optional
from supabase import create_client, Client

# ============================================================
# SUPABASE CONNECTION
# ============================================================

@st.cache_resource
def get_supabase_client() -> Client:
    url = st.secrets["supabase"]["url"]
    key = st.secrets["supabase"]["key"]
    return create_client(url, key)


def load_data() -> pd.DataFrame:
    """Load all data from Supabase."""
    try:
        supabase = get_supabase_client()
        response = supabase.table("tasks").select("*").order("created_at", desc=True).execute()
        
        if response.data:
            df = pd.DataFrame(response.data)
            # Ensure all expected columns exist
            expected_cols = [
                "id", "date", "username", "name", "team", "type",
                "content", "priority", "status", "created_at", "updated_at"
            ]
            for col in expected_cols:
                if col not in df.columns:
                    df[col] = None
            return df[expected_cols]
        else:
            return pd.DataFrame(columns=[
                "id", "date", "username", "name", "team", "type",
                "content", "priority", "status", "created_at", "updated_at"
            ])
    except Exception as e:
        st.error(f"Error loading data from Supabase: {e}")
        return pd.DataFrame(columns=[
            "id", "date", "username", "name", "team", "type",
            "content", "priority", "status", "created_at", "updated_at"
        ])


def generate_id(username: str) -> str:
    return f"{username}_{datetime.now().timestamp():.6f}"


def add_entry(
    username: str,
    name: str,
    team: str,
    entry_type: str,
    content: str,
    priority: str = "Medium",
    status: str = "Open",
    entry_date: Optional[str] = None,
) -> bool:
    """Add a new POA / EOD / Task entry to Supabase."""
    try:
        supabase = get_supabase_client()
        now = datetime.now().isoformat()

        new_row = {
            "id": generate_id(username),
            "date": entry_date or date.today().isoformat(),
            "username": username,
            "name": name,
            "team": team,
            "type": entry_type,
            "content": content.strip(),
            "priority": priority,
            "status": status,
            "created_at": now,
            "updated_at": now,
        }

        supabase.table("tasks").insert(new_row).execute()
        return True
    except Exception as e:
        st.error(f"Error adding entry: {e}")
        return False


def update_status(entry_id: str, new_status: str) -> bool:
    """Update status of a single entry."""
    try:
        supabase = get_supabase_client()
        supabase.table("tasks").update({
            "status": new_status,
            "updated_at": datetime.now().isoformat()
        }).eq("id", entry_id).execute()
        return True
    except Exception as e:
        st.error(f"Error updating status: {e}")
        return False


def delete_entry(entry_id: str) -> bool:
    """Delete an entry by ID."""
    try:
        supabase = get_supabase_client()
        supabase.table("tasks").delete().eq("id", entry_id).execute()
        return True
    except Exception as e:
        st.error(f"Error deleting entry: {e}")
        return False


def get_user_entries(username: str, entry_type: Optional[str] = None) -> pd.DataFrame:
    df = load_data()
    mask = df["username"] == username
    if entry_type:
        mask = mask & (df["type"] == entry_type)
    return df[mask].sort_values("created_at", ascending=False)


def get_entries_by_date(
    target_date: str,
    entry_type: Optional[str] = None,
    team: Optional[str] = None,
) -> pd.DataFrame:
    df = load_data()
    mask = df["date"] == target_date
    if entry_type:
        mask = mask & (df["type"] == entry_type)
    if team and team != "All Teams":
        mask = mask & (df["team"] == team)
    return df[mask].sort_values(["team", "name", "created_at"])


def get_open_tasks(team: Optional[str] = None) -> pd.DataFrame:
    df = load_data()
    mask = df["status"].isin(["Open", "In Progress"])
    if team and team != "All Teams":
        mask = mask & (df["team"] == team)
    return df[mask].sort_values(["team", "date", "priority"], ascending=[True, False, True])


def get_all_data() -> pd.DataFrame:
    return load_data().sort_values("created_at", ascending=False)
