from typing import Tuple, List
from .ml_pipeline import load_intent_model

_intent_model = load_intent_model()


def classify_intent(text: str) -> Tuple[str, List[str]]:
    if not text:
        return "unknown", []
    prediction = _intent_model.predict([text])[0]
    entities = []
    if "admission" in text.lower():
        entities.append("admission")
    if "scholarship" in text.lower():
        entities.append("scholarship")
    return prediction, entities


def generate_response(message: str, intent: str, entities: List[str], context: str) -> str:
    base = "Here is the answer based on CampusGPT AI knowledge base."
    if intent == "admission":
        return f"{base} For admissions, you need to submit transcripts, entrance exam score, and identity documents."
    if intent == "placement":
        return f"{base} Placement insights: top recruiters include Deloitte, TCS, Microsoft, and placement rate is above 85%."
    return f"{base} I also found these topics: {', '.join(entities) if entities else 'general college support'}."
