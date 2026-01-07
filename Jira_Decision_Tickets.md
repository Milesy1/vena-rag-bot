# Jira Decision Tickets - Architecture Decisions

Ready-to-use templates for creating Architecture Decision Records (ADRs) in Jira.

---

## ADR-001: ChromaDB for Vector Storage

**Work Type:** Task  
**Summary:**
```
ADR-001: Use ChromaDB for Vector Storage
```

**Description:**
```
**Decision:** Use ChromaDB as the vector database for Phase 1

**Context:** 
Need a vector database for semantic search to enable RAG functionality. 
Evaluated three options: Pinecone, Weaviate, and ChromaDB.

**Options Considered:**

1. **Pinecone:**
   - Pros: Managed service, highly scalable, minimal setup, enterprise-ready
   - Cons: Cost scales with usage ($70+/month), vendor lock-in, requires internet
   - Best for: Production at scale (50+ users)

2. **Weaviate:**
   - Pros: Open source, self-hosted, feature-rich, good scalability
   - Cons: Requires infrastructure management, more complex setup
   - Best for: Organizations with DevOps resources

3. **ChromaDB:**
   - Pros: Free, local storage, zero infrastructure, lightweight, easy setup
   - Cons: Less scalable, fewer enterprise features, local-only
   - Best for: POC and Phase 1 (10 users)

**Decision:**
- **Chosen:** ChromaDB
- **Reason:** 
  - Free for Phase 1 (no budget for managed services yet)
  - Zero infrastructure setup (runs locally)
  - Fast to implement and test
  - Sufficient for Phase 1 scale (10 concurrent users)
- **Date:** December 24, 2024
- **Decided by:** Miles Waite

**Consequences:**
- ✅ No infrastructure setup needed
- ✅ Free for Phase 1
- ✅ Fast implementation (already working in POC)
- ✅ Data stored locally (privacy/security benefit)
- ⚠️ May need migration to Pinecone for Phase 2 (50+ users)
- ⚠️ Less scalable than managed solutions
- ⚠️ No built-in backup/replication (manual backup required)

**Migration Path:**
- Phase 2: Evaluate Pinecone if user count exceeds 25
- Migration strategy: Export embeddings from ChromaDB, import to Pinecone

**Status:** Accepted  
**Related Epic:** FRBP-1 (Core RAG System)
```

**Labels:**
- `architecture-decision`
- `decision-record`
- `adr`
- `data-storage`

**Parent:** FRBP-1 (Core RAG System Epic)

---

## ADR-002: OpenAI GPT-4o for LLM

**Work Type:** Task  
**Summary:**
```
ADR-002: Use OpenAI GPT-4o for LLM
```

**Description:**
```
**Decision:** Use OpenAI GPT-4o as the Large Language Model for response generation

**Context:**
Need an LLM to synthesize retrieved context into coherent, cited responses.
Evaluated OpenAI GPT-4o, Anthropic Claude, and open-source alternatives.

**Options Considered:**

1. **OpenAI GPT-4o:**
   - Pros: Proven performance, extensive ecosystem, excellent code generation, good documentation
   - Cons: Higher cost ($5-15/1M tokens), potential latency, vendor lock-in
   - Cost: ~$0.005 per query (estimated)
   - Best for: Production-ready applications

2. **Anthropic Claude 3.5 Sonnet:**
   - Pros: Strong code generation, longer context window (200k tokens), safety features
   - Cons: Smaller ecosystem, similar cost, less proven for RAG
   - Cost: ~$0.003 per query (estimated)
   - Best for: Applications requiring long context

3. **Open Source (Llama 3, Mistral):**
   - Pros: Cost-effective, full control, no vendor dependency, no data leaving premises
   - Cons: Requires infrastructure, more setup complexity, potentially lower quality
   - Cost: Infrastructure only (~$50-200/month for GPU)
   - Best for: Organizations with strict data privacy requirements

**Decision:**
- **Chosen:** OpenAI GPT-4o
- **Reason:**
  - Best balance of quality, speed, and cost for Phase 1
  - Proven performance in RAG applications
  - Excellent code generation capabilities (needed for Epic 2)
  - Easy API integration (already working in POC)
  - Estimated Phase 1 cost: $5-20/month (acceptable)
- **Date:** December 24, 2024
- **Decided by:** Miles Waite

**Consequences:**
- ✅ High-quality responses
- ✅ Fast response times (~2-3 seconds)
- ✅ Excellent code generation
- ✅ Easy integration
- ⚠️ Ongoing API costs (monitor usage)
- ⚠️ Vendor dependency
- ⚠️ Data sent to OpenAI (review data privacy policy)

**Cost Management:**
- Implement response caching for common queries
- Monitor token usage in real-time
- Set rate limits per user if needed
- Optimize prompts for token efficiency

**Future Considerations:**
- Phase 2: Evaluate Claude if cost becomes issue
- Future: Consider open-source if data privacy becomes critical

**Status:** Accepted  
**Related Epic:** FRBP-1 (Core RAG System), FRBP-2 (Code Capabilities)
```

**Labels:**
- `architecture-decision`
- `decision-record`
- `adr`
- `llm`

**Parent:** FRBP-1 (Core RAG System Epic)

---

## ADR-003: Streamlit for User Interface

**Work Type:** Task  
**Summary:**
```
ADR-003: Use Streamlit for User Interface
```

**Description:**
```
**Decision:** Use Streamlit for the web-based chat interface in Phase 1

**Context:**
Need a web interface for users to interact with the RAG system.
Evaluated Streamlit, React + FastAPI, and pure FastAPI with templates.

**Options Considered:**

1. **Streamlit:**
   - Pros: Rapid development, Python-native, built-in chat components, no frontend expertise needed
   - Cons: Less customizable, performance limitations at scale, not ideal for complex UIs
   - Development time: 1-2 days
   - Best for: POC and Phase 1 MVP

2. **React + FastAPI:**
   - Pros: Highly customizable, professional UI, scalable, industry standard
   - Cons: Requires frontend expertise, longer development time, more complex
   - Development time: 1-2 weeks
   - Best for: Production applications

3. **FastAPI with Jinja2 Templates:**
   - Pros: Server-side rendering, simple, Python-only
   - Cons: Less interactive, outdated UX patterns
   - Development time: 3-5 days
   - Best for: Simple internal tools

**Decision:**
- **Chosen:** Streamlit
- **Reason:**
  - Already implemented and working in POC
  - Rapid development (focus on RAG functionality, not UI)
  - Sufficient for Phase 1 requirements (basic chat interface)
  - Python-only stack (no frontend developers needed)
  - Can migrate to React in Phase 2 if needed
- **Date:** December 24, 2024
- **Decided by:** Miles Waite

**Consequences:**
- ✅ Fast to implement (already done in POC)
- ✅ Easy to maintain (Python-only)
- ✅ Good enough for Phase 1 (basic chat works)
- ✅ No frontend expertise required
- ⚠️ Less customizable than React
- ⚠️ Performance limitations at scale (10 users OK, 50+ may struggle)
- ⚠️ May need migration to React for Phase 2

**Migration Path:**
- Phase 2: Evaluate React if UI requirements become complex
- Keep API layer separate for easy frontend swap

**Status:** Accepted  
**Related Epic:** FRBP-3 (User Interface and Experience)
```

**Labels:**
- `architecture-decision`
- `decision-record`
- `adr`
- `ui`

**Parent:** FRBP-3 (User Interface and Experience Epic)

---

## ADR-004: LangChain Framework

**Work Type:** Task  
**Summary:**
```
ADR-004: Use LangChain Framework for RAG Orchestration
```

**Description:**
```
**Decision:** Use LangChain framework for RAG pipeline orchestration

**Context:**
Need a framework to orchestrate document loading, chunking, embedding, 
vector storage, and LLM integration. Evaluated LangChain vs custom implementation.

**Options Considered:**

1. **LangChain:**
   - Pros: Comprehensive framework, handles all RAG components, active community, good documentation
   - Cons: Large dependency, some abstraction overhead, version changes
   - Development time: 2-3 days (already done in POC)
   - Best for: Rapid development, standard RAG patterns

2. **Custom Implementation:**
   - Pros: Full control, lightweight, no external dependencies, optimized for our use case
   - Cons: More development time, maintain all components ourselves, reinventing the wheel
   - Development time: 1-2 weeks
   - Best for: Highly specialized requirements

3. **LlamaIndex:**
   - Pros: RAG-focused, good performance, data connectors
   - Cons: Less flexible, smaller ecosystem, learning curve
   - Development time: 3-5 days
   - Best for: Data-heavy applications

**Decision:**
- **Chosen:** LangChain
- **Reason:**
  - Already implemented and working in POC
  - Handles all RAG components (loaders, splitters, embeddings, vector stores, LLMs)
  - Active community and good documentation
  - Saves development time (focus on business logic, not infrastructure)
  - Easy to swap components (e.g., change vector DB or LLM)
- **Date:** December 24, 2024
- **Decided by:** Miles Waite

**Consequences:**
- ✅ Fast development (already done)
- ✅ Comprehensive features out of the box
- ✅ Easy to maintain and extend
- ✅ Good community support
- ⚠️ Large dependency (many packages)
- ⚠️ Version changes may require updates
- ⚠️ Some abstraction overhead (but acceptable)

**Status:** Accepted  
**Related Epic:** FRBP-1 (Core RAG System)
```

**Labels:**
- `architecture-decision`
- `decision-record`
- `adr`
- `framework`

**Parent:** FRBP-1 (Core RAG System Epic)

---

## ADR-005: Local ChromaDB Storage

**Work Type:** Task  
**Summary:**
```
ADR-005: Use Local ChromaDB Storage (vs Cloud)
```

**Description:**
```
**Decision:** Store ChromaDB vector database locally on server (vs cloud storage)

**Context:**
ChromaDB can store data locally or in cloud (S3, etc.). Need to decide 
storage location for Phase 1.

**Options Considered:**

1. **Local Storage:**
   - Pros: Fast access, no cloud costs, simple setup, data stays on-premises
   - Cons: No automatic backup, single point of failure, manual backup required
   - Best for: Phase 1, single-server deployments

2. **Cloud Storage (S3, etc.):**
   - Pros: Automatic backup, scalable, accessible from multiple servers
   - Cons: Additional cost, network latency, more complex setup
   - Best for: Multi-server deployments, production

3. **Hybrid (Local + Cloud Backup):**
   - Pros: Fast local access + cloud backup
   - Cons: More complex, additional cost
   - Best for: Production with backup requirements

**Decision:**
- **Chosen:** Local Storage
- **Reason:**
  - Simple for Phase 1 (single developer, single server)
  - No additional costs
  - Fast access (no network latency)
  - Data stays on-premises (privacy benefit)
  - Can add cloud backup later if needed
- **Date:** December 24, 2024
- **Decided by:** Miles Waite

**Consequences:**
- ✅ Simple setup (already working)
- ✅ Fast access
- ✅ No cloud storage costs
- ✅ Data privacy (stays local)
- ⚠️ Manual backup required
- ⚠️ Single point of failure (mitigate with regular backups)
- ⚠️ Not suitable for multi-server deployments

**Backup Strategy:**
- Weekly manual backup of `data/chromadb/` folder
- Phase 2: Implement automated backup to cloud storage

**Status:** Accepted  
**Related Epic:** FRBP-1 (Core RAG System), FRBP-5 (Performance and Reliability)
```

**Labels:**
- `architecture-decision`
- `decision-record`
- `adr`
- `storage`

**Parent:** FRBP-1 (Core RAG System Epic)

---

## ADR-006: OpenAI Embeddings Model

**Work Type:** Task  
**Summary:**
```
ADR-006: Use OpenAI text-embedding-3-small for Embeddings
```

**Description:**
```
**Decision:** Use OpenAI text-embedding-3-small for document embeddings

**Context:**
Need embedding model to convert documents and queries to vectors for 
semantic search. Evaluated OpenAI models vs open-source alternatives.

**Options Considered:**

1. **OpenAI text-embedding-3-small:**
   - Pros: High quality, optimized for retrieval, cost-effective ($0.02/1M tokens)
   - Cons: Vendor dependency, requires API calls
   - Cost: ~$0.0001 per document (negligible)
   - Best for: Production applications

2. **OpenAI text-embedding-3-large:**
   - Pros: Higher quality, better for complex queries
   - Cons: 3x more expensive, may be overkill for Phase 1
   - Cost: ~$0.0003 per document
   - Best for: Complex semantic search

3. **Open Source (sentence-transformers):**
   - Pros: Free, runs locally, no API calls
   - Cons: Lower quality, requires GPU for performance, more setup
   - Cost: Infrastructure only
   - Best for: High-volume, cost-sensitive applications

**Decision:**
- **Chosen:** OpenAI text-embedding-3-small
- **Reason:**
  - Already implemented in POC
  - Excellent quality for semantic search
  - Very cost-effective ($0.02/1M tokens)
  - No infrastructure needed
  - Fast (API-based, no local processing)
- **Date:** December 24, 2024
- **Decided by:** Miles Waite

**Consequences:**
- ✅ High-quality embeddings
- ✅ Cost-effective (negligible cost for Phase 1)
- ✅ Fast (no local processing)
- ✅ Easy to use (API-based)
- ⚠️ Vendor dependency
- ⚠️ Requires internet connection

**Status:** Accepted  
**Related Epic:** FRBP-1 (Core RAG System)
```

**Labels:**
- `architecture-decision`
- `decision-record`
- `adr`
- `embeddings`

**Parent:** FRBP-1 (Core RAG System Epic)

---

## Summary

| ADR | Decision | Status | Related Epic |
|-----|----------|--------|--------------|
| ADR-001 | ChromaDB for Vector Storage | Accepted | FRBP-1 |
| ADR-002 | OpenAI GPT-4o for LLM | Accepted | FRBP-1, FRBP-2 |
| ADR-003 | Streamlit for UI | Accepted | FRBP-3 |
| ADR-004 | LangChain Framework | Accepted | FRBP-1 |
| ADR-005 | Local ChromaDB Storage | Accepted | FRBP-1, FRBP-5 |
| ADR-006 | OpenAI text-embedding-3-small | Accepted | FRBP-1 |

---

## How to Use

1. **Create a Task** in Jira for each ADR
2. **Copy the Summary** as the ticket title
3. **Copy the Description** into the ticket description
4. **Add Labels** (architecture-decision, decision-record, adr)
5. **Link to Parent Epic** (set Parent field)
6. **Set Priority** to Medium
7. **Set Status** to Done (since decisions are already made)

---

*Document created: December 24, 2024*

