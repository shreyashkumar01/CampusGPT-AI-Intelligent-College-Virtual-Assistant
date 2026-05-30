from typing import Any, Dict


def build_response(text: str, sources: list, meta: Dict[str, Any] = None) -> Dict[str, Any]:
    return {
        "answer": text,
        "sources": sources,
        "meta": meta or {},
    }
