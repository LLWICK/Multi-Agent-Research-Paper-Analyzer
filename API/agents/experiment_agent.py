from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun
from langchain_community.utilities import ArxivAPIWrapper
from dotenv import load_dotenv
load_dotenv()

experimental_analysis_agent_prompt = """You are the Experimental Analysis Agent and Empirical reviewer. 
Read the given context carefully and explain / Reviews Datasets used, Experimental setup, Baselines, Evaluation metrics.
Determines whether experiments support claims, If comparisons are fair. Conpare them with other related research papers.
Compress the result into bullet points.
Keep only essential facts, findings, and conclusions.
Use the given tools only if needed. Give me exacly a final answer don't think too much.
"""


arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
arxiv_tool = ArxivQueryRun(api_wrapper= arxiv_wrapper)
wiki_api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
wiki_tool = WikipediaQueryRun(api_wrapper= wiki_api_wrapper)

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
    max_tokens=None,
    reasoning_format="parsed",
    timeout=None,
    max_retries=2, 
    # other params...
)
experimental_analysis_agent_tools = [arxiv_tool,wiki_tool]
experimental_analysis_agent_llm=llm.bind_tools(experimental_analysis_agent_tools)

experimental_analysis_agent = create_agent(
    model=experimental_analysis_agent_llm,  
    tools=experimental_analysis_agent_tools,
    system_prompt=experimental_analysis_agent_prompt
)

