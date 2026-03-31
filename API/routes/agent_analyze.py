from fastapi import APIRouter
from fastapi import APIRouter, UploadFile, File
import shutil
from services.context_manager import split_context
from services.agent_pipeline import run_all_agents
from agents.parser_agent import praser_Agent
from dotenv import load_dotenv
from pathlib import Path
load_dotenv()

router = APIRouter()

@router.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    path = Path("temp") / file.filename
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)


    #parsed = praser_Agent(path)

    #parsed_content = parsed["messages"][-1].content

    """ contexts = split_context(parsed_content)

    results = await run_all_agents(contexts) """

    return {"p":path};