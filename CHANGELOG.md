# Changelog

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
