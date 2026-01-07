"""
Document ingestion pipeline for the Vena RAG Bot.

Loads documents from knowledge_base/, chunks them, generates embeddings,
and stores them in ChromaDB for semantic search.
"""

import os
from pathlib import Path
from typing import List

from langchain_community.document_loaders import DirectoryLoader, TextLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

from src.config import settings, validate_settings


def load_documents(knowledge_base_path: Path) -> List:
    """Load all markdown, text, and PDF documents from knowledge base."""
    
    print(f"📂 Loading documents from: {knowledge_base_path}")
    
    documents = []
    
    try:
        # Load markdown files
        md_loader = DirectoryLoader(
            str(knowledge_base_path),
            glob="**/*.md",
            loader_cls=TextLoader,
            loader_kwargs={"encoding": "utf-8"}
        )
        documents.extend(md_loader.load())
        
        # Load text files
        txt_loader = DirectoryLoader(
            str(knowledge_base_path),
            glob="**/*.txt",
            loader_cls=TextLoader,
            loader_kwargs={"encoding": "utf-8"}
        )
        documents.extend(txt_loader.load())
        
        # Load PDF files
        pdf_loader = DirectoryLoader(
            str(knowledge_base_path),
            glob="**/*.pdf",
            loader_cls=PyPDFLoader
        )
        documents.extend(pdf_loader.load())
        
        print(f"   Found {len(documents)} documents")
        
    except Exception as e:
        print(f"   ⚠️  Error loading some documents: {e}")
        print(f"   Continuing with {len(documents)} documents loaded so far...")
    
    return documents


def chunk_documents(documents: List) -> List:
    """Split documents into smaller chunks for embedding."""
    
    print(f"✂️  Chunking documents...")
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.chunk_size,
        chunk_overlap=settings.chunk_overlap,
        length_function=len,
        separators=["\n\n", "\n", " ", ""]
    )
    
    chunks = text_splitter.split_documents(documents)
    print(f"   Created {len(chunks)} chunks")
    return chunks


def create_vector_store(chunks: List) -> Chroma:
    """Create ChromaDB vector store from document chunks."""
    
    print(f"🔢 Generating embeddings and storing in ChromaDB...")
    
    # Ensure directory exists
    settings.chroma_persist_dir.mkdir(parents=True, exist_ok=True)
    
    # Initialize embeddings
    embeddings = OpenAIEmbeddings(
        model=settings.embedding_model,
        openai_api_key=settings.openai_api_key
    )
    
    # Create vector store
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(settings.chroma_persist_dir)
    )
    
    print(f"   ✅ Vector store created at: {settings.chroma_persist_dir}")
    return vector_store


def ingest_knowledge_base() -> Chroma:
    """Main ingestion pipeline: Load → Chunk → Embed → Store."""
    
    print("\n" + "="*50)
    print("🚀 Vena RAG Bot - Knowledge Base Ingestion")
    print("="*50 + "\n")
    
    # Validate configuration
    if not validate_settings():
        raise ValueError("Configuration validation failed!")
    
    # Check knowledge base exists
    if not settings.knowledge_base_dir.exists():
        print(f"❌ Knowledge base directory not found: {settings.knowledge_base_dir}")
        print("   Creating empty directory structure...")
        settings.knowledge_base_dir.mkdir(parents=True, exist_ok=True)
        raise FileNotFoundError("Add documents to knowledge_base/ folder first!")
    
    # Load documents
    documents = load_documents(settings.knowledge_base_dir)
    
    if len(documents) == 0:
        print("❌ No documents found in knowledge base!")
        print("   Add .md, .txt, or .pdf files to knowledge_base/ folder")
        raise FileNotFoundError("No documents to ingest!")
    
    # Chunk documents
    chunks = chunk_documents(documents)
    
    # Create vector store
    vector_store = create_vector_store(chunks)
    
    print("\n" + "="*50)
    print("✅ Ingestion complete!")
    print(f"   Documents: {len(documents)}")
    print(f"   Chunks: {len(chunks)}")
    print("="*50 + "\n")
    
    return vector_store


if __name__ == "__main__":
    ingest_knowledge_base()



