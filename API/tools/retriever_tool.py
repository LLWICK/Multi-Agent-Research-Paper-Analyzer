# Vector Data impimentation
from langchain_ollama import OllamaEmbeddings
from langchain_core.tools import tool
from services.clean_text import clean_text
embeddings = OllamaEmbeddings(model="nomic-embed-text")




def build_retriever_tool(vectorstore):

    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

    @tool
    def database_search(query: str) -> str:
        """
        Search relevant parts of the research paper.
        Always use this tool before answering.
        """
        docs = retriever.invoke(query)
        raw_text = "\n\n".join([doc.page_content for doc in docs])
        cleaned_text = clean_text(raw_text)
        return cleaned_text;

    return database_search;



#result = retriever_tool("C:/Users/CHAMA COMPUTERS/Desktop/Data_Science/AI_ML/projects/Multi_Agent_Research_Paper_Analyzer/Multi-Agent-Research-Paper-Analyzer/test_documents/ALBERT.pdf", "ALBERT Architecture")
#print(result)