from pathlib import Path
import json
import sys

import yaml
from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
EXAMPLES_DIR = ROOT / "examples"

VALIDATION_TARGETS = [
    {
        "name": "Synchronization Audit Record",
        "schema": ROOT / "schemas" / "sync-audit-record.schema.json",
        "pattern": "sync-audit-record*.yaml",
    },
    {
        "name": "Structure Fingerprint",
        "schema": ROOT / "schemas" / "structure-fingerprint.schema.json",
        "pattern": "structure-fingerprint*.yaml",
    },
    {
        "name": "Defense Court Bridge",
        "schema": ROOT / "schemas" / "defense-court-bridge.schema.json",
        "pattern": "defense-court-bridge*.yaml",
    },
]


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def find_example_files(pattern: str):
    return sorted(EXAMPLES_DIR.glob(pattern))


def validate_example(name: str, schema_path: Path, example_path: Path):
    print(f"[validate] {name}")
    print(f"  schema : {schema_path.relative_to(ROOT)}")
    print(f"  example: {example_path.relative_to(ROOT)}")

    schema = load_json(schema_path)
    example = load_yaml(example_path)

    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(example), key=lambda e: e.path)

    if errors:
        print(f"[error] {example_path.name} validation failed")
        for error in errors:
            path = ".".join(str(part) for part in error.path) or "<root>"
            print(f"  - path: {path}")
            print(f"    message: {error.message}")
        return False

    print(f"[ok] {example_path.name} is valid")
    return True


def validate_target(target):
    schema_path = target["schema"]
    example_files = find_example_files(target["pattern"])

    if not schema_path.exists():
        print(f"[error] Schema not found: {schema_path.relative_to(ROOT)}")
        return False

    if not example_files:
        print(f"[error] No example files found for pattern: {target['pattern']}")
        return False

    all_ok = True

    for example_path in example_files:
        if not validate_example(target["name"], schema_path, example_path):
            all_ok = False

    return all_ok


def main():
    all_ok = True

    for target in VALIDATION_TARGETS:
        if not validate_target(target):
            all_ok = False

    if not all_ok:
        sys.exit(1)


if __name__ == "__main__":
    main()
