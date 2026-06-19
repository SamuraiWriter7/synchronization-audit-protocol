# Synchronization Audit Protocol

## 1. Overview

The Synchronization Audit Protocol is a minimal structure for recording observed similarities without prematurely converting them into claims of influence.

It is designed for cases where an idea, document, system, protocol, public event, or AI-generated interpretation appears to resemble another structure.

The protocol does not ask:

> “Is this copied?”

It first asks:

> “What kind of similarity is this, and what evidence supports that classification?”

## 2. Core Principle

Similarity does not prove influence.

Two structures may resemble each other for many reasons:

- coincidence
- shared constraints
- public discourse
- indirect influence
- direct reference
- AI-side reconstruction
- common source material
- environmental pressure
- historical timing

The protocol therefore separates observation from conclusion.

## 3. Classification Model

### A: Accidental Sync

The similarity is weak, generic, or plausibly coincidental.

Use this classification when:

- overlap is shallow
- shared terms are common
- structural order does not match
- no unique metaphor is shared
- no reference path exists

### B: Structural Convergence

The similarity is best explained by shared constraints or environmental pressure.

Use this classification when:

- different actors face the same problem
- physical, economic, technical, legal, or social pressures are similar
- the same architecture emerges independently
- no direct reference path is confirmed

This is the default classification for many infrastructure, AI, governance, and market patterns.

### C: Indirect Influence

Influence is plausible but not directly proven.

Use this classification when:

- the source was publicly accessible
- the target may have been exposed through discourse
- similar vocabulary and structure appear
- no direct citation or copying is confirmed

This classification preserves ambiguity.

### D: Direct Reference or Imitation

Direct reference, citation, imitation, copying, or derivation is supported by evidence.

Use this classification only when trace evidence exists.

Examples include:

- explicit citation
- link or backlink
- copied text
- reused diagram
- matching unique metaphor and sequence
- repository fork or derivative work
- documented access path

D should not be assigned based only on intuition.

### E: AI Reconstruction

The similarity may have been reconstructed or amplified by an AI system.

Use this classification when:

- AI context is known to include the source
- the output reproduces unusual structure without citation
- prompt dependency is evident
- retrieval or memory may have influenced the result
- the AI collapses multiple sources into an unattributed reconstruction

E does not necessarily imply malicious behavior.

It marks AI-side reconstruction risk.

## 4. Evidence Matrix

Each record contains eight evidence fields.

### 4.1 timestamp_order

Records whether one structure clearly predates the other.

Timestamp order is necessary but not sufficient.

Earlier publication does not prove influence.

### 4.2 vocabulary_overlap

Records shared terminology.

Vocabulary overlap is usually weak evidence unless the terms are rare, coined, or unusually combined.

### 4.3 structural_order_overlap

Records whether the same conceptual sequence, hierarchy, or architecture appears.

This is stronger than vocabulary overlap.

### 4.4 unique_metaphor_overlap

Records whether distinctive metaphors, symbolic frames, or unusual conceptual images overlap.

This can become strong evidence when combined with structural order overlap.

### 4.5 reference_path

Records whether there is any known path of reference, citation, access, backlink, quotation, or documented exposure.

This is central for moving from convergence to influence.

### 4.6 public_accessibility

Records whether the source was publicly available.

Public accessibility supports plausibility, but does not prove use.

### 4.7 ai_context_dependency

Records whether an AI system may have reconstructed, summarized, or amplified the similarity.

This is important when outputs appear structurally close but lack citation.

### 4.8 independent_constraint_pressure

Records whether independent external pressure can explain the similarity.

Strong independent constraint pressure often supports B: structural convergence.

## 5. Conclusion Style

Conclusions should avoid overclaiming.

Recommended language:

```text
No direct influence is proven.
Structural convergence is likely.
Indirect influence remains plausible.
Further trace evidence is required.
