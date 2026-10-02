from pathlib import Path

from backend.app.config import settings


def ensure_directories() -> None:
    paths = [
        Path("backend/data/knowledge"),
        Path("backend/app/prompts"),
        Path("backend/tests"),
    ]
    for path in paths:
        path.mkdir(parents=True, exist_ok=True)
