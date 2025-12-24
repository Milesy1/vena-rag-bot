# Vena RAG Bot - Proof of Concept Proposal

**Document Version:** 1.0  
**Date:** December 24, 2024  
**Author:** Miles Waite  
**Status:** Draft - For Review

---

## Executive Summary

This document outlines a **2-3 week Proof of Concept (POC)** to validate the core hypothesis of the Vena RAG-Based Technical Support System before committing to full implementation.

### POC Objective

> **Prove that a RAG (Retrieval Augmented Generation) system can accurately retrieve and synthesize answers to complex Vena technical questions from a curated knowledge base.**

This POC focuses on **retrieval quality validation** — the foundational capability upon which all other features (code generation, issue diagnosis, documentation) depend.

### Key Outcomes

| Outcome | Description |
|---------|-------------|
| **Validated Approach** | Evidence that semantic search can find relevant Vena documentation |
| **Working Prototype** | Functional chat interface for testing queries |
| **Go/No-Go Decision** | Data-driven recommendation for Phase 1 investment |
| **Risk Reduction** | Early identification of technical challenges before full build |

---

## Background & Context

### Problem Statement

Based on the full Business Requirements Document (BRD v1.0), the organisation faces:

- **3-4 week onboarding** for new Vena contractors
- **40-50% of senior resource time** consumed by repetitive technical queries
- **Tribal knowledge** locked in experienced team members
- **No systematic capture** of issue resolutions and patterns

### Proposed Solution (Full Scope)

A RAG-based AI assistant providing:
- Knowledge Q&A with source citations
- VenaQL code generation and explanation
- Issue diagnosis and troubleshooting
- Automated documentation generation

### Why a POC First?

Before investing 4 months and significant resources, we need to validate:

1. **Can the system retrieve relevant information?** — If semantic search doesn't work well for Vena-specific content, the entire approach fails
2. **What quality of knowledge base is required?** — Understanding documentation effort needed
3. **Will the LLM synthesize accurate answers?** — Testing real-world query scenarios

---

## POC Scope

### In Scope ✅

| Component | Description |
|-----------|-------------|
| **Vector Database Setup** | ChromaDB instance for semantic search |
| **Document Ingestion Pipeline** | Load, chunk, and embed knowledge documents |
| **RAG Query Pipeline** | Retrieve relevant context and generate answers |
| **Source Citations** | Responses include references to source documents |
| **Simple Chat Interface** | Basic web UI for testing (Streamlit or HTML) |
| **Seed Knowledge Base** | 10-15 curated documents (issue resolutions, patterns, concepts) |
| **Accuracy Testing** | 10 "difficult" test questions with documented results |

### Out of Scope ❌

| Component | Rationale |
|-----------|-----------|
| VenaQL Code Generation | Higher risk; validate retrieval first |
| Issue Diagnosis | Phase 2 feature |
| Authentication/SSO | Not needed for internal testing |
| Production Infrastructure | POC runs locally |
| Full Knowledge Base (100+ docs) | Start small, prove concept |
| Analytics Dashboard | Manual evaluation sufficient for POC |
| Vena Metadata Integration | Phase 2 feature |

---

## Technical Approach

### Recommended Technology Stack

| Component | Technology | Rationale |
|-----------|------------|-----------|
| **Large Language Model** | OpenAI GPT-4o | Best quality/speed/cost balance; proven performance |
| **Vector Database** | ChromaDB | Free, local, zero infrastructure; ideal for POC |
| **Embeddings** | OpenAI text-embedding-3-small | High quality, cost-effective ($0.02/1M tokens) |
| **Backend** | Python + FastAPI | Rapid development, async support |
| **Frontend** | Streamlit | Quick to build, sufficient for testing |

### Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                        User Interface                           │
│                    (Streamlit Chat App)                         │
└─────────────────────────┬───────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                     RAG Pipeline                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐  │
│  │   Query     │  │  Retrieve   │  │      Generate           │  │
│  │  Embedding  │─▶│  Top 3-5    │─▶│   Answer + Citations    │  │
│  │             │  │  Documents  │  │      (GPT-4o)           │  │
│  └─────────────┘  └─────────────┘  └─────────────────────────┘  │
└─────────────────────────┬───────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                    ChromaDB Vector Store                         │
│         (10-15 embedded knowledge documents)                     │
└─────────────────────────────────────────────────────────────────┘
```

### Data Flow

1. **Document Ingestion (One-time setup)**
   - Load markdown/text documents
   - Split into semantic chunks (~500 tokens each)
   - Generate embeddings via OpenAI API
   - Store vectors in ChromaDB

2. **Query Processing (Per user question)**
   - Convert user question to embedding
   - Search ChromaDB for similar document chunks
   - Retrieve top 3-5 most relevant chunks
   - Send query + context to GPT-4o
   - Return synthesized answer with source citations

---

## Deliverables

### POC Deliverables

| # | Deliverable | Description |
|---|-------------|-------------|
| 1 | **Working Prototype** | Functional RAG chat application |
| 2 | **Seed Knowledge Base** | 10-15 curated, embedded documents |
| 3 | **Test Results** | Accuracy evaluation across 10 test questions |
| 4 | **Findings Report** | Technical learnings and recommendations |
| 5 | **Go/No-Go Recommendation** | Data-driven decision for Phase 1 |

### Jira Stories

| ID | Story | Est. Points |
|----|-------|-------------|
| POC-1 | Set up development environment | 2 |
| POC-2 | Create initial knowledge base content (10-15 docs) | 3 |
| POC-3 | Implement document ingestion pipeline | 3 |
| POC-4 | Build core RAG query pipeline | 5 |
| POC-5 | Add source citations to responses | 2 |
| POC-6 | Create simple chat interface | 3 |
| POC-7 | Test with 10 "difficult" questions | 3 |
| POC-8 | Document POC findings & recommendations | 2 |
| | **Total** | **23 points** |

---

## Timeline

### 2-Week Sprint + Buffer

```
Week 1: Foundation
├── Days 1-2: Environment setup + Start content creation
├── Days 3-4: Complete content + Ingestion pipeline
└── Day 5: Start RAG pipeline development

Week 2: Build & Test
├── Days 1-2: Complete RAG pipeline + Citations
├── Days 3-4: Chat UI + Testing
└── Day 5: Document findings

Week 3: Buffer & Demo (if needed)
├── Fix issues found in testing
├── Prepare stakeholder demo
└── Finalize recommendations
```

### Key Milestones

| Milestone | Target Date | Criteria |
|-----------|-------------|----------|
| Environment Ready | End of Day 2 | Can run Python, access OpenAI API |
| Documents Ingested | End of Week 1 | 10-15 docs in ChromaDB |
| First Query Working | Mid Week 2 | End-to-end query returns answer |
| POC Complete | End of Week 2 | All test questions evaluated |
| Report Delivered | End of Week 3 | Findings documented, demo ready |

---

## Success Criteria

### Quantitative Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Retrieval Relevance** | ≥80% | Correct source documents retrieved for test queries |
| **Answer Accuracy** | ≥70% | Answers rated "helpful" by reviewers |
| **Response Time** | <5 seconds | Time from query to response |
| **Test Coverage** | 10 questions | Diverse "difficult" questions tested |

### Qualitative Criteria

- [ ] System retrieves relevant context for Vena-specific terminology
- [ ] Answers are coherent and cite their sources
- [ ] System gracefully handles questions outside knowledge base
- [ ] User experience is acceptable for continued testing

### Go/No-Go Decision Framework

| Outcome | Criteria | Action |
|---------|----------|--------|
| **GO** | ≥80% retrieval relevance, ≥70% answer accuracy | Proceed to Phase 1 implementation |
| **CONDITIONAL GO** | 60-79% metrics, clear improvement path | Address gaps, extend POC 1 week |
| **NO-GO** | <60% metrics, fundamental issues | Re-evaluate approach or technology |

---

## Resource Requirements

### Team

| Role | Person | Time Commitment |
|------|--------|-----------------|
| ML Engineer / Developer | Miles Waite | 80% for 2-3 weeks |
| Vena SME / Reviewer | [Manager] | 20% for review and testing |

### Infrastructure

| Resource | Cost | Notes |
|----------|------|-------|
| OpenAI API | ~$5-20 | Based on estimated usage during POC |
| Development Machine | $0 | Local development |
| ChromaDB | $0 | Open source, runs locally |

### Knowledge Base Content

**Critical Dependency:** The POC requires 10-15 seed documents to be curated. Suggested content:

| Type | Count | Source |
|------|-------|--------|
| Issue Resolutions | 5-6 | Historical tickets, team knowledge |
| VenaQL Patterns | 3-4 | Existing code examples |
| Concept Explainers | 2-3 | Platform documentation, SME input |
| Troubleshooting Guides | 2 | Common debugging approaches |

---

## Risks & Mitigations

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| **Insufficient seed content** | Cannot properly test retrieval | Medium | Start content gathering Day 1; accept smaller initial set |
| **Poor retrieval quality** | Inaccurate answers | Medium | Test multiple chunking strategies; adjust embedding approach |
| **OpenAI API issues** | Development delays | Low | Have Anthropic Claude as backup |
| **Scope creep** | Timeline overrun | Medium | Strict scope boundaries; defer all non-POC features |
| **Limited testing time** | Incomplete validation | Low | Prioritize highest-value test questions |

---

## Assumptions & Constraints

### Assumptions

1. OpenAI API access can be provisioned within Day 1
2. At least 10 quality documents can be sourced/created within Week 1
3. Local development environment is sufficient (no cloud infrastructure needed)
4. Miles Waite has capacity for 80% allocation during POC period

### Constraints

1. POC must complete within 3 weeks maximum
2. No production data to be used in knowledge base
3. No integration with external systems during POC
4. Limited to 2 testers (Miles + Manager)

---

## Next Steps

### Immediate Actions (Upon Approval)

1. **Create Jira Epic and Stories** — Set up tracking for POC-1 through POC-8
2. **Provision OpenAI API Access** — Obtain API key with appropriate budget
3. **Begin Content Gathering** — Identify first 5 documents for knowledge base
4. **Set Up Development Environment** — Python, dependencies, project structure

### Approval Required

| Approver | Role | Signature | Date |
|----------|------|-----------|------|
| [Manager Name] | Project Sponsor | _________ | _________ |
| Miles Waite | POC Lead | _________ | _________ |

---

## Appendix A: Example Test Questions

The following represent the types of "difficult" questions the POC should handle:

1. "How does FX conversion work when the rate source has missing periods?"
2. "Why would entity data be missing from a consolidation output?"
3. "What are the VenaQL constraints I need to know about?"
4. "How do I write a query that joins data across multiple intersections?"
5. "What causes COALESCE to fail with type mismatch errors?"
6. "How do I handle circular references in elimination entries?"
7. "What's the correct pattern for inverse FX rate calculations?"
8. "Why isn't my WHERE clause filtering the expected records?"
9. "How do I troubleshoot performance issues in complex queries?"
10. "What's the difference between slice types and when to use each?"

*Note: These are example questions — actual test set to be refined with Vena SME input.*

---

## Appendix B: Relationship to Full BRD

This POC validates the foundational capabilities defined in the Business Requirements Document v1.0:

| BRD Requirement | POC Coverage |
|-----------------|--------------|
| UR-001: Knowledge Query and Response | ✅ Primary focus |
| UR-002: VenaQL Code Explanation | ⚠️ Partial (if time permits) |
| UR-003: VenaQL Code Generation | ❌ Deferred to Phase 1 |
| UR-004: Issue Diagnosis Support | ❌ Deferred to Phase 2 |
| UR-005: Documentation Generation | ❌ Deferred to Phase 2 |
| FR-002: Knowledge Retrieval | ✅ Core validation |
| FR-003: Response Generation | ✅ Core validation |
| FR-006: Feedback Collection | ⚠️ Manual during POC |

---

*Document End*

