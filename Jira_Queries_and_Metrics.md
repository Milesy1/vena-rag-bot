# Jira Queries and Metrics Guide
## Based on Vena RAG Bot BRD Requirements

This document provides practical JQL queries and dashboard suggestions for tracking the RAG Bot project based on the Business Requirements Document.

---

## Useful JQL Queries

### 1. Phase-Based Queries

**All Phase 1 Stories:**
```jql
project = "FRBP" AND labels = "Phase1" AND type = Story
```

**All Phase 2 Stories:**
```jql
project = "FRBP" AND labels = "Phase2" AND type = Story
```

**Phase 1 Stories by Status:**
```jql
project = "FRBP" AND labels = "Phase1" AND status = "In Progress"
```

**Phase 1 Completed:**
```jql
project = "FRBP" AND labels = "Phase1" AND status = Done
```

---

### 2. Epic-Based Queries

**Stories by Epic:**
```jql
project = "FRBP" AND "Epic Link" = FRBP-1
```

**All Epics:**
```jql
project = "FRBP" AND type = Epic
```

**Epics with Unresolved Stories:**
```jql
project = "FRBP" AND type = Epic AND status != Done
```

---

### 3. Requirement-Based Queries

**Stories for User Requirements (UR-001 to UR-007):**
```jql
project = "FRBP" AND (summary ~ "UR-001" OR summary ~ "UR-002" OR summary ~ "UR-003")
```

**Stories for Functional Requirements (FR-001 to FR-013):**
```jql
project = "FRBP" AND (summary ~ "FR-001" OR summary ~ "FR-002" OR summary ~ "FR-003")
```

**Stories for Non-Functional Requirements:**
```jql
project = "FRBP" AND (summary ~ "NFR" OR labels = "NFR")
```

**Security and Compliance Stories:**
```jql
project = "FRBP" AND (labels = "Security" OR labels = "Compliance" OR labels = "GDPR" OR labels = "Audit")
```

---

### 4. Priority-Based Queries

**Critical Priority Stories:**
```jql
project = "FRBP" AND priority = Highest AND type = Story
```

**High Priority Stories:**
```jql
project = "FRBP" AND priority = High AND type = Story
```

**Critical/High Priority Not Started:**
```jql
project = "FRBP" AND priority in (Highest, High) AND status = "To Do"
```

---

### 5. Component/Feature-Based Queries

**Knowledge Base Management:**
```jql
project = "FRBP" AND (summary ~ "Knowledge Base" OR summary ~ "Document Ingestion" OR labels = "Knowledge-Base")
```

**Code Generation:**
```jql
project = "FRBP" AND (summary ~ "Code Generation" OR summary ~ "VenaQL" OR labels = "Code-Generation")
```

**RAG Pipeline:**
```jql
project = "FRBP" AND (summary ~ "RAG" OR summary ~ "Retrieval" OR labels = "RAG")
```

**User Interface:**
```jql
project = "FRBP" AND (summary ~ "UI" OR summary ~ "Interface" OR summary ~ "Chat" OR labels = "UI")
```

**Validation:**
```jql
project = "FRBP" AND (summary ~ "Validation" OR summary ~ "Code Validation" OR labels = "Validation")
```

---

### 6. Resource/Assignee Queries

**Stories Assigned to ML Engineer:**
```jql
project = "FRBP" AND assignee = "ml-engineer-username" AND type = Story
```

**Stories Assigned to Vena SME:**
```jql
project = "FRBP" AND assignee = "vena-sme-username" AND type = Story
```

**Unassigned Stories:**
```jql
project = "FRBP" AND assignee is EMPTY AND type = Story
```

**Stories by Team Member:**
```jql
project = "FRBP" AND assignee in (user1, user2, user3) AND status != Done
```

---

### 7. Risk and Dependency Queries

**Stories Linked to Risks:**
```jql
project = "FRBP" AND issueFunction in linkedIssuesOf("labels = Risk")
```

**Stories with Blockers:**
```jql
project = "FRBP" AND status = Blocked
```

**Stories with Dependencies:**
```jql
project = "FRBP" AND issueFunction in hasLinks("is blocked by")
```

**High-Risk Stories:**
```jql
project = "FRBP" AND labels = "High-Risk" AND status != Done
```

---

### 8. Testing and QA Queries

**Testing Stories:**
```jql
project = "FRBP" AND (summary ~ "Test" OR summary ~ "QA" OR labels = "Testing")
```

**Stories Ready for Testing:**
```jql
project = "FRBP" AND status = "Ready for Testing"
```

**Bugs Found:**
```jql
project = "FRBP" AND type = Bug
```

**Stories with Test Coverage:**
```jql
project = "FRBP" AND labels = "Tested"
```

---

### 9. Compliance and Security Queries

**Security Stories:**
```jql
project = "FRBP" AND (labels = "Security" OR summary ~ "Security" OR summary ~ "Encryption")
```

**GDPR/Compliance Stories:**
```jql
project = "FRBP" AND (labels = "GDPR" OR labels = "Compliance" OR summary ~ "GDPR" OR summary ~ "Data Protection")
```

**Audit Stories:**
```jql
project = "FRBP" AND (labels = "Audit" OR summary ~ "Audit" OR summary ~ "Logging")
```

**All Compliance-Related (Section 18-20):**
```jql
project = "FRBP" AND (labels in ("Security", "Compliance", "GDPR", "Audit", "Governance"))
```

---

### 10. Progress and Velocity Queries

**Stories Completed This Sprint:**
```jql
project = "FRBP" AND status = Done AND updated >= startOfWeek()
```

**Stories Completed This Month:**
```jql
project = "FRBP" AND status = Done AND resolved >= startOfMonth()
```

**In Progress Stories:**
```jql
project = "FRBP" AND status = "In Progress"
```

**Stories by Story Points:**
```jql
project = "FRBP" AND "Story Points" >= 5 AND type = Story
```

**Total Story Points by Epic:**
```jql
project = "FRBP" AND type = Epic
```
*(Use Jira's built-in Epic report for this)*

---

### 11. User Persona Queries

**New Contractor Features:**
```jql
project = "FRBP" AND labels = "New-Contractor"
```

**Active Developer Features:**
```jql
project = "FRBP" AND labels = "Active-Developer"
```

**Technical Consultant Features:**
```jql
project = "FRBP" AND labels = "Technical-Consultant"
```

---

### 12. Acceptance Criteria Queries

**Stories Without Acceptance Criteria:**
```jql
project = "FRBP" AND type = Story AND description !~ "Acceptance Criteria"
```

**Stories Ready for Review:**
```jql
project = "FRBP" AND status = "Ready for Review"
```

---

### 13. Time-Based Queries

**Stories Due This Week:**
```jql
project = "FRBP" AND dueDate <= endOfWeek() AND dueDate >= startOfWeek()
```

**Overdue Stories:**
```jql
project = "FRBP" AND dueDate < now() AND status != Done
```

**Stories Created This Month:**
```jql
project = "FRBP" AND created >= startOfMonth()
```

---

### 14. Decision Tickets (Architecture Decisions)

**All Architecture Decisions:**
```jql
project = "FRBP" AND type = Decision
```

**Pending Decisions:**
```jql
project = "FRBP" AND type = Decision AND status != "Approved"
```

**Technology Decisions:**
```jql
project = "FRBP" AND type = Decision AND labels = "Technology"
```

---

## Useful Dashboards and Reports

### 1. Phase 1 Progress Dashboard

**Widgets:**
- **Phase 1 Epic Progress** - Pie chart showing Done vs In Progress vs To Do
- **Phase 1 Story Points Burndown** - Burndown chart for Phase 1 stories
- **Phase 1 Stories by Status** - Bar chart
- **Phase 1 Velocity** - Velocity chart showing story points completed per sprint

**JQL for Widget:**
```jql
project = "FRBP" AND labels = "Phase1" AND type = Story
```

---

### 2. Requirements Coverage Dashboard

**Widgets:**
- **User Requirements Progress** - Shows completion of UR-001 through UR-007
- **Functional Requirements Progress** - Shows completion of FR-001 through FR-013
- **Non-Functional Requirements Progress** - Shows NFR completion
- **Requirements by Priority** - Stacked bar chart

**JQL Example:**
```jql
project = "FRBP" AND (summary ~ "UR-" OR summary ~ "FR-" OR summary ~ "NFR-")
```

---

### 3. Resource Allocation Dashboard

**Widgets:**
- **Workload by Assignee** - Shows story points assigned to each team member
- **Unassigned Work** - List of unassigned stories
- **Team Capacity** - Shows available vs allocated capacity
- **Sprint Commitment** - Story points committed per sprint

**JQL for Workload:**
```jql
project = "FRBP" AND assignee is not EMPTY AND status != Done
```

---

### 4. Risk and Dependency Dashboard

**Widgets:**
- **Blocked Stories** - List of blocked stories
- **High-Risk Stories** - Stories with high-risk label
- **Dependency Map** - Visual representation of dependencies
- **Risk Mitigation Progress** - Stories related to risk mitigation

**JQL for Blocked:**
```jql
project = "FRBP" AND status = Blocked
```

---

### 5. Quality and Testing Dashboard

**Widgets:**
- **Test Coverage** - Percentage of stories with test coverage
- **Bugs by Priority** - Bugs grouped by priority
- **Stories Ready for Testing** - List of stories awaiting testing
- **Test Execution Progress** - Test cases executed vs total

**JQL for Test Coverage:**
```jql
project = "FRBP" AND labels = "Tested" AND type = Story
```

---

### 6. Compliance and Security Dashboard

**Widgets:**
- **Security Stories Progress** - Progress on security-related stories
- **GDPR Compliance Progress** - GDPR-related stories
- **Audit Trail Stories** - Stories related to audit logging
- **Compliance Checklist** - Checklist of compliance requirements

**JQL for Security:**
```jql
project = "FRBP" AND labels in ("Security", "Compliance", "GDPR", "Audit")
```

---

### 7. Knowledge Base Progress Dashboard

**Widgets:**
- **Document Ingestion Progress** - Stories related to knowledge base
- **Content Creation Progress** - Stories for creating initial content
- **Knowledge Base Size** - Track number of documents ingested
- **Content Quality Metrics** - Stories for content review

**JQL:**
```jql
project = "FRBP" AND (summary ~ "Knowledge Base" OR summary ~ "Document" OR labels = "Knowledge-Base")
```

---

### 8. Architecture Decisions Dashboard

**Widgets:**
- **Pending Decisions** - Decisions awaiting approval
- **Decision Status** - Pie chart of decision statuses
- **Technology Decisions** - Decisions related to technology choices
- **Decision Timeline** - Timeline of key decisions

**JQL:**
```jql
project = "FRBP" AND type = Decision
```

---

## Key Metrics to Track (Based on BRD Section 14)

### 1. Adoption Metrics

**Track in Jira:**
- Number of active users (track via custom field or label)
- Queries per user per day (track via linked issues or comments)
- User retention rate (track via user activity)

**JQL:**
```jql
project = "FRBP" AND labels = "User-Adoption" AND type = Story
```

---

### 2. Quality Metrics

**Track in Jira:**
- Response accuracy (link test results to stories)
- Code generation acceptance rate (track via acceptance criteria)
- User satisfaction score (track via feedback stories)

**JQL for Quality Stories:**
```jql
project = "FRBP" AND (labels = "Quality" OR labels = "Testing" OR summary ~ "Accuracy")
```

---

### 3. Business Impact Metrics

**Track in Jira:**
- Reduction in senior resource time (track via time tracking or labels)
- Contractor onboarding time reduction (track via stories)
- Self-service resolution rate (track via analytics stories)

**JQL:**
```jql
project = "FRBP" AND labels = "Business-Impact"
```

---

### 4. Technical Performance Metrics

**Track in Jira:**
- Average response time (track via performance stories)
- System uptime (track via monitoring stories)
- Error rate (track via bug stories)
- API cost per query (track via cost stories)

**JQL for Performance:**
```jql
project = "FRBP" AND (labels = "Performance" OR summary ~ "Performance" OR summary ~ "Response Time")
```

---

## Recommended Jira Labels

Based on the BRD, use these labels consistently:

### Phase Labels
- `Phase1`
- `Phase2`

### Requirement Labels
- `UR-001`, `UR-002`, `UR-003`, etc. (User Requirements)
- `FR-001`, `FR-002`, `FR-003`, etc. (Functional Requirements)
- `NFR-001`, `NFR-002`, etc. (Non-Functional Requirements)

### Feature Labels
- `Knowledge-Base`
- `Code-Generation`
- `RAG`
- `UI`
- `Validation`
- `Testing`

### Persona Labels
- `New-Contractor`
- `Active-Developer`
- `Technical-Consultant`

### Compliance Labels
- `Security`
- `Compliance`
- `GDPR`
- `Audit`
- `Governance`

### Priority Labels
- `High-Risk`
- `Critical-Path`
- `Blocked`

### Status Labels
- `Tested`
- `Reviewed`
- `Ready-for-Production`

---

## Useful Jira Filters

Create saved filters for:

1. **Phase 1 Active Work**
   ```jql
   project = "FRBP" AND labels = "Phase1" AND status in ("To Do", "In Progress")
   ```

2. **This Sprint's Work**
   ```jql
   project = "FRBP" AND sprint in openSprints()
   ```

3. **Blocked Items**
   ```jql
   project = "FRBP" AND status = Blocked
   ```

4. **Security & Compliance**
   ```jql
   project = "FRBP" AND labels in ("Security", "Compliance", "GDPR", "Audit")
   ```

5. **High Priority Unresolved**
   ```jql
   project = "FRBP" AND priority in (Highest, High) AND status != Done
   ```

---

## Sprint Planning Queries

**Stories for Next Sprint:**
```jql
project = "FRBP" AND labels = "Phase1" AND status = "To Do" AND priority in (Highest, High) ORDER BY priority DESC
```

**Stories Ready for Sprint Planning:**
```jql
project = "FRBP" AND status = "Ready for Development" AND labels = "Phase1"
```

**Stories with Dependencies Resolved:**
```jql
project = "FRBP" AND status = "To Do" AND issueFunction in hasLinks("is blocked by") = false
```

---

## Reporting Queries

**Monthly Progress Report:**
```jql
project = "FRBP" AND resolved >= startOfMonth() AND resolved <= endOfMonth()
```

**Stories Completed by Epic:**
```jql
project = "FRBP" AND status = Done AND "Epic Link" is not EMPTY
```

**Velocity by Sprint:**
```jql
project = "FRBP" AND sprint in closedSprints() AND status = Done
```

---

*Document created: January 5, 2026*
*Based on BRD Version 1.1*

