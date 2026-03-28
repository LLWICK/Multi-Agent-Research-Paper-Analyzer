from fastapi import APIRouter
from models.schemas import AnalyzeRequest
from services.context_manager import split_context
from services.agent_pipeline import run_all_agents
from agents.parser_agent import parse_agent

router = APIRouter()

@router.post("/analyze")
async def analyze(req: AnalyzeRequest):

    parsed = parse_agent.invoke({
        "messages": [{"role": "user", "content": req.query}]
    })

    parsed_content = parsed["messages"][-1].content

    contexts = split_context(parsed_content)

    results = await run_all_agents(contexts)

    return results