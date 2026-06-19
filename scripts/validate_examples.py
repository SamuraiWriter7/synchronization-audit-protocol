from pathlib import Path
import json
import sys

import yaml
from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "sync-audit-record.schema.json"
EXAMPLES_DIR = ROOT / "examples"


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def find_example_files():
    return sorted(EXAMPLES_DIR.glob("sync-audit-record*.yaml"))


def validate_example(schema, example_path: Path):
    print("[validate] Synchronization Audit Record")
    print(f"  schema : {SCHEMA_PATH.relative_to(ROOT)}")
    print(f"  example: {example_path.relative_to(ROOT)}")

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


def main():
    schema = load_json(SCHEMA_PATH)
    example_files = find_example_files()

    if not example_files:
        print("[error] No example files found")
        sys.exit(1)

    all_ok = True

    for example_path in example_files:
        if not validate_example(schema, example_path):
            all_ok = False

    if not all_ok:
        sys.exit(1)


if __name__ == "__main__":
    main()
