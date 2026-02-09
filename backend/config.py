import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH)

OPENAI_API_KEY = os.getenv("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")
