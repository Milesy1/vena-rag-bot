"""
RAG retrieval and response generation pipeline.

Handles semantic search in ChromaDB and response synthesis using GPT-4.
"""

from typing import List, Dict, Tuple
from pathlib import Path

from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain.schema import Document

from src.config import settings


# System prompt for the RAG assistant
SYSTEM_PROMPT = """You are a knowledgeable technical assistant specializing in the Vena financial consolidation platform. Your role is to help contractors and developers understand Vena concepts, write VenaQL code, and troubleshoot issues.

IMPORTANT GUIDELINES:
1. Base your answers ONLY on the provided context documents
2. Always cite your sources using [Source: document_name] format
3. If the context doesn't contain enough information, say so clearly
4. For code examples, ensure they follow Vena constraints (no aliasing, explicit columns, 8192 char limit)
5. Be concise but thorough
6. If asked about something outside Vena, politely redirect to Vena topics

CONTEXT DOCUMENTS:
{context}

Remember: Only use information from the context above. Cite your sources."""


USER_PROMPT = """Question: {question}

Please provide a helpful answer based on the context documents provided. Include source citations."""


class RAGPipeline:
    """Retrieval Augmented Generation pipeline for Vena support."""
    
    def __init__(self):
        """Initialize the RAG pipeline."""
        self.embeddings = OpenAIEmbeddings(
            model=settings.embedding_model,
            openai_api_key=settings.openai_api_key
        )
        
        self.llm = ChatOpenAI(
            model=settings.openai_model,
            temperature=settings.temperature,
            max_tokens=settings.max_tokens,
            openai_api_key=settings.openai_api_key
        )
        
        self.vector_store = None
        self._load_vector_store()
        
        # Create prompt template
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", SYSTEM_PROMPT),
            ("human", USER_PROMPT)
        ])
    
    def _load_vector_store(self):
        """Load existing ChromaDB vector store."""
        if settings.chroma_persist_dir.exists():
            self.vector_store = Chroma(
                persist_directory=str(settings.chroma_persist_dir),
                embedding_function=self.embeddings
            )
            print(f"✅ Loaded vector store from: {settings.chroma_persist_dir}")
        else:
            print("⚠️  No vector store found. Run ingestion first!")
            self.vector_store = None
    
    def retrieve(self, query: str, top_k: int = None) -> List[Document]:
        """Retrieve relevant documents for a query."""
        if self.vector_store is None:
            raise ValueError("Vector store not initialized. Run ingestion first!")
        
        k = top_k or settings.top_k_results
        documents = self.vector_store.similarity_search(query, k=k)
        return documents
    
    def format_context(self, documents: List[Document]) -> str:
        """Format retrieved documents as context for the LLM."""
        context_parts = []
        
        for i, doc in enumerate(documents, 1):
            source = Path(doc.metadata.get("source", "unknown")).stem
            content = doc.page_content.strip()
            context_parts.append(f"[Document {i}: {source}]\n{content}\n")
        
        return "\n---\n".join(context_parts)
    
    def generate_response(self, query: str, documents: List[Document]) -> str:
        """Generate a response using the LLM with retrieved context."""
        context = self.format_context(documents)
        
        # Format the prompt
        messages = self.prompt.format_messages(
            context=context,
            question=query
        )
        
        # Generate response
        response = self.llm.invoke(messages)
        return response.content
    
    def query(self, question: str) -> Tuple[str, List[Document]]:
        """
        Main query method: Retrieve relevant docs and generate response.
        
        Returns:
            Tuple of (response_text, source_documents)
        """
        print(f"\n🔍 Query: {question}")
        
        # Retrieve relevant documents
        documents = self.retrieve(question)
        print(f"   Retrieved {len(documents)} relevant documents")
        
        # Generate response
        response = self.generate_response(question, documents)
        
        return response, documents
    
    def get_sources(self, documents: List[Document]) -> List[str]:
        """Extract source names from documents."""
        sources = []
        for doc in documents:
            source = Path(doc.metadata.get("source", "unknown")).stem
            if source not in sources:
                sources.append(source)
        return sources


# Create singleton instance
_rag_pipeline = None

def get_rag_pipeline() -> RAGPipeline:
    """Get or create the RAG pipeline singleton."""
    global _rag_pipeline
    if _rag_pipeline is None:
        _rag_pipeline = RAGPipeline()
    return _rag_pipeline


if __name__ == "__main__":
    # Test the pipeline
    from src.config import validate_settings
    
    if validate_settings():
        pipeline = get_rag_pipeline()
        
        # Test query
        test_question = "How does FX conversion work in Vena?"
        response, docs = pipeline.query(test_question)
        
        print("\n" + "="*50)
        print("RESPONSE:")
        print("="*50)
        print(response)
        print("\n" + "="*50)
        print("SOURCES:", pipeline.get_sources(docs))
        print("="*50)



