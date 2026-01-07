# Production Architecture Decision - Vena RAG Bot

**Document Version:** 1.0  
**Date:** January 5, 2026  
**Status:** Under Review

---

## Executive Summary

This document defines the target production architecture for the Vena RAG Bot system. The architecture is designed to scale from the current POC (10 users) to full production (500+ users) whilst maintaining cost efficiency and operational simplicity.

**Key Decision:** Select final production technology stack that will serve as the target state for all future development phases.

---

## Current State (POC)

**Technology Stack:**
- Frontend: Streamlit
- Vector Database: ChromaDB (local storage)
- LLM: OpenAI GPT-4o
- Embeddings: OpenAI text-embedding-3-small
- Framework: LangChain
- Hosting: Local development

**Status:** Working prototype, validates RAG approach

---

## Target Production Architecture

### Core Components

**1. Vector Database: Qdrant Cloud**

**Rationale:**
- Production-grade performance and reliability
- Persistent storage (no data loss risk)
- Hybrid search capability (semantic + keyword)
- Multi-tenant support for organisation isolation
- Managed cloud service (no infrastructure management)
- Better price-to-performance ratio than alternatives

**Alternatives Considered:**
- Pinecone: More expensive, similar features
- Weaviate: Requires infrastructure management
- ChromaDB: Not suitable for production scale

**Cost:** £50-200 per month depending on scale

---

**2. Backend API: FastAPI**

**Rationale:**
- Industry standard for Python ML/AI applications
- Excellent async support (crucial for LLM API calls)
- Automatic API documentation
- Type safety with Pydantic
- Easy deployment and scaling
- Strong performance

**Cost:** Included in hosting costs

---

**3. Frontend: React + Next.js (or Streamlit)**

**Rationale:**
- React: Professional, scalable, industry standard
- Next.js: Server-side rendering, excellent performance
- Alternative: Streamlit if simplicity preferred

**Decision:** To be confirmed based on user requirements

**Cost:** Included in hosting costs

---

**4. LLM Provider: Dual Provider Strategy**

**Primary: OpenAI GPT-4o**
- Best quality responses
- Excellent code generation
- Proven reliability

**Backup: Anthropic Claude 3.5 Sonnet**
- Redundancy if OpenAI unavailable
- Different strengths for comparison
- Negotiation leverage

**Rationale:**
- Redundancy ensures system availability
- Ability to A/B test quality
- Better negotiating position with providers
- Different models for different use cases

**Cost:** £100-500 per month (usage-based)

---

**5. Database: PostgreSQL**

**Rationale:**
- Industry standard relational database
- Stores user accounts, organisations, usage logs
- Analytics and billing data
- Can add pgvector extension if needed later
- Excellent tooling and support

**Cost:** Included in hosting platform

---

**6. Hosting: Railway (London Region)**

**Rationale:**
- London datacentre (low latency for UK customers)
- Easy deployment from GitHub
- PostgreSQL included
- Auto-scaling capability
- Usage-based pricing
- Minimal DevOps overhead

**Cost:** £50-100 per month

---

**7. Additional Services (Phase 2+)**

**Redis Caching**
- Cache common queries to reduce LLM costs
- Faster response times
- Cost: £10-20 per month

**Cohere Reranking**
- Improve retrieval precision by 20-30%
- Better answer quality
- Cost: £20-50 per month

**Authentication: Clerk or Auth0**
- User authentication and authorisation
- Required for external customers
- Cost: £0-25 per month

**Monitoring: Sentry + PostHog**
- Error tracking and product analytics
- Essential for production debugging
- Cost: £0-50 per month

**CDN: Cloudflare**
- DDoS protection and caching
- Required for external-facing applications
- Cost: £0-20 per month

---

## Architecture Diagram

```
┌─────────────────────────────────────────────┐
│ Frontend                                     │
│ React + Next.js (or Streamlit)               │
└──────────────┬──────────────────────────────┘
               │
┌──────────────▼──────────────────────────────┐
│ API Layer                                    │
│ FastAPI (Python)                             │
│ - REST endpoints                             │
│ - Authentication                             │
│ - Rate limiting                              │
│ - Request logging                            │
└──────────────┬──────────────────────────────┘
               │
┌──────────────▼──────────────────────────────┐
│ RAG Engine                                   │
│ LangChain (orchestration)                     │
│ - Query processing                           │
│ - Retrieval logic                            │
│ - Response generation                        │
└──────────────┬──────────────────────────────┘
               │
       ┌───────┴───────┐
       │               │
┌──────▼──────┐ ┌─────▼──────────┐
│ Vector DB   │ │ LLM Providers  │
│ Qdrant Cloud│ │ OpenAI GPT-4o  │
│             │ │ Claude (backup)│
└─────────────┘ └────────────────┘
       │
┌──────▼──────┐
│ Database    │
│ PostgreSQL  │
│ - Users     │
│ - Logs      │
│ - Analytics │
└─────────────┘
       │
┌──────▼──────┐
│ Hosting      │
│ Railway      │
│ (London)     │
└─────────────┘
```

---

## Benefits of Target Architecture

**Scalability**
- Supports 100-500 users in Phase 2
- Can scale to 1000+ users with minimal changes
- Auto-scaling infrastructure

**Reliability**
- Dual LLM provider (redundancy)
- Persistent vector storage (no data loss)
- Managed services (reduced operational risk)

**Cost Efficiency**
- Estimated £300-500 per month for 100-500 users
- Usage-based pricing scales with growth
- No upfront infrastructure costs

**Maintainability**
- Industry standard technologies
- Good documentation and community support
- Easy to hire developers familiar with stack

**Performance**
- Hybrid search (semantic + keyword) for better results
- Caching layer reduces costs and latency
- London hosting for low UK latency

**Security**
- Multi-tenant isolation in Qdrant
- Proper authentication and authorisation
- Data encryption in transit and at rest

---

## Migration Roadmap

### Phase 1: POC to MVP (Months 1-2)

**Current Stack (Keep):**
- Streamlit frontend (works, sufficient for Phase 1)
- ChromaDB (free, adequate for 10 users)
- LangChain framework (already implemented)
- OpenAI GPT-4o (proven quality)

**Add:**
- FastAPI backend (Month 2)
- PostgreSQL database (Month 2, for users and logs)
- Railway hosting (Month 2, proper deployment)

**Focus:**
- Core RAG functionality
- Code generation capabilities
- Basic analytics

**Cost:** £70-250 per month

---

### Phase 2: Production Ready (Months 3-4)

**Migrate:**
- ChromaDB → Qdrant Cloud (persistent storage, hybrid search)
- Add Redis caching (reduce LLM costs)
- Enhance monitoring (Sentry for errors)

**Add:**
- User authentication (if selling externally)
- Advanced analytics dashboard
- Performance optimisations

**Focus:**
- Scale to 50 concurrent users
- Production reliability
- User management

**Cost:** £300-500 per month

---

### Phase 3: Enhanced Production (Months 5-6)

**Add:**
- Cohere reranking (improve answer quality)
- PostHog analytics (product insights)
- CDN/Cloudflare (if external-facing)
- Advanced error handling

**Focus:**
- Scale to 100-500 users
- Enterprise features
- Advanced monitoring

**Cost:** £500-800 per month

---

### Phase 4: Enterprise Scale (Month 6+)

**Enhance:**
- Multi-region deployment (if needed)
- Advanced caching strategies
- Custom domain and branding
- Backup and disaster recovery

**Focus:**
- 500+ users
- Enterprise customers
- SLA compliance

**Cost:** £800-1000+ per month

---

## Cost Summary

| Phase | Users | Monthly Cost | Annual Cost |
|-------|-------|--------------|-------------|
| Phase 1 (MVP) | 10 | £70-250 | £840-3,000 |
| Phase 2 (Production) | 50 | £300-500 | £3,600-6,000 |
| Phase 3 (Enhanced) | 100-500 | £500-800 | £6,000-9,600 |
| Phase 4 (Enterprise) | 500+ | £800-1,000+ | £9,600-12,000+ |

**Budget Alignment:**
- Phase 1 budget: £8,000-32,000 per year
- Phase 1 actual: £840-3,000 per year (well within budget)

---

## Decision Criteria

**Technology Selection Based On:**
- Proven performance in production environments
- Cost efficiency at scale
- Ease of maintenance and operation
- UK/EU data residency options
- Community support and documentation
- Migration path from POC

**Key Requirements Met:**
- Scalable from 10 to 500+ users
- Cost-effective for Phase 1 budget
- Reliable and maintainable
- Supports all Phase 1 functional requirements
- Clear migration path from POC

---

## Risks and Mitigations

**Risk 1: Vendor Lock-in**
- Mitigation: Use standard APIs, design abstraction layers
- Impact: Medium
- Probability: Low

**Risk 2: Cost Overruns**
- Mitigation: Monitor usage, implement caching, set budgets
- Impact: Medium
- Probability: Medium

**Risk 3: Migration Complexity**
- Mitigation: Design Phase 1 code for migration, incremental approach
- Impact: Medium
- Probability: Low

**Risk 4: Technology Changes**
- Mitigation: Choose established technologies, maintain flexibility
- Impact: Low
- Probability: Low

---

## Next Steps

1. **Review and Approve Architecture** (This week)
   - Stakeholder review of target architecture
   - Confirm technology choices
   - Approve migration roadmap

2. **Phase 1 Implementation** (Months 1-2)
   - Build on POC stack
   - Add FastAPI and PostgreSQL
   - Design for future migration

3. **Phase 2 Migration** (Months 3-4)
   - Migrate to Qdrant Cloud
   - Add production services
   - Scale to 50 users

4. **Continuous Improvement** (Ongoing)
   - Monitor costs and performance
   - Add services as needed
   - Optimise based on usage patterns

---

## Approval

**Status:** Under Review

**Decision Required By:** [Date]

**Approvers:**
- [ ] Project Sponsor
- [ ] Technical Lead
- [ ] Infrastructure Team
- [ ] Finance/Budget Approval

**Decided By:** [Name/Date]

---

*Document prepared by: Miles Waite*  
*Date: January 5, 2026*

