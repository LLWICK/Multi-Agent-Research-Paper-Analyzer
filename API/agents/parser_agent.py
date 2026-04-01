import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
# Get the path to the parent directory (one level up)
parent_dir = os.path.dirname(current_dir)
# Add the parent directory to the system path
sys.path.append(parent_dir)

from tools.retriever_tool import build_retriever_tool
from langchain.agents import create_agent
from langchain.tools import tool
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from services.vectore_store import create_or_load_vectorstore
from langchain_ollama import ChatOllama
from services.Structured_output import PaperOutput
load_dotenv()

#Agent pre setup

def praser_Agent(pdf_path):

    vectorstore = create_or_load_vectorstore(pdf_path)
    retriever_tool = build_retriever_tool(vectorstore)
    parse_agent_Tools = [retriever_tool]

  

    llm = ChatOllama(
        model="llama3.2",
        temperature=0,
        # other params...
    )
    

    """ llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
    max_tokens=None,
    reasoning_format="parsed",
    timeout=None,
    max_retries=2, 
    # other params...
) """
    parse_llm_with_tools = llm.bind_tools(parse_agent_Tools)
    
    

    parse_agent_prompt = """
You are a Research Document Parsing Agent.

Your job is to extract structured information from a research paper using the database_search tool.

Instructions:
- Use the retriever_tool tool to retrieve relevant sections of the paper
- You may call the tool multiple times if needed
- Do NOT ask the user anything
- Do NOT make up information
- Only use retrieved content

What to extract:
- Abstract(Descriptive Abstract with Research Paper Name)
- Method
- Math (equations or formulas)
- Experiments (datasets, setup with with Research Paper Name)
- Results (performance, evaluation)
- Youtube (YouTube search query which strictly represents the paperto find the more information about this paper NOT YOUTUBE LINKS JUST SEARCH QUERY )

Output format (STRICT):
Return ONLY valid JSON with this structure:

{
  "Abstract": "...",
  "Method": "...",
  "Math": "...",
  "Experiments": "...",
  "Results": "...",
  "Youtube": "..."
}

Rules:
- No extra text outside JSON
-descriptive details PLEASE DO NOT SUMMARIZE DETAILS MAKE IT DESCRIPTIVE 
-don't miss any important detail on research paper
- If something is not found, return "Not found"
"""

    parse_agent = create_agent(
        model=parse_llm_with_tools,  # or any other supported model identifier string
        tools=parse_agent_Tools,
        system_prompt=parse_agent_prompt
    )


    inputs = {"messages": [{"role": "user", "content": "Analyze the given research paper"}]}
    result_parse_agent=parse_agent.invoke(inputs)
    raw_text =  result_parse_agent["messages"][-1].content
    structured_llm = llm.with_structured_output(PaperOutput)
    final_output = structured_llm.invoke(raw_text)

    return final_output.dict()
    




