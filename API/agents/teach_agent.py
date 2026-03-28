## Agents
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper


teaching_agent_prompt = """You are the Teaching Assistant Agent. 
Read the given context carefully and explain the key concepts, Architecture ideas , algorithm intuition using 
simple language, Analogies and step by step reasoning so even a complete beginner could understand.Use the tools only if you want.
Compress the result into bullet points.
Keep only essential facts, findings, and conclusions.
"""

wiki_api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
wiki_tool = WikipediaQueryRun(api_wrapper= wiki_api_wrapper)

llm = ChatGroq(
    model="openai/gpt-oss-safeguard-20b",
    temperature=0,
    max_tokens=None,
    reasoning_format="parsed",
    timeout=None,
    max_retries=2, 
    # other params...
)
teach_tools = [wiki_tool]
teach_llm=llm.bind_tools(teach_tools)

teach_agent = create_agent(
    model=teach_llm,  # or any other supported model identifier string
    tools=teach_tools,
    system_prompt=teaching_agent_prompt
)
