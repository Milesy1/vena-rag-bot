"""
<<<<<<< HEAD
Streamlit chat interface for the Vena RAG Bot.
=======
Streamlit chat interface for the FCS RAG Bot.
>>>>>>> 8d6f9d581e1a19332070f83b53fbf922e1fb730c

Run with: streamlit run src/app.py
"""

import streamlit as st
from pathlib import Path

# Add parent directory to path for imports
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.config import settings, validate_settings
<<<<<<< HEAD
from src.retrieval import get_rag_pipeline
=======
>>>>>>> 8d6f9d581e1a19332070f83b53fbf922e1fb730c


# Page configuration
st.set_page_config(
<<<<<<< HEAD
    page_title="Vena RAG Bot",
=======
    page_title="FCS RAG Bot",
>>>>>>> 8d6f9d581e1a19332070f83b53fbf922e1fb730c
    page_icon="🤖",
    layout="wide"
)


def initialize_session_state():
    """Initialize session state variables."""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
<<<<<<< HEAD
    if "rag_pipeline" not in st.session_state:
        st.session_state.rag_pipeline = None


def load_rag_pipeline():
    """Load the RAG pipeline."""
    if st.session_state.rag_pipeline is None:
        try:
            st.session_state.rag_pipeline = get_rag_pipeline()
            return True
        except Exception as e:
            st.error(f"Failed to load RAG pipeline: {e}")
            return False
    return True
=======
    if "vector_store" not in st.session_state:
        st.session_state.vector_store = None
    
    if "kb_loaded" not in st.session_state:
        st.session_state.kb_loaded = False


def build_knowledge_base():
    """Build the knowledge base in memory."""
    from src.ingestion import ingest_knowledge_base, load_documents
    from src.config import settings
    from pathlib import Path
    
    # First show what documents we find
    docs = load_documents(settings.knowledge_base_dir)
    st.session_state.doc_count = len(docs)
    
    # Debug: Count by folder
    comparisons = [d for d in docs if 'Comparisons' in str(d.metadata.get('source', ''))]
    st.session_state.comparison_count = len(comparisons)
    
    vector_store = ingest_knowledge_base(in_memory=True)
    st.session_state.vector_store = vector_store
    st.session_state.kb_loaded = True
    return vector_store


def query_knowledge_base(question: str, api_key: str):
    """Query the knowledge base."""
    from langchain_openai import ChatOpenAI
    from langchain_core.prompts import ChatPromptTemplate
    
    if st.session_state.vector_store is None:
        raise ValueError("Knowledge base not loaded!")
    
    # Retrieve relevant documents
    docs = st.session_state.vector_store.similarity_search(question, k=5)
    
    # Format context
    context_parts = []
    for i, doc in enumerate(docs, 1):
        source = Path(doc.metadata.get("source", "unknown")).stem
        content = doc.page_content.strip()
        context_parts.append(f"[Document {i}: {source}]\n{content}\n")
    context = "\n---\n".join(context_parts)
    
    # Create prompt
    system_prompt = """You are a knowledgeable technical assistant specializing in the Vena financial consolidation platform. Your role is to help contractors and developers understand Vena concepts, write VenaQL code, and troubleshoot issues.

IMPORTANT GUIDELINES:
1. Base your answers ONLY on the provided context documents
2. Always cite your sources using [Source: document_name] format
3. If the context doesn't contain enough information, say so clearly
4. Be concise but thorough

CONTEXT DOCUMENTS:
{context}

Remember: Only use information from the context above. Cite your sources."""

    # Generate response
    llm = ChatOpenAI(
        model=settings.openai_model,
        temperature=settings.temperature,
        max_tokens=settings.max_tokens,
        openai_api_key=api_key
    )
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{question}")
    ])
    
    messages = prompt.format_messages(context=context, question=question)
    response = llm.invoke(messages)
    
    # Extract sources with content
    sources = []
    seen = set()
    for doc in docs:
        source_name = Path(doc.metadata.get("source", "unknown")).stem
        if source_name not in seen:
            seen.add(source_name)
            sources.append({
                "name": source_name,
                "content": doc.page_content[:500] + "..." if len(doc.page_content) > 500 else doc.page_content
            })
    
    return response.content, sources
>>>>>>> 8d6f9d581e1a19332070f83b53fbf922e1fb730c


def display_chat_history():
    """Display the chat message history."""
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
            # Show sources for assistant messages
            if message["role"] == "assistant" and "sources" in message:
<<<<<<< HEAD
                with st.expander("📚 Sources"):
                    for source in message["sources"]:
                        st.write(f"• {source}")
=======
                with st.expander("📚 View Sources"):
                    for source in message["sources"]:
                        if isinstance(source, dict):
                            st.markdown(f"**{source['name']}**")
                            st.markdown(f"```\n{source['content']}\n```")
                            st.divider()
                        else:
                            st.write(f"• {source}")


def get_api_key():
    """Get API key from settings or Streamlit secrets."""
    # Check Streamlit secrets first (for Cloud deployment)
    if 'OPENAI_API_KEY' in st.secrets:
        return st.secrets['OPENAI_API_KEY']
    # Fall back to settings (local .env)
    if settings.openai_api_key and settings.openai_api_key != "sk-your-api-key-here":
        return settings.openai_api_key
    return None
>>>>>>> 8d6f9d581e1a19332070f83b53fbf922e1fb730c


def main():
    """Main Streamlit application."""
    
    # Initialize
    initialize_session_state()
    
<<<<<<< HEAD
    # Header
    st.title("🤖 Vena RAG Bot")
=======
    # Get API key (check secrets first for Cloud deployment)
    api_key = get_api_key()
    if api_key:
        settings.openai_api_key = api_key
    
    # Header
    st.title("🤖 FCS RAG Bot")
>>>>>>> 8d6f9d581e1a19332070f83b53fbf922e1fb730c
    st.caption("AI-powered technical support for the Vena platform")
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Settings")
        
        # Configuration status
<<<<<<< HEAD
        if settings.openai_api_key and settings.openai_api_key != "sk-your-api-key-here":
            st.success("✅ API Key configured")
        else:
            st.error("❌ API Key not configured")
            st.info("Copy env.example to .env and add your OpenAI API key")
            return
        
        # Vector store status
        if settings.chroma_persist_dir.exists():
            st.success("✅ Knowledge base loaded")
        else:
            st.warning("⚠️ Knowledge base not found")
            st.info("Run: python -m src.ingestion")
=======
        if api_key:
            st.success("✅ API Key configured")
        else:
            st.error("❌ API Key not configured")
            st.info("Add OPENAI_API_KEY to Streamlit secrets or .env file")
            return
        
        # Knowledge base status
        if st.session_state.kb_loaded:
            doc_count = st.session_state.get('doc_count', '?')
            comparison_count = st.session_state.get('comparison_count', 0)
            st.success(f"✅ Knowledge base loaded ({doc_count} docs)")
            if comparison_count > 0:
                st.info(f"📊 Including {comparison_count} comparison documents")
            # Add rebuild option
            if st.button("🔄 Rebuild Knowledge Base"):
                with st.spinner("Rebuilding... (this may take a minute)"):
                    try:
                        build_knowledge_base()
                        st.success(f"✅ Rebuilt with {st.session_state.get('doc_count', '?')} docs!")
                        st.rerun()
                    except Exception as e:
                        st.error(f"Rebuild failed: {e}")
        else:
            st.warning("⚠️ Knowledge base not built yet")
            if st.button("📥 Build Knowledge Base"):
                with st.spinner("Building knowledge base... (this may take a minute)"):
                    try:
                        build_knowledge_base()
                        st.success("✅ Knowledge base built!")
                        st.rerun()
                    except Exception as e:
                        st.error(f"Build failed: {e}")
>>>>>>> 8d6f9d581e1a19332070f83b53fbf922e1fb730c
        
        st.divider()
        
        # Model info
        st.subheader("Model")
        st.write(f"LLM: {settings.openai_model}")
        st.write(f"Embeddings: {settings.embedding_model}")
        
        st.divider()
        
        # Clear chat button
        if st.button("🗑️ Clear Chat"):
            st.session_state.messages = []
            st.rerun()
    
<<<<<<< HEAD
    # Load RAG pipeline
    if not load_rag_pipeline():
        st.warning("Please configure the system and ingest documents first.")
=======
    # Check if knowledge base is loaded
    if not st.session_state.kb_loaded:
        st.info("👆 Click **'Build Knowledge Base'** in the sidebar to get started!")
>>>>>>> 8d6f9d581e1a19332070f83b53fbf922e1fb730c
        return
    
    # Display chat history
    display_chat_history()
    
    # Chat input
    if prompt := st.chat_input("Ask a question about Vena..."):
        # Add user message
        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
<<<<<<< HEAD
                    response, docs = st.session_state.rag_pipeline.query(prompt)
                    sources = st.session_state.rag_pipeline.get_sources(docs)
=======
                    response, sources = query_knowledge_base(prompt, api_key)
>>>>>>> 8d6f9d581e1a19332070f83b53fbf922e1fb730c
                    
                    # Display response
                    st.markdown(response)
                    
<<<<<<< HEAD
                    # Show sources
                    with st.expander("📚 Sources"):
                        for source in sources:
                            st.write(f"• {source}")
=======
                    # Show sources with content
                    with st.expander("📚 View Sources"):
                        for source in sources:
                            st.markdown(f"**{source['name']}**")
                            st.markdown(f"```\n{source['content']}\n```")
                            st.divider()
>>>>>>> 8d6f9d581e1a19332070f83b53fbf922e1fb730c
                    
                    # Save to history
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": response,
                        "sources": sources
                    })
                    
                except Exception as e:
                    error_msg = f"Sorry, I encountered an error: {str(e)}"
                    st.error(error_msg)
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": error_msg
                    })


if __name__ == "__main__":
    main()

<<<<<<< HEAD


=======
>>>>>>> 8d6f9d581e1a19332070f83b53fbf922e1fb730c
