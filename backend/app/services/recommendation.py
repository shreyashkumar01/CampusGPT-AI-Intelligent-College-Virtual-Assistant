from typing import Dict, Any


def get_course_recommendations(user_interest: str) -> Dict[str, Any]:
    return {
        "courses": [
            {"name": "B.Tech Computer Science", "eligibility": "JEE / 75% in 12th"},
            {"name": "BBA with Data Analytics", "eligibility": "50% in 12th"},
        ],
        "top_reasons": ["Strong placement ecosystem", "Industry-aligned curriculum"],
    }


def get_usage_insights() -> Dict[str, Any]:
    return {
        "daily": [
            {"date": "2026-05-24", "sessions": 130},
            {"date": "2026-05-25", "sessions": 156},
            {"date": "2026-05-26", "sessions": 174},
            {"date": "2026-05-27", "sessions": 191},
            {"date": "2026-05-28", "sessions": 214},
        ],
        "weekly": [
            {"week": "Week 20", "sessions": 920},
            {"week": "Week 21", "sessions": 1032},
        ],
    }
