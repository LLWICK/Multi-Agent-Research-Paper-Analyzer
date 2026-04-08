import os
import hashlib
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(model="nomic-embed-text")

VECTOR_CACHE = {}

def get_file_hash(pdf_path):
    with open(pdf_path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

def get_db_path(pdf_path):
    file_hash = get_file_hash(pdf_path)
    return f"faiss_vector_files/faiss_index_{file_hash}"

def create_or_load_vectorstore(pdf_path: str):
    db_path = get_db_path(pdf_path)

    if os.path.exists(db_path):
        vectors = FAISS.load_local(db_path, embeddings, allow_dangerous_deserialization=True)
    else:
        loader = PyPDFLoader(pdf_path)
        document = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100
        )

        docs = splitter.split_documents(document)
        vectors = FAISS.from_documents(docs, embeddings)
        vectors.save_local(db_path)

    return vectors

def get_vectorstore(pdf_path):
    key = get_file_hash(pdf_path)

    if key not in VECTOR_CACHE:
        VECTOR_CACHE[key] = create_or_load_vectorstore(pdf_path)

    return VECTOR_CACHE[key]