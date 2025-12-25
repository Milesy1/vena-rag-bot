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
    
    if "vector_store" not in st.session_state:
        st.session_state.vector_store = None
    
    if "kb_loaded" not in st.session_state:
        st.session_state.kb_loaded = False


def build_knowledge_base():
    """Build the knowledge base in memory."""
    from src.ingestion import ingest_knowledge_base
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
    
    # Extract sources
    sources = list(set([Path(doc.metadata.get("source", "unknown")).stem for doc in docs]))
    
    return response.content, sources


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


def get_api_key():
    """Get API key from settings or Streamlit secrets."""
    # Check Streamlit secrets first (for Cloud deployment)
    if 'OPENAI_API_KEY' in st.secrets:
        return st.secrets['OPENAI_API_KEY']
    # Fall back to settings (local .env)
    if settings.openai_api_key and settings.openai_api_key != "sk-your-api-key-here":
        return settings.openai_api_key
    return None


def main():
    """Main Streamlit application."""
    
    # Initialize
    initialize_session_state()
    
    # Get API key (check secrets first for Cloud deployment)
    api_key = get_api_key()
    if api_key:
        settings.openai_api_key = api_key
    
    # Header
    st.title("🤖 Vena RAG Bot")
    st.caption("AI-powered technical support for the Vena platform")
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Settings")
        
        # Configuration status
        if api_key:
            st.success("✅ API Key configured")
        else:
            st.error("❌ API Key not configured")
            st.info("Add OPENAI_API_KEY to Streamlit secrets or .env file")
            return
        
        # Knowledge base status
        if st.session_state.kb_loaded:
            st.success("✅ Knowledge base loaded")
            # Add rebuild option
            if st.button("🔄 Rebuild Knowledge Base"):
                with st.spinner("Rebuilding... (this may take a minute)"):
                    try:
                        build_knowledge_base()
                        st.success("✅ Knowledge base rebuilt!")
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
    
    # Check if knowledge base is loaded
    if not st.session_state.kb_loaded:
        st.info("👆 Click **'Build Knowledge Base'** in the sidebar to get started!")
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
                    response, sources = query_knowledge_base(prompt, api_key)
                    
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

