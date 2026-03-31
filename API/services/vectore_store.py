# services/vector_store.py

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from dotenv import load_dotenv
load_dotenv()
import os

embeddings = OllamaEmbeddings(model="nomic-embed-text")

DB_PATH = "faiss_index"

def create_or_load_vectorstore(pdf_path: str):
    loader = PyPDFLoader(pdf_path)
    document = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap=200)
    documents =  text_splitter.split_documents(document)
    vectors = FAISS.from_documents(documents, embeddings)

    return vectors