"""Settings loaded from .env.
-> HOST, API_KEY, MODEL: LLM endpoint config (required).
-> PORT: HTTP port, defaults to 8000.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).with_name(".env"))

HOST = os.environ["HOST"]
API_KEY = os.environ["API_KEY"]
MODEL = os.environ["MODEL"]
PORT = int(os.getenv("PORT", "8000"))
