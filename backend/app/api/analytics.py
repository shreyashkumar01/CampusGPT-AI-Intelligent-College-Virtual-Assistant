from fastapi import APIRouter
from ..services.recommendation import get_usage_insights

router = APIRouter()

@router.get("/overview")
def overview():
    return {
        "total_users": 1240,
        "active_users": 214,
        "total_conversations": 10932,
        "top_categories": ["Admissions", "Scholarships", "Placements", "Hostel"],
        "user_satisfaction": 4.6,
    }

@router.get("/usage-trends")
def usage_trends():
    return get_usage_insights()

@router.get("/top-queries")
def top_queries():
    return [
        {"query": "How do I apply for a scholarship?", "count": 182},
        {"query": "What are the hostel facilities?", "count": 139},
    ]

@router.get("/model-performance")
def model_performance():
    return [
        {"model_name": "Logistic Regression", "accuracy": 0.89, "precision": 0.87, "recall": 0.85, "f1_score": 0.86},
        {"model_name": "Naive Bayes", "accuracy": 0.83, "precision": 0.81, "recall": 0.80, "f1_score": 0.80},
        {"model_name": "Random Forest", "accuracy": 0.91, "precision": 0.90, "recall": 0.89, "f1_score": 0.89},
    ]
