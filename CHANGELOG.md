# Changelog

## [v0.4.0-candidate] - 2026-06-20

### Added

- Added Defense Court Protocol Integration.
- Added `docs/defense-court-integration.md`.
- Added `schemas/defense-court-bridge.schema.json`.
- Added `examples/defense-court-bridge.example.yaml`.
- Updated `scripts/validate_examples.py` to validate Defense Court Bridge examples.

### Defense Court Bridge

The Defense Court Bridge provides a non-verdict handoff layer between:

- Synchronization Audit Records
- Structure Fingerprints
- Case Studies
- Trace Layer references
- Human review
- Formal Defense Court Protocol review

### Human Review Boundary

v0.4 makes explicit that AI may assist with summarization, comparison, and packet preparation, but must not:

- declare theft
- assign legal responsibility
- convert similarity into proof
- treat fingerprints as verdicts
- bypass human review

### Principle

Audit is not accusation.

Fingerprint is not proof.

Bridge is not verdict.

Human review is the gate.

## [v0.3.0-candidate] - 2026-06-20

### Added

- Added Structure Fingerprint layer.
- Added `schemas/structure-fingerprint.schema.json`.
- Added `examples/structure-fingerprint.example.yaml`.
- Added `docs/structure-fingerprint.md`.
- Added `docs/trace-layer-integration.md`.
- Updated `scripts/validate_examples.py` to validate multiple schema/example groups.

### Structure Fingerprint Components

The new Structure Fingerprint schema supports:

- `vocabulary_signature`
- `structural_sequence`
- `metaphor_signature`
- `dependency_pattern`
- `transformation_pattern`
- `trace_layer_refs`

### Notes

v0.3 does not introduce automatic verdicts.

A Structure Fingerprint is not proof of influence, imitation, copying, or causality.

It is a comparison aid that helps Synchronization Audit Records evaluate structural similarity more carefully.

### Principle

A fingerprint is a map of resemblance.

It is not a verdict.

## [v0.2.0-candidate] - 2026-06-20

### Added

- Added Case Study Layer.
- Added `docs/case-study-method.md`.
- Added case study directory:
  - `docs/case-studies/centralized-ai-backlash-memory-inflation.md`
  - `docs/case-studies/data-center-local-resistance.md`
  - `docs/case-studies/ai-search-trace-origin-opacity.md`
- Added multiple example audit records:
  - `sync-audit-record.centralized-ai-backlash-memory-inflation.example.yaml`
  - `sync-audit-record.data-center-local-resistance.example.yaml`
  - `sync-audit-record.ai-search-trace-origin-opacity.example.yaml`
- Updated `scripts/validate_examples.py` to validate all matching sync audit record examples.

### Notes

v0.2 applies the v0.1 audit ruler to concrete cases.

The goal is to demonstrate conservative classification discipline before adding structural fingerprint logic in v0.3.

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
