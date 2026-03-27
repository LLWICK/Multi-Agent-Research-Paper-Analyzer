import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
# Get the path to the parent directory (one level up)
parent_dir = os.path.dirname(current_dir)
# Add the parent directory to the system path
sys.path.append(parent_dir)

from tools.retriever_tool import retriever_tool
from langchain.agents import create_agent
from langchain.tools import tool
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
load_dotenv()

#Agent pre setup
parse_agent_Tools = [retriever_tool]
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
    max_tokens=None,
    reasoning_format="parsed",
    timeout=None,
    max_retries=2, 
    # other params...
)
parse_llm_with_tools = llm.bind_tools(parse_agent_Tools)

parse_agent_prompt = """You are the Research Document Parsing Agent. 
First Use the given retriver_tool Tool to get research paper context and  You Read the given  research paper  Fully and divide them into Abstract, Method, Math, Experiments, Results, Youtube.
Rules:
- Do NOT wait for user input or paper name
- Go directly to the vector database and extract
- Do NOT ask questions
- Use the document retrieval tool to read the paper
- Be concise but complete
- GIVE THE FINAL RESULT IN JSON KEY VALUE PAIRS JUST JSON NO JARGON NO STRING
- Include a search query for YOUTUBE to learn more aboute the content on research paper. Don't search youtube just provide query only
"""

parse_agent = create_agent(
    model=parse_llm_with_tools,  # or any other supported model identifier string
    tools=parse_agent_Tools,
    system_prompt=parse_agent_prompt
)

inputs = {"messages": [{"role": "user", "content": "Analyze the given research paper"}]}
result_parse_agent=parse_agent.invoke(inputs)
print(result_parse_agent["messages"][-1].content)