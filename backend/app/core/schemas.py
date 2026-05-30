from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
    role: Optional[str] = None

class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    role: str = Field("student", description="student, faculty, admin")

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True

class ChatMessage(BaseModel):
    id: Optional[int]
    session_id: str
    user_id: Optional[int]
    role: str
    content: str
    timestamp: Optional[datetime]

    class Config:
        orm_mode = True

class FAQCreate(BaseModel):
    question: str
    answer: str
    category: Optional[str] = None

class FAQOut(FAQCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class MLModelPerformance(BaseModel):
    model_name: str
    accuracy: float
    precision: float
    recall: float
    f1_score: float
    confusion_matrix: List[List[int]]
