from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..core import schemas, models
from ..core.database import get_db
from ..services import nlp, rag

router = APIRouter()

@router.post("/send")
def send_message(payload: dict, db: Session = Depends(get_db)):
    message = payload.get("message")
    session_id = payload.get("session_id")
    user_id = payload.get("user_id")
    if not message or not session_id:
        raise HTTPException(status_code=400, detail="Message and session_id are required")
    intent, entities = nlp.classify_intent(message)
    sources, context = rag.retrieve_relevant_context(message)
    response = nlp.generate_response(message, intent, entities, context)
    history = models.ChatHistory(
        session_id=session_id,
        user_id=user_id,
        role="user",
        content=message,
        metadata=str({"intent": intent, "entities": entities}),
    )
    db.add(history)
    db.commit()
    assistant_item = models.ChatHistory(
        session_id=session_id,
        user_id=user_id,
        role="assistant",
        content=response,
        metadata=str({"sources": sources}),
    )
    db.add(assistant_item)
    db.commit()
    return {"message": response, "sources": sources, "intent": intent, "entities": entities}

@router.get("/history", response_model=List[schemas.ChatMessage])
def get_history(session_id: str, db: Session = Depends(get_db)):
    return db.query(models.ChatHistory).filter(models.ChatHistory.session_id == session_id).order_by(models.ChatHistory.timestamp).all()

@router.get("/suggestions")
def get_suggestions():
    return {"suggestions": [
        "What are the application deadlines?",
        "Which courses are available in engineering?",
        "How do I apply for scholarships?",
        "What are the placement statistics for 2025?",
    ]}
