from pathlib import Path

from backend.app.config import settings


def ingest_documents(directory: str = "backend/data/knowledge") -> None:
    docs_dir = Path(directory)
    if docs_dir.exists():
        for file in docs_dir.glob("*.txt"):
            print(f"Loaded knowledge document: {file.name}")
    else:
        print(f"No local knowledge directory found at {directory}")
