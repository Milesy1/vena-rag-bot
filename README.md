# FCS RAG Bot - Proof of Concept

AI-powered technical support assistant for Vena platform using Retrieval Augmented Generation (RAG).

## 🎯 Objective

Prove that a RAG system can accurately retrieve and synthesize answers to complex Vena technical questions from a curated knowledge base.

## 📁 Project Structure

```
RAG Bot POC/
├── src/                    # Source code
│   ├── config.py          # Configuration settings
│   ├── ingestion.py       # Document ingestion pipeline
│   ├── retrieval.py       # RAG query pipeline
│   └── app.py             # Streamlit chat interface
│
├── knowledge_base/         # Vena documentation
│   ├── issue_resolutions/ # Historical problems + solutions
│   ├── patterns/          # VenaQL code patterns
│   ├── concepts/          # Concept explainers
│   └── troubleshooting/   # Debugging guides
│
├── data/                   # ChromaDB vector storage
├── requirements.txt        # Python dependencies
└── .env                    # API keys (not in git)
```

## 🚀 Quick Start

### 1. Set up Python environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# or: source venv/bin/activate  # Mac/Linux

pip install -r requirements.txt
```

### 2. Configure API key

```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

### 3. Ingest knowledge base

```bash
python -m src.ingestion
```

### 4. Run the chat interface

```bash
streamlit run src/app.py
```

## 📊 Success Criteria

| Metric | Target |
|--------|--------|
| Retrieval Relevance | ≥80% |
| Answer Accuracy | ≥70% |
| Response Time | <5 seconds |

## 🛠️ Tech Stack

- **LLM**: OpenAI GPT-4o
- **Embeddings**: OpenAI text-embedding-3-small
- **Vector DB**: ChromaDB
- **Backend**: Python + FastAPI
- **Frontend**: Streamlit

## 📅 Timeline

2-3 week POC starting December 24, 2024

## 👥 Team

- **Developer**: Miles Waite
- **Stakeholder**: Martin Bruwer

---

*Part of the Vena RAG-Based Technical Support System initiative*

