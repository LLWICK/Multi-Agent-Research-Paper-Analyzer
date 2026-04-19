# 📄 Multi-Agent Research Paper Analyzer (RAG System)

An end-to-end AI system that analyzes research papers and extracts structured insights using a **multi-agent Retrieval-Augmented Generation (RAG) architecture**.

---

## 🚀 Overview

This project is a production-style AI pipeline that processes research papers (PDFs) and generates structured outputs such as:

* Abstract summary
* Methodology explanation
* Mathematical concepts
* Experiments & datasets
* Results & evaluation

The system combines **vector search, LLM reasoning, and multi-agent orchestration** to handle large documents efficiently.

---

## 🧠 Architecture

The system follows a **multi-agent pipeline design**:

```
User Upload (Streamlit UI)
        ↓
FastAPI Backend
        ↓
Parser Agent
        ↓
Context Splitter
        ↓
Multi-Agent Pipeline
   ├── Retrieval Agent (FAISS)
   ├── Summarization Agent
   ├── Parsing Agent (Structured Output)
   ├── teach Agent
   ├── Math Agent
   ├── Experiment Analysis Agent
        ↓
Final Structured JSON Response
```

---

## ⚙️ Tech Stack

* **Backend:** FastAPI
* **Frontend:** Streamlit
* **LLM Inference:** Groq
* **Framework:** LangChain
* **Vector Database:** FAISS
* **Embeddings:** Ollama (nomic-embed-text)
* **Language:** Python

---

## 🔑 Key Features

* 🧩 **Multi-Agent Architecture**
  Separate agents for retrieval, summarization, and parsing.

* 📚 **RAG Pipeline**
  Efficient document understanding using vector search + LLMs.

* ⚡ **Token Optimization**
  Chunking + summarization to handle large PDFs within model limits.

* 🔍 **Semantic Search**
  FAISS-based retrieval for relevant document sections.

* 🧾 **Structured Output**
  Returns clean JSON for downstream applications.

* 🌐 **Full-Stack Integration**
  FastAPI backend + Streamlit frontend.



---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/research-paper-analyzer.git
cd research-paper-analyzer
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup environment variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Running the Application

### Start FastAPI backend

```bash
uvicorn main:app --reload
```

API will run at:

```
http://127.0.0.1:8000
```

---

### Start Streamlit frontend

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```
project/
│
├── api/
│   └── routes/
│
├── agents/
│   ├── parser_agent.py
│   ├── retrieval_agent.py
│   ├── summarizer_agent.py
│
├── services/
│   ├── vector_store.py
│   ├── context_manager.py
│   ├── agent_pipeline.py
│
├── data/
│   ├── uploads/
│   └── faiss_index/
│
├── app.py            # Streamlit frontend
├── main.py           # FastAPI app
└── README.md
```

---

## 🧪 Example Output

```json
{
  "Abstract": "...",
  "Method": "...",
  "Math": "...",
  "Experiments": "...",
  "Results": "...",
  "Youtube": "search query..."
}
```

---

## ⚡ Challenges & Learnings

* Handling **token limits in LLM APIs**
* Designing **efficient retrieval pipelines**
* Managing **multi-agent orchestration**
* Optimizing **performance vs accuracy trade-offs**

---

## 🚀 Future Improvements

* Add **real-time streaming responses**
* Implement **citation tracking**
* Integrate **Redis caching**
* Deploy on **AWS / Docker**
* Add **evaluation agent for hallucination detection**

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork and improve the project.

---

## 📬 Contact

If you’d like to collaborate or discuss AI systems, feel free to connect!

---
