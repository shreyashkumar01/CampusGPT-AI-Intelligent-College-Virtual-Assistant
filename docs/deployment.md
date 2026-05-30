# CampusGPT AI Deployment

## Frontend

- Deploy `frontend/` to Vercel.
- Build command: `npm run build`
- Output directory: `.next`
- Environment variables:
  - `NEXT_PUBLIC_API_URL`
  - `NEXT_PUBLIC_APP_NAME`

## Backend

- Deploy `backend/` to Render or similar.
- Start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
- Environment variables:
  - `DATABASE_URL`
  - `SECRET_KEY`
  - `ACCESS_TOKEN_EXPIRE_MINUTES`
  - `SENTENCE_TRANSFORMERS_MODEL`
  - `CHROMA_DB_PATH`

## Database

- Use Supabase PostgreSQL.
- Apply schema migrations from `backend/app/core/models.py` or Alembic.

## Vector Store

- Use local ChromaDB for development.
- For production, configure persistent object storage or hosted vector database.

## Scaling

- Use autoscaling on Render.
- Store embeddings and document metadata in a scalable store.
- Use Redis for caching conversation context if needed.
