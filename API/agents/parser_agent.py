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
load_dotenv()

#Agent pre setup
pdf_path = "test_documents/attention.pdf"
vectorstore = create_or_load_vectorstore(pdf_path)
retriever_tool = build_retriever_tool(vectorstore)
parse_agent_Tools = [retriever_tool]
llm = ChatGroq(
    model="openai/gpt-oss-safeguard-20b",
    temperature=0,
    max_tokens=None,
    reasoning_format="parsed",
    timeout=None,
    max_retries=2, 
    # other params...
)
parse_llm_with_tools = llm.bind_tools(parse_agent_Tools)

parse_agent_prompt = """
You are a Research Document Parsing Agent.

- Do NOT wait for user input or paper name
- Go directly to the vector database and extract
- Do NOT ask questions
- Use the document retrieval tool to read the paper
Steps:
1. Call the database_search tool MULTIPLE times with different queries:
   - "abstract of the paper"
   - "methodology"
   - "mathematical equations"
   - "experiments and dataset"
   - "results and evaluation"

2. Combine all retrieved content

3. Return structured JSON:

{
  "Abstract": "...",
  "Method": "...",
  "Math": "...",
  "Experiments": "...",
  "Results": "...",
  "Youtube": "search query to learn this paper"
}

Rules:
- MUST use the tool multiple times
- DO NOT hallucinate
- Output ONLY JSON
"""

parse_agent = create_agent(
    model=parse_llm_with_tools,  # or any other supported model identifier string
    tools=parse_agent_Tools,
    system_prompt=parse_agent_prompt
)


inputs = {"messages": [{"role": "user", "content": "Analyze the given research paper"}]}
result_parse_agent=parse_agent.invoke(inputs)
print(result_parse_agent["messages"][-1].content)


