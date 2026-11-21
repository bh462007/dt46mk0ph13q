"""Vercel entrypoint.

Vercel finds a FastAPI instance named `app` by reading this file, so one is created here
and the real application under backend/ is mounted on it.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "backend"))

from app.main import app as api  # noqa: E402
from fastapi import FastAPI  # noqa: E402

app = FastAPI()
app.mount("/", api)