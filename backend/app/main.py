from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import auth, chat, admin, analytics, users
from .core.config import settings

app = FastAPI(
    title="CampusGPT AI Backend",
    description="API server for CampusGPT AI college assistant",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(chat.router, prefix="/api/chat", tags=["chat"])
app.include_router(admin.router, prefix="/api/admin", tags=["admin"])
app.include_router(analytics.router, prefix="/api/analytics", tags=["analytics"])
app.include_router(users.router, prefix="/api/users", tags=["users"])

@app.get("/api/health")
def health_check():
    return {"status": "ok", "service": "CampusGPT AI Backend"}
