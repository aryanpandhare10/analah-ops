"""
Authentication + Team structure for Analah Capital Ops Platform
"""

import streamlit as st
from typing import Optional, Dict, Any

# ============================================================
# USERS + TEAMS
# Username is lowercase, password is temporary (change later)
# ============================================================

USERS: Dict[str, Dict[str, Any]] = {
    # -------------------- ADMIN --------------------
    "admin": {
        "password": "Analah@Admin2026",
        "name": "Administrator",
        "role": "admin",
        "team": "Admin",
        "email": "admin@analah.com",
    },

    # -------------------- Team: Harshad Pacharane --------------------
    "harshad": {
        "password": "harshad123",
        "name": "Harshad Pacharane",
        "role": "user",
        "team": "Harshad Pacharane",
        "email": "",
    },
    "adwait": {
        "password": "adwait123",
        "name": "Adwait Nandkumar Kadam",
        "role": "user",
        "team": "Harshad Pacharane",
        "email": "",
    },
    "aishwarya": {
        "password": "aishwarya123",
        "name": "Aishwarya Kshatriya",
        "role": "user",
        "team": "Harshad Pacharane",
        "email": "",
    },
    "jahnavi": {
        "password": "jahnavi123",
        "name": "Jahnavi Singh",
        "role": "user",
        "team": "Harshad Pacharane",
        "email": "",
    },
    "kanchi": {
        "password": "kanchi123",
        "name": "Kanchi Doshi",
        "role": "user",
        "team": "Harshad Pacharane",
        "email": "",
    },
    "tanu": {
        "password": "tanu123",
        "name": "Tanu Soni",
        "role": "user",
        "team": "Harshad Pacharane",
        "email": "",
    },

    # -------------------- Team: Kinjal Gharawala --------------------
    "kinjal": {
        "password": "kinjal123",
        "name": "Kinjal Gharawala",
        "role": "user",
        "team": "Kinjal Gharawala",
        "email": "",
    },
    "gurneesh": {
        "password": "gurneesh123",
        "name": "Gurneesh Kaur Chhabra",
        "role": "user",
        "team": "Kinjal Gharawala",
        "email": "",
    },
    "himalay": {
        "password": "himalay123",
        "name": "Himalay Mhatre",
        "role": "user",
        "team": "Kinjal Gharawala",
        "email": "",
    },
    "kunjal": {
        "password": "kunjal123",
        "name": "Kunjal Mehta",
        "role": "user",
        "team": "Kinjal Gharawala",
        "email": "",
    },
    "dhwani": {
        "password": "dhwani123",
        "name": "Dhwani Trivedi",
        "role": "user",
        "team": "Kinjal Gharawala",
        "email": "",
    },
    "yash": {
        "password": "yash123",
        "name": "Yash Waghela",
        "role": "user",
        "team": "Kinjal Gharawala",
        "email": "",
    },
    "kalyanram": {
        "password": "kalyanram123",
        "name": "Kalyanram",
        "role": "user",
        "team": "Kinjal Gharawala",
        "email": "",
    },
    "rohan": {
        "password": "rohan123",
        "name": "Rohan Bandivadekar",
        "role": "user",
        "team": "Kinjal Gharawala",
        "email": "",
    },
    "harshp": {
        "password": "harshp123",
        "name": "Harsh Ashwin Panchal",
        "role": "user",
        "team": "Kinjal Gharawala",
        "email": "",
    },
    "neeraj": {
        "password": "neeraj123",
        "name": "Neeraj Jovharani",
        "role": "user",
        "team": "Kinjal Gharawala",
        "email": "",
    },

    # -------------------- Team: Jitesh Mhatre --------------------
    "jitesh": {
        "password": "jitesh123",
        "name": "Jitesh Mhatre",
        "role": "user",
        "team": "Jitesh Mhatre",
        "email": "",
    },
    "shubham": {
        "password": "shubham123",
        "name": "Shubham Bagawade",
        "role": "user",
        "team": "Jitesh Mhatre",
        "email": "",
    },
    "sneha": {
        "password": "sneha123",
        "name": "Sneha Morya",
        "role": "user",
        "team": "Jitesh Mhatre",
        "email": "",
    },
    "swarni": {
        "password": "swarni123",
        "name": "Swarni Tharwal",
        "role": "user",
        "team": "Jitesh Mhatre",
        "email": "",
    },
    "vaishnavi_v": {
        "password": "vaishnavi123",
        "name": "Vaishnavi Vaknalli",
        "role": "user",
        "team": "Jitesh Mhatre",
        "email": "",
    },
    "fatema": {
        "password": "fatema123",
        "name": "Fatema Colombowala",
        "role": "user",
        "team": "Jitesh Mhatre",
        "email": "",
    },

    # -------------------- Team: Nupur Gawand --------------------
    "nupur": {
        "password": "nupur123",
        "name": "Nupur Gawand",
        "role": "user",
        "team": "Nupur Gawand",
        "email": "",
    },
    "binita": {
        "password": "binita123",
        "name": "Binita Sanjay Desai",
        "role": "user",
        "team": "Nupur Gawand",
        "email": "",
    },
    "sandali": {
        "password": "sandali123",
        "name": "Sandali Wagh",
        "role": "user",
        "team": "Nupur Gawand",
        "email": "",
    },
    "ritika": {
        "password": "ritika123",
        "name": "Ritika Girdhani",
        "role": "user",
        "team": "Nupur Gawand",
        "email": "",
    },
    "karishma": {
        "password": "karishma123",
        "name": "Karishma Birendra Yadav",
        "role": "user",
        "team": "Nupur Gawand",
        "email": "",
    },
    "rajpournima": {
        "password": "rajpournima123",
        "name": "Rajpournima B",
        "role": "user",
        "team": "Nupur Gawand",
        "email": "",
    },

    # -------------------- Team: Snehashish Mate --------------------
    "snehashish": {
        "password": "snehashish123",
        "name": "Snehashish Mate",
        "role": "user",
        "team": "Snehashish Mate",
        "email": "",
    },
    "jyoti": {
        "password": "jyoti123",
        "name": "Jyoti Rani",
        "role": "user",
        "team": "Snehashish Mate",
        "email": "",
    },
    "kamiya": {
        "password": "kamiya123",
        "name": "Kamiya Sahetai",
        "role": "user",
        "team": "Snehashish Mate",
        "email": "",
    },
    "kashish_c": {
        "password": "kashish123",
        "name": "Kashish Chheda",
        "role": "user",
        "team": "Snehashish Mate",
        "email": "",
    },
    "kunal": {
        "password": "kunal123",
        "name": "Kunal Rathod",
        "role": "user",
        "team": "Snehashish Mate",
        "email": "",
    },

    # -------------------- Team: Krish Anam --------------------
    "krish": {
        "password": "krish123",
        "name": "Krish Anam",
        "role": "user",
        "team": "Krish Anam",
        "email": "",
    },
    "mayank": {
        "password": "mayank123",
        "name": "Mayank Shukla",
        "role": "user",
        "team": "Krish Anam",
        "email": "",
    },
    "vaishnavi_d": {
        "password": "vaishnavi123",
        "name": "Vaishnavi Narayan Dhuri",
        "role": "user",
        "team": "Krish Anam",
        "email": "",
    },
    "nidhi": {
        "password": "nidhi123",
        "name": "Nidhi Prajapati",
        "role": "user",
        "team": "Krish Anam",
        "email": "",
    },
    "nimisha": {
        "password": "nimisha123",
        "name": "Nimisha Nagesh Dhuri",
        "role": "user",
        "team": "Krish Anam",
        "email": "",
    },

    # -------------------- Team: Shweta K --------------------
    "shweta": {
        "password": "shweta123",
        "name": "Shweta K",
        "role": "user",
        "team": "Shweta K",
        "email": "",
    },
    "dhruv": {
        "password": "dhruv123",
        "name": "Dhruv Rathod",
        "role": "user",
        "team": "Shweta K",
        "email": "",
    },
    "shreya": {
        "password": "shreya123",
        "name": "Shreya Tonpe",
        "role": "user",
        "team": "Shweta K",
        "email": "",
    },
    "nikkee": {
        "password": "nikkee123",
        "name": "Nikkee Khuswaha",
        "role": "user",
        "team": "Shweta K",
        "email": "",
    },
    "gaurav": {
        "password": "gaurav123",
        "name": "Gaurav Sayaji Kashid",
        "role": "user",
        "team": "Shweta K",
        "email": "",
    },

    # -------------------- Team: Vyshnavi Doki --------------------
    "vyshnavi": {
        "password": "vyshnavi123",
        "name": "Vyshnavi Doki",
        "role": "user",
        "team": "Vyshnavi Doki",
        "email": "",
    },
    "sankalp": {
        "password": "sankalp123",
        "name": "Sankalp Mishra",
        "role": "user",
        "team": "Vyshnavi Doki",
        "email": "",
    },
    "priyal": {
        "password": "priyal123",
        "name": "Priyal Manish Mhatre",
        "role": "user",
        "team": "Vyshnavi Doki",
        "email": "",
    },
    "riddhi": {
        "password": "riddhi123",
        "name": "Riddhi Pandey",
        "role": "user",
        "team": "Vyshnavi Doki",
        "email": "",
    },
    "sakshi_s": {
        "password": "sakshi123",
        "name": "Sakshi Subodh Shinde",
        "role": "user",
        "team": "Vyshnavi Doki",
        "email": "",
    },
    "rohit": {
        "password": "rohit123",
        "name": "Rohit Maurya",
        "role": "user",
        "team": "Vyshnavi Doki",
        "email": "",
    },
    "kashish_v": {
        "password": "kashish123",
        "name": "Kashish Verma",
        "role": "user",
        "team": "Vyshnavi Doki",
        "email": "",
    },

    # -------------------- Team: Rutik Mokal --------------------
    "rutik": {
        "password": "rutik123",
        "name": "Rutik Mokal",
        "role": "user",
        "team": "Rutik Mokal",
        "email": "",
    },
    "aditya": {
        "password": "aditya123",
        "name": "Aditya Joshi",
        "role": "user",
        "team": "Rutik Mokal",
        "email": "",
    },
    "ankita": {
        "password": "ankita123",
        "name": "Ankita Sahebrao Jadhav",
        "role": "user",
        "team": "Rutik Mokal",
        "email": "",
    },
    "divya": {
        "password": "divya123",
        "name": "Divya Sharma",
        "role": "user",
        "team": "Rutik Mokal",
        "email": "",
    },

    # -------------------- Team: Pratikasha Awate --------------------
    "pratikasha": {
        "password": "pratikasha123",
        "name": "Pratikasha Awate",
        "role": "user",
        "team": "Pratikasha Awate",
        "email": "",
    },
    "pratham": {
        "password": "pratham123",
        "name": "Pratham Shetty",
        "role": "user",
        "team": "Pratikasha Awate",
        "email": "",
    },
    "durvi": {
        "password": "durvi123",
        "name": "Durvi Makarand Dalvi",
        "role": "user",
        "team": "Pratikasha Awate",
        "email": "",
    },
    "anushka": {
        "password": "anushka123",
        "name": "Anushka Nikam",
        "role": "user",
        "team": "Pratikasha Awate",
        "email": "",
    },

    # -------------------- Team: Roshen Mandumpala --------------------
    "roshen": {
        "password": "roshen123",
        "name": "Roshen Mandumpala",
        "role": "user",
        "team": "Roshen Mandumpala",
        "email": "",
    },
    "sreemurali": {
        "password": "sreemurali123",
        "name": "Acharya Sreemurali",
        "role": "user",
        "team": "Roshen Mandumpala",
        "email": "",
    },

    # -------------------- Team: Shivam Rathore --------------------
    "shivam": {
        "password": "shivam123",
        "name": "Shivam Rathore",
        "role": "user",
        "team": "Shivam Rathore",
        "email": "",
    },
    "jash": {
        "password": "jash123",
        "name": "Jash Shinde",
        "role": "user",
        "team": "Shivam Rathore",
        "email": "",
    },
    "abhijeet": {
        "password": "abhijeet123",
        "name": "Abhijeet Singh Shekhawat",
        "role": "user",
        "team": "Shivam Rathore",
        "email": "",
    },
    "ashvi": {
        "password": "ashvi123",
        "name": "Ashvi Jain",
        "role": "user",
        "team": "Shivam Rathore",
        "email": "",
    },
    "dimple": {
        "password": "dimple123",
        "name": "Dimple Mishra",
        "role": "user",
        "team": "Shivam Rathore",
        "email": "",
    },
    "himanshu": {
        "password": "himanshu123",
        "name": "Himanshu Verma",
        "role": "user",
        "team": "Shivam Rathore",
        "email": "",
    },
    "sonali": {
        "password": "sonali123",
        "name": "Sonali Soni",
        "role": "user",
        "team": "Shivam Rathore",
        "email": "",
    },
    "priyanshi": {
        "password": "priyanshi123",
        "name": "Priyanshi Mangal",
        "role": "user",
        "team": "Shivam Rathore",
        "email": "",
    },
    "vanshika": {
        "password": "vanshika123",
        "name": "Vanshika Bhargava",
        "role": "user",
        "team": "Shivam Rathore",
        "email": "",
    },
    "yuvraj": {
        "password": "yuvraj123",
        "name": "Yuvraj Sethi",
        "role": "user",
        "team": "Shivam Rathore",
        "email": "",
    },
    "tarun": {
        "password": "tarun123",
        "name": "Tarun Saharan",
        "role": "user",
        "team": "Shivam Rathore",
        "email": "",
    },
    "khushbu": {
        "password": "khushbu123",
        "name": "Khushbu Jangid",
        "role": "user",
        "team": "Shivam Rathore",
        "email": "",
    },

    # -------------------- Team: Charchit Tak --------------------
    "charchit": {
        "password": "charchit123",
        "name": "Charchit Tak",
        "role": "user",
        "team": "Charchit Tak",
        "email": "",
    },
    "sakshi_b": {
        "password": "sakshi123",
        "name": "Sakshi Beluniya",
        "role": "user",
        "team": "Charchit Tak",
        "email": "",
    },
    "akash": {
        "password": "akash123",
        "name": "Akash Kumar",
        "role": "user",
        "team": "Charchit Tak",
        "email": "",
    },
    "ritik": {
        "password": "ritik123",
        "name": "Ritik Soni",
        "role": "user",
        "team": "Charchit Tak",
        "email": "",
    },

    # -------------------- Team: Muskan Vaswani --------------------
    "muskan": {
        "password": "muskan123",
        "name": "Muskan Vaswani",
        "role": "user",
        "team": "Muskan Vaswani",
        "email": "",
    },
    "ayush": {
        "password": "ayush123",
        "name": "Ayush Kumar Singh",
        "role": "user",
        "team": "Muskan Vaswani",
        "email": "",
    },
    "ayushi": {
        "password": "ayushi123",
        "name": "Ayushi Jain",
        "role": "user",
        "team": "Muskan Vaswani",
        "email": "",
    },
    "jay": {
        "password": "jay123",
        "name": "Jay Jogi",
        "role": "user",
        "team": "Muskan Vaswani",
        "email": "",
    },
    "mehak": {
        "password": "mehak123",
        "name": "Mehak Gauba",
        "role": "user",
        "team": "Muskan Vaswani",
        "email": "",
    },
    "vishal": {
        "password": "vishal123",
        "name": "Vishal Chandani",
        "role": "user",
        "team": "Muskan Vaswani",
        "email": "",
    },
    "bhumika": {
        "password": "bhumika123",
        "name": "Bhumika Dusane",
        "role": "user",
        "team": "Muskan Vaswani",
        "email": "",
    },

    # -------------------- Team: Nikita Tilwani --------------------
    "nikita": {
        "password": "nikita123",
        "name": "Nikita Tilwani",
        "role": "user",
        "team": "Nikita Tilwani",
        "email": "",
    },
    "chandni": {
        "password": "chandni123",
        "name": "Chandni Shekhawat",
        "role": "user",
        "team": "Nikita Tilwani",
        "email": "",
    },
    "krishna": {
        "password": "krishna123",
        "name": "Krishna Sharma",
        "role": "user",
        "team": "Nikita Tilwani",
        "email": "",
    },
    "deepti": {
        "password": "deepti123",
        "name": "Deepti Gupta",
        "role": "user",
        "team": "Nikita Tilwani",
        "email": "",
    },
    "shraddha": {
        "password": "shraddha123",
        "name": "Shraddha Goyal",
        "role": "user",
        "team": "Nikita Tilwani",
        "email": "",
    },

    # -------------------- Team: Sankalp Mishra (separate) --------------------
    "dinesh": {
        "password": "dinesh123",
        "name": "Dinesh Panwar",
        "role": "user",
        "team": "Sankalp Mishra",
        "email": "",
    },
    "shashwat": {
        "password": "shashwat123",
        "name": "Shashwat Shrivastava",
        "role": "user",
        "team": "Sankalp Mishra",
        "email": "",
    },
    "stephen": {
        "password": "stephen123",
        "name": "Stephen Ranadive",
        "role": "user",
        "team": "Sankalp Mishra",
        "email": "",
    },
    "suraj": {
        "password": "suraj123",
        "name": "Suraj Mishra",
        "role": "user",
        "team": "Sankalp Mishra",
        "email": "",
    },

    # -------------------- Team: Taniya Sharma --------------------
    "taniya": {
        "password": "taniya123",
        "name": "Taniya Sharma",
        "role": "user",
        "team": "Taniya Sharma",
        "email": "",
    },
}


def check_login(username: str, password: str) -> Optional[Dict[str, Any]]:
    user = USERS.get(username.strip().lower())
    if user and user["password"] == password:
        return {
            "username": username.strip().lower(),
            "name": user["name"],
            "role": user["role"],
            "team": user.get("team", "Unknown"),
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


def get_all_teams() -> list:
    """Return sorted list of unique teams (excluding Admin)."""
    teams = set()
    for user in USERS.values():
        team = user.get("team")
        if team and team != "Admin":
            teams.add(team)
    return sorted(list(teams))
