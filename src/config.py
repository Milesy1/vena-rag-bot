"""
Configuration settings for the Vena RAG Bot POC.
"""

import os
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import field_validator, computed_field


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )
    
    # OpenAI Configuration
    openai_api_key: str = ""
    openai_model: str = "gpt-4o"
    embedding_model: str = "text-embedding-3-small"
    
    # RAG Configuration
    chunk_size: int = 500  # tokens per chunk
    chunk_overlap: int = 50  # overlap between chunks
    top_k_results: int = 5  # number of documents to retrieve
    
    # Model Configuration
    max_tokens: int = 2000  # max response tokens
    temperature: float = 0.1  # low temperature for factual responses
    
    @computed_field
    @property
    def project_root(self) -> Path:
        """Get project root directory."""
        # Get the directory containing this config file
        config_file = Path(__file__)
        return config_file.parent.parent
    
    @computed_field
    @property
    def knowledge_base_dir(self) -> Path:
        """Get knowledge base directory."""
        return self.project_root / "knowledge_base"
    
    @computed_field
    @property
    def chroma_persist_dir(self) -> Path:
        """Get ChromaDB persistence directory."""
        return self.project_root / "data" / "chromadb"


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



