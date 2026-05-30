# CampusGPT AI Testing Strategy

## Testing Scope

- **Frontend UI tests** for auth flows, chat interactions, dashboard rendering.
- **Backend API tests** for auth, chat, analytics, admin, and recommendation endpoints.
- **ML pipeline tests** for model training, evaluation metrics, and semantic search.
- **RAG tests** for document ingestion and retrieval.
- **Integration tests** for end-to-end user scenarios.

## Recommended Tools

- Frontend: `Jest`, `React Testing Library`, `Playwright`
- Backend: `pytest`, `httpx`, `pytest-asyncio`
- ML: `scikit-learn` cross-validation and metrics
- Data validation: `pydantic`

## Example Test Cases

- Register a new student and confirm JWT token issuance.
- Send chat messages and ensure context is preserved.
- Upload a PDF and verify vector store indexing.
- Validate model accuracy and compare Logistic Regression / Naive Bayes / Random Forest scores.
- Confirm admin user can manage FAQs and announcements.

## Release Validation

- Smoke test all public API routes.
- Verify dashboard analytics update with simulated usage.
- Confirm voice TTS/STT endpoints return valid payloads.
