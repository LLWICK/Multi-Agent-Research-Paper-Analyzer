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
from services.vectore_store import create_or_load_vectorstore, get_vectorstore
from langchain_ollama import ChatOllama
from services.Structured_output import PaperOutput

from tools.MultiStep_Reasoning import multi_step_retrieval
load_dotenv()

#Agent pre setup

def praser_Agent(pdf_path):

    vectorstore = get_vectorstore(pdf_path)
    retriever_tool = build_retriever_tool(vectorstore)
    

    context = multi_step_retrieval(retriever_tool)

  

    llm = ChatOllama(
        model="llama3.2",
        temperature=0,
        max_tokens=None,
        reasoning_format="parsed",
        timeout=None,
        max_retries=2, 
        # other params...
    )

    #parse_llm_with_tools = llm.bind_tools(parse_agent_Tools)
    
    

    parse_agent_prompt = f"""
    You are a Research Paper Parsing Agent.

    Extract structured information from the context below.
    Research Paper Name:
    {context['Name']}

    Abstract Context:
    {context['Abstract']}

    Method Context:
    {context['Method']}

    Math Context:
    {context['Math']}

    Experiments Context:
    {context['Experiments']}

    Results Context:
    {context['Results']}

    Instructions:
    - Clean and explain the content
    - Remove noise or broken symbols
    - Be descriptive. Give the sufficient amount of Information to work on.
    - Do NOT hallucinate

    Return ONLY JSON:

    {{
    "Paper_Name":"..."
    "Abstract": "...",
    "Method": "...",
    "Math": "...",
    "Experiments": "...",
    "Results": "...",
    "Youtube": "Generate a YouTube search query for this paper"
    }}
    """;

    parse_agent = create_agent(
        model=llm,  # or any other supported model identifier string
        #tools=parse_agent_tools,
        #response_format=PaperOutput,
        system_prompt=parse_agent_prompt
    )


    inputs = {"messages": [{"role": "user", "content": "Analyze the given research paper"}]}
    result_parse_agent=parse_agent.invoke(inputs)
    raw_text =  result_parse_agent["messages"][-1].content
  
    structured_llm = llm.with_structured_output(PaperOutput)
    final_output = structured_llm.invoke(raw_text)

    return final_output;
    




