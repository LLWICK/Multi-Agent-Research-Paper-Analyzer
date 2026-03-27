# Vector Data impimentation
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain_core.tools import tool
embeddings = OllamaEmbeddings(model="nomic-embed-text")


def retriever_tool(path, query):
    #Doc indexing
    print("document indexing.....")
    loader = PyPDFLoader(path)
    document = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap=50)
    documents =  text_splitter.split_documents(document)
    vectors = FAISS.from_documents(documents, embeddings)
    retriver1 = vectors.as_retriever()

    print("Retriever as a tool.....")
    
    @tool
    def database_search(query: str) -> str:
        """Search for information about the research paper.
        You should use this tool to get the information about the relevant research paper."""
        docs = retriver1.invoke(query)
        return "\n\n".join([doc.page_content for doc in docs])
    
    return database_search.invoke({"query": query})



#result = retriever_tool("C:/Users/CHAMA COMPUTERS/Desktop/Data_Science/AI_ML/projects/Multi_Agent_Research_Paper_Analyzer/Multi-Agent-Research-Paper-Analyzer/test_documents/ALBERT.pdf", "ALBERT Architecture")
#print(result)