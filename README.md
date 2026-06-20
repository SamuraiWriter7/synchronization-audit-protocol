# Synchronization Audit Protocol

A minimal audit protocol for recording and classifying observed similarities between ideas, documents, systems, protocols, public events, or AI-generated interpretations.

This protocol does not assume that similarity proves influence.

It provides a minimal audit structure for classifying observed similarities between ideas, documents, systems, protocols, public events, or AI-generated interpretations.

The purpose is to distinguish coincidence, structural convergence, indirect influence, direct reference, and AI-side reconstruction without collapsing them into a vague notion of “synchronization.”

## Purpose

The Synchronization Audit Protocol exists to slow down premature interpretation.

When two structures appear similar, it is tempting to immediately assume influence, imitation, theft, resonance, or hidden synchronization. This protocol avoids that shortcut.

Instead, it asks:

- Which structure appeared first?
- Are the vocabularies actually similar?
- Is the structural order similar?
- Are unique metaphors reused?
- Is there any reference path?
- Was the source publicly accessible?
- Could an AI system have reconstructed the similarity?
- Could independent constraints explain the convergence?

The goal is not accusation.

The goal is evidence-based origin auditing.

## Classification Model

The protocol uses five fixed classifications.

| Code | Label | Meaning |
|---|---|---|
| A | `accidental_sync` | Similarity appears coincidental or too weak to support a stronger claim. |
| B | `structural_convergence` | Similarity is likely caused by shared constraints, timing, environment, or common structural pressures. |
| C | `indirect_influence` | Influence is plausible through public availability, diffusion, shared discourse, or intermediary systems, but no direct reference is proven. |
| D | `direct_reference_or_imitation` | Direct reference, copying, imitation, citation, or derivation is supported by evidence. |
| E | `ai_reconstruction` | Similarity may have been reconstructed, amplified, or reassembled by an AI system from prior context, training exposure, retrieval, or prompt dependency. |

## Evidence Matrix

Each audit record includes the following evidence fields:

| Field | Purpose |
|---|---|
| `timestamp_order` | Checks whether one structure clearly predates the other. |
| `vocabulary_overlap` | Measures shared terminology. |
| `structural_order_overlap` | Checks whether the sequence, hierarchy, or architecture is similar. |
| `unique_metaphor_overlap` | Checks whether distinctive metaphors or symbolic frames overlap. |
| `reference_path` | Records citations, links, backlinks, mentions, or access paths. |
| `public_accessibility` | Records whether the source could have been accessed publicly. |
| `ai_context_dependency` | Checks whether AI context, memory, retrieval, or reconstruction may have shaped the similarity. |
| `independent_constraint_pressure` | Evaluates whether shared external constraints are enough to explain the similarity. |

## Why Unique Metaphor and Structural Order Matter

Vocabulary overlap is weak evidence by itself.

Many people may independently use terms like “AI infrastructure,” “data center,” “trace,” “memory,” or “governance.”

However, overlap becomes stronger when two elements appear together:

1. Unique metaphors
2. Similar structural order

For example, if two systems share not only words but also the same sequence of concepts, the same layered architecture, and the same unusual metaphor, the audit weight increases.

This does not automatically prove influence.

It means the similarity deserves stronger trace review.

## Repository Structure

```text
.
├── README.md
├── CHANGELOG.md
├── docs/
│   └── synchronization-audit-protocol.md
├── schemas/
│   └── sync-audit-record.schema.json
├── examples/
│   └── sync-audit-record.example.yaml
├── scripts/
│   └── validate_examples.py
└── .github/
    └── workflows/
        └── validate-examples.yml
Validation

Install dependencies:

pip install jsonschema pyyaml

Run validation:

python scripts/validate_examples.py

Expected result:

[validate] Synchronization Audit Record
  schema : schemas/sync-audit-record.schema.json
  example: examples/sync-audit-record.example.yaml
[ok] Synchronization Audit Record example is valid
v0.1 Scope

v0.1 places the audit ruler.

It does not yet attempt automated detection, legal judgment, attribution enforcement, or case-study expansion.

The focus is:

fixed A–E classification
minimal audit record schema
evidence matrix
conservative conclusion style
one calm example case
Roadmap
v0.1 = Place the audit ruler
v0.2 = Add case studies
v0.3 = Connect to Structure Fingerprint / Trace Layer
v0.4 = Connect to Defense Court Protocol
v0.5 = Add AI Agent Hook / automatic synchronization detection
Principle

Similarity is not proof.

Synchronization is not causality.

A strong audit begins before excitement, accusation, or resonance.

First calibrate the radar.


## 6. `docs/synchronization-audit-protocol.md`

```markdown
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

Avoid language such as:

This proves copying.
This was definitely stolen.
They must have used the source.

unless strong direct evidence exists.

6. v0.1 Scope

v0.1 only provides the audit ruler.

It includes:

one JSON Schema
one example record
one validation script
one GitHub Actions workflow
this protocol document

It does not include:

automated similarity detection
legal attribution review
machine-generated scoring
case-study archive
integration with other trace systems

Those are reserved for later versions.

7. Roadmap
v0.1 = Place the audit ruler
v0.2 = Add case studies
v0.3 = Connect to Structure Fingerprint / Trace Layer
v0.4 = Connect to Defense Court Protocol
v0.5 = Add AI Agent Hook / automatic synchronization detection
8. Final Principle

Resonance is valuable.

But resonance without audit becomes fog.

This protocol exists to keep the fog from pretending to be evidence.


## 7. `CHANGELOG.md`

```markdown
# Changelog

All notable changes to this project will be documented in this file.

## [v0.1.0-candidate] - 2026-06-20

### Added

- Added initial Synchronization Audit Protocol repository structure.
- Added `sync-audit-record.schema.json`.
- Added fixed A–E classification model:
  - `A = accidental_sync`
  - `B = structural_convergence`
  - `C = indirect_influence`
  - `D = direct_reference_or_imitation`
  - `E = ai_reconstruction`
- Added evidence matrix fields:
  - `timestamp_order`
  - `vocabulary_overlap`
  - `structural_order_overlap`
  - `unique_metaphor_overlap`
  - `reference_path`
  - `public_accessibility`
  - `ai_context_dependency`
  - `independent_constraint_pressure`
- Added first example:
  - `centralized_ai_backlash_memory_inflation`
- Added Python validation script.
- Added GitHub Actions workflow for example validation.
- Added protocol documentation.

### Notes

v0.1 places the audit ruler before case-study expansion.

The purpose of this version is not to prove influence, imitation, or causality.

The purpose is to classify observed similarities with a conservative evidence structure.

## v0.2 Case Study Layer

v0.2 adds the Case Study Layer.

v0.1 placed the audit ruler.

v0.2 applies that ruler to multiple examples.

The purpose is not to accuse, prove imitation, or claim influence. The purpose is to test the A–E classification model against concrete similarity patterns.

### Added Case Studies

```text
docs/case-studies/
├── centralized-ai-backlash-memory-inflation.md
├── data-center-local-resistance.md
└── ai-search-trace-origin-opacity.md
Added Example Records
examples/
├── sync-audit-record.centralized-ai-backlash-memory-inflation.example.yaml
├── sync-audit-record.data-center-local-resistance.example.yaml
└── sync-audit-record.ai-search-trace-origin-opacity.example.yaml
Case Study Discipline

Each case study must preserve the distinction between:

similarity
convergence
influence
direct reference
AI-side reconstruction

No case study should begin with an accusation.

Every case study should begin with an observed similarity and then classify it conservatively.

## v0.3 Structure Fingerprint / Trace Layer

v0.3 adds the Structure Fingerprint and Trace Layer Integration.

v0.1 placed the audit ruler.

v0.2 applied the ruler to case studies.

v0.3 adds a comparison layer for recording structural features without treating them as proof.

### Added Documents

```text
docs/
├── structure-fingerprint.md
└── trace-layer-integration.md
Added Schema
schemas/
└── structure-fingerprint.schema.json
Added Example
examples/
└── structure-fingerprint.example.yaml
Structure Fingerprint

A Structure Fingerprint records comparison features such as:

vocabulary signature
structural sequence
metaphor signature
dependency pattern
transformation pattern
trace layer references

A Structure Fingerprint is not a verdict.

It does not prove copying, influence, imitation, or causality.

It is a comparison aid that supports Synchronization Audit Records.

Trace Layer Integration

Trace Layer Integration connects audit records and fingerprints to evidence anchors such as:

case studies
trace receipts
source contribution graphs
repository commits
public articles
AI outputs
external sources

Trace references are pointers.

They are not automatic proof.

v0.3 Principle
A fingerprint is a map of resemblance.
It is not a verdict.

## v0.4 Defense Court Protocol Integration

v0.4 adds Defense Court Protocol Integration.

This layer does not create verdicts.

It prepares synchronization audit records and structure fingerprints for human review.

### Added Documents

```text
docs/
└── defense-court-integration.md
Added Schema
schemas/
└── defense-court-bridge.schema.json
Added Example
examples/
└── defense-court-bridge.example.yaml
Defense Court Bridge

A Defense Court Bridge record connects:

synchronization audit records
structure fingerprints
case studies
trace references
evidence status
classification stability
human review boundaries

It is designed for cases where similarity may create public accusation risk, attribution dispute, AI reconstruction concern, or high-impact interpretation.

Human Review Boundary

v0.4 makes the review boundary explicit.

AI may assist with:

summarization
structural comparison
missing evidence lists
non-verdict packet preparation

AI must not:

declare theft
assign legal responsibility
convert similarity into proof
bypass human review
treat structure fingerprints as verdicts
v0.4 Principle
Audit is not accusation.
Fingerprint is not proof.
Bridge is not verdict.
Human review is the gate.
