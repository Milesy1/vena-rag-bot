"""
Configuration settings for the FCS RAG Bot POC.
"""

import os
from pathlib import Path
from pydantic_settings import BaseSettings


def get_openai_key() -> str:
    """Get OpenAI API key from environment, .env, or Streamlit secrets."""
    # Try environment variable first
    key = os.getenv("OPENAI_API_KEY", "")
    if key and key != "sk-your-api-key-here":
        return key
    
    # Try Streamlit secrets (for Streamlit Cloud)
    try:
        import streamlit as st
        if hasattr(st, 'secrets') and 'OPENAI_API_KEY' in st.secrets:
            return st.secrets['OPENAI_API_KEY']
    except:
        pass
    
    return ""


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # OpenAI Configuration
    openai_api_key: str = ""
    openai_model: str = "gpt-4o"
    embedding_model: str = "text-embedding-3-small"
    
    # Paths
    project_root: Path = Path(__file__).parent.parent
    # Allow knowledge base path to be set via environment variable (e.g., for Dropbox)
    knowledge_base_dir: Path = Path(os.getenv("KNOWLEDGE_BASE_DIR", str(project_root / "knowledge_base")))
    chroma_persist_dir: Path = project_root / "data" / "chromadb"
    
    # RAG Configuration
    chunk_size: int = 500  # tokens per chunk
    chunk_overlap: int = 50  # overlap between chunks
    top_k_results: int = 5  # number of documents to retrieve
    
    # Model Configuration
    max_tokens: int = 2000  # max response tokens
    temperature: float = 0.1  # low temperature for factual responses
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Override with Streamlit secrets if available
        if not self.openai_api_key or self.openai_api_key == "sk-your-api-key-here":
            self.openai_api_key = get_openai_key()


# Global settings instance
settings = Settings()


def validate_settings() -> bool:
    """Validate that required settings are configured."""
    if not settings.openai_api_key or settings.openai_api_key == "sk-your-api-key-here":
        print("[ERROR] OPENAI_API_KEY not configured!")
        print("   1. Copy env.example to .env")
        print("   2. Add your OpenAI API key")
        return False
    
    print("[OK] Configuration validated successfully!")
    print(f"   Model: {settings.openai_model}")
    print(f"   Embeddings: {settings.embedding_model}")
    print(f"   Knowledge Base: {settings.knowledge_base_dir}")
    return True


if __name__ == "__main__":
    validate_settings()

