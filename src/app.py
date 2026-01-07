"""
Streamlit chat interface for the Vena RAG Bot.

Run with: streamlit run src/app.py
"""

import streamlit as st
from pathlib import Path

# Add parent directory to path for imports
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.config import settings, validate_settings
from src.retrieval import get_rag_pipeline


# Page configuration
st.set_page_config(
    page_title="Vena RAG Bot",
    page_icon="🤖",
    layout="wide"
)


def initialize_session_state():
    """Initialize session state variables."""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
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


def display_chat_history():
    """Display the chat message history."""
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
            # Show sources for assistant messages
            if message["role"] == "assistant" and "sources" in message:
                with st.expander("📚 Sources"):
                    for source in message["sources"]:
                        st.write(f"• {source}")


def main():
    """Main Streamlit application."""
    
    # Initialize
    initialize_session_state()
    
    # Header
    st.title("🤖 Vena RAG Bot")
    st.caption("AI-powered technical support for the Vena platform")
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Settings")
        
        # Configuration status
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
    
    # Load RAG pipeline
    if not load_rag_pipeline():
        st.warning("Please configure the system and ingest documents first.")
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
                    response, docs = st.session_state.rag_pipeline.query(prompt)
                    sources = st.session_state.rag_pipeline.get_sources(docs)
                    
                    # Display response
                    st.markdown(response)
                    
                    # Show sources
                    with st.expander("📚 Sources"):
                        for source in sources:
                            st.write(f"• {source}")
                    
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



