from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..core import schemas, models
from ..core.database import get_db
from ..services import rag

router = APIRouter()

@router.post("/upload-document")
def upload_document(name: str, file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file.filename.lower().endswith((".pdf", ".txt", ".docx")):
        raise HTTPException(status_code=400, detail="Unsupported file type")
    content = file.file.read()
    rag.index_document(file.filename, content)
    return {"message": "Document uploaded and indexed"}

@router.get("/faqs", response_model=List[schemas.FAQOut])
def list_faqs(db: Session = Depends(get_db)):
    return db.query(models.FAQ).order_by(models.FAQ.created_at.desc()).all()

@router.post("/faqs", response_model=schemas.FAQOut)
def create_faq(faq: schemas.FAQCreate, db: Session = Depends(get_db)):
    faq_item = models.FAQ(**faq.dict())
    db.add(faq_item)
    db.commit()
    db.refresh(faq_item)
    return faq_item
