from fastapi import FastAPI
from pydantic import BaseModel
from backend.services.llm_service import generate_content
from backend.services.vector_service import search
from backend.utils.formatter import clean_output, format_as_markdown
from pathlib import Path
from services.vector_service import load_documents

app = FastAPI()
def startup_event():
    load_documents()

BASE_DIR = Path(__file__).resolve().parent
PROMPT_PATH = BASE_DIR / "prompts" / "match_recap_prompt.txt"

class MatchRequest(BaseModel):
    sport: str
    teams: str
    score: str
    moments: str
    tone: str

@app.post("/generate")
def generate_match_recap(request: MatchRequest):

    with open(PROMPT_PATH, "r", encoding="utf-8") as f:
        template = f.read()

    retrieved_docs = search(request.moments, sport_filter=request.sport)

    prompt = template.format(
        sport=request.sport,
        teams=request.teams,
        score=request.score,
        moments=request.moments + "\nContext:\n" + "\n".join(retrieved_docs),
        tone=request.tone
    )

    content = generate_content(prompt)

    # 👇 Formatting Layer
    content = clean_output(content)
    content = format_as_markdown(content)

    return {"recap": content}
