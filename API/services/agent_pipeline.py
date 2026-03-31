import asyncio
from agents.teach_agent import teach_agent
from agents.math_agent import math_agent
from agents.experiment_agent import experimental_analysis_agent
from dotenv import load_dotenv
load_dotenv()

async def run_agent(agent, context, prompt):
    result = agent.invoke({
        "messages": [{"role": "user", "content": prompt + context}]
    })
    return result["messages"][-1].content


async def run_all_agents(contexts):
    tasks = [
        run_agent(teach_agent, contexts["teach"], "Teach me this research paper context"),
        run_agent(math_agent, contexts["math"], "explain all the Mathematical terms in this research paper"),
        run_agent(experimental_analysis_agent, contexts["experiment"], "experiment analysis on the given research paper")
    ]

    results = await asyncio.gather(*tasks)

    return {
        "teach": results[0],
        "math": results[1],
        "experiment": results[2]
    }