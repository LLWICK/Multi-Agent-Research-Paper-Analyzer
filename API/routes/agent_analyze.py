from fastapi import APIRouter
from fastapi import APIRouter, UploadFile, File
import shutil
from services.context_manager import split_context
from services.agent_pipeline import run_all_agents
from agents.parser_agent import praser_Agent
from dotenv import load_dotenv
from pathlib import Path
load_dotenv()
import os

router = APIRouter()

@router.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    #path = Path("temp") / file.filename
    #path.parent.mkdir(parents=True, exist_ok=True)

    BASE_DIR = Path(__file__).resolve().parent.parent.parent # adjust if needed

    file_path = BASE_DIR  / "test_documents" / str(file.filename)
    file_path = file_path.resolve()

    


    parsed = praser_Agent(file_path)

    

    contexts = split_context(parsed)

    results = await run_all_agents(contexts)
    
    
   
    return {
        "results": results
    };