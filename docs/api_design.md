# CampusGPT AI API Design

## Authentication

- `POST /api/auth/register`
- `POST /api/auth/login`
- `GET /api/auth/me`
- `POST /api/auth/refresh`

## Chat & AI

- `POST /api/chat/send` — user message, returns assistant answer and sources
- `GET /api/chat/history` — session messages and metadata
- `GET /api/chat/suggestions` — suggested questions for current context

## Documents & RAG

- `POST /api/admin/upload-document` — upload brochure / PDF / notice
- `GET /api/rag/search` — semantic query against knowledge base
- `POST /api/rag/index` — re-index documents after upload

## Analytics

- `GET /api/analytics/overview`
- `GET /api/analytics/usage-trends`
- `GET /api/analytics/top-queries`
- `GET /api/analytics/model-performance`

## Admin

- `GET /api/admin/users`
- `PATCH /api/admin/users/{user_id}`
- `GET /api/admin/faqs`
- `POST /api/admin/faqs`
- `PATCH /api/admin/faqs/{faq_id}`
- `DELETE /api/admin/faqs/{faq_id}`

## Recommendations

- `GET /api/recommendations/courses`
- `GET /api/recommendations/scholarships`
- `GET /api/recommendations/events`
- `GET /api/recommendations/placements`

## ML Evaluation

- `POST /api/ml/train`
- `GET /api/ml/models`
- `GET /api/ml/performance`

## Voice

- `POST /api/voice/tts`
- `POST /api/voice/stt`
