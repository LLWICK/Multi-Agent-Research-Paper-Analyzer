from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper


Math_agent_prompt = """You are the Mathematical Reasoning Agent. 
Read the given research paper context carefully, extract all the mathematical formulas and explain , analyze equations, Loss functions, 
optimization methods.
Explain what each equation represents, why it needed and assumptions made so even a complete beginner could understand.
present the results in a human-readable format. 
Compress the result into bullet points.
Keep only essential facts, findings, and conclusions.
Use the provided tools ONLY if you need.

"""

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
    max_tokens=None,
    reasoning_format="parsed",
    timeout=None,
    max_retries=2, 
    # other params...
)
wiki_api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
wiki_tool = WikipediaQueryRun(api_wrapper= wiki_api_wrapper)
math_tools = [wiki_tool]
math_llm=llm.bind_tools(math_tools)

math_agent = create_agent(
    model=math_llm,  # or any other supported model identifier string
    tools=math_tools,
    system_prompt=Math_agent_prompt
)

math_agent_input = {"messages": [{"role": "user", "content": "explain all the mathematical terms in this research paper"+ "context - "+str(result_parse_agent["messages"][-1].content)}]}
math_agent_results=math_agent.invoke(math_agent_input)
print(math_agent_results["messages"][-1].content)