"""Read-only integrity check for the Arpan_UI reference snapshot."""
import hashlib
import json
from pathlib import Path


def main():
    root = Path(__file__).resolve().parent
    manifest = json.loads((root / "SOURCE-MANIFEST.json").read_text())
    errors = []
    for relative, record in manifest["sourceFiles"].items():
        path = (root / relative).resolve()
        if not path.is_relative_to(root) or not path.is_file():
            errors.append(f"Missing or invalid path: {relative}")
            continue
        data = path.read_bytes()
        if len(data) != record["size"] or hashlib.sha256(data).hexdigest() != record["sha256"]:
            errors.append(f"Source changed: {relative}")
    for relative in [
        "START_HERE.md", "CLAUDE_START_PROMPT.md", "HANDOFF.md",
        "reference/Design-Thinking/docs/plans/ui-implementation-plan.md",
        "reference/Design-Thinking/docs/plans/ui-team-local-validation.md",
        "reference/Design-Thinking/data-model/cases/analog-modulation-odia.json",
        "reference/Design-Thinking/design-system/project/components/bundle.js",
        "demos/Kiki-journey-walkthrough.html",
    ]:
        if not (root / relative).is_file():
            errors.append(f"Required resource absent: {relative}")
    result = {
        "status": "FAIL" if errors else "PASS",
        "verified_source_files": len(manifest["sourceFiles"]),
        "source_commit": manifest["sourceCommit"],
        "documented_template_links": len(manifest["unresolvedReferenceLinks"]),
        "errors": errors,
    }
    print(json.dumps(result, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
