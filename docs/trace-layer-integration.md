# Trace Layer Integration

## 1. Overview

The Trace Layer Integration connects Synchronization Audit records and Structure Fingerprints to external trace evidence.

This includes:

- case studies
- audit records
- trace receipts
- source contribution graphs
- repository commits
- public articles
- AI outputs
- external references

The purpose is to preserve origin paths without overclaiming influence.

## 2. Why Trace Layer Integration Matters

Similarity alone is not enough.

A strong audit requires trace anchors.

Trace anchors help reviewers answer:

- Was the source publicly available?
- Was there a documented reference path?
- Did an AI system have access to the structure?
- Was the structure transformed, summarized, or reconstructed?
- Is there a commit, article, receipt, or contribution graph that supports the timeline?

## 3. Trace References Are Not Proof

A trace reference is a pointer.

It is not automatic proof.

For example:

```text
A public article proves public accessibility.
It does not prove that a target actor read or used it.

Similarly:

A trace receipt may show source exposure.
It does not automatically prove direct imitation.

Trace references must be interpreted through the evidence matrix.

4. Supported Trace Reference Types

v0.3 supports the following reference types in structure-fingerprint.schema.json:

sync_audit_record
case_study
trace_receipt
source_contribution_graph
repository_commit
article
external_source
ai_output
other
5. Relation to AI Search Trace Receipt

Trace Receipt records how sources are accessed, transformed, summarized, or routed.

Synchronization Audit records how similarities are classified.

Structure Fingerprint records which structural features are being compared.

Together:

Trace Receipt = source/action transparency
Synchronization Audit = similarity classification
Structure Fingerprint = structural comparison layer
6. Relation to Source Contribution Graph

A Source Contribution Graph may show how multiple sources contribute to an output.

A Structure Fingerprint may show whether the output resembles a particular conceptual or structural pattern.

Together, they help separate:

direct source contribution
indirect structural influence
shared background discourse
AI-side reconstruction
independent convergence
7. Recommended Workflow
1. Observe similarity
2. Create or update Synchronization Audit Record
3. Create Structure Fingerprint if structural comparison is needed
4. Link case studies and trace references
5. Review evidence matrix
6. Assign conservative A-E classification
7. Escalate only if reference-path evidence is strong
8. Anti-Overclaiming Rule

Do not use Trace Layer Integration to inflate weak evidence.

A larger trace graph does not automatically mean stronger influence.

Evidence strength depends on:

timestamp order
reference path
structural order overlap
unique metaphor overlap
AI context dependency
independent constraint pressure
9. Final Principle

Trace without caution becomes accusation.

Caution without trace becomes fog.

The Trace Layer connects evidence while preserving uncertainty.
