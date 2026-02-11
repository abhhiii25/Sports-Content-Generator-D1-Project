import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH)

OPENAI_API_KEY = os.getenv("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")
