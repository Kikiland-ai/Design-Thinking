#!/usr/bin/env python3
"""Export a pinned, offline Kiki backend context + BB8 starter (no repo mutation)."""

import argparse
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import re
import subprocess
import sys
import tarfile
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / 'tools' / 'backend-starter'
PREFIXES = ('docs/', 'data-model/', 'design-system/', 'prototype/')
ROOT_FILES = {
    'README.md', 'HANDOVER.md', 'AI_Builder_Cup_Product_Vision.docx',
    'AI_Builder_Cup_Technical_Architecture.docx', 'Audio Transcript.txt',
}
sys.dont_write_bytecode = True
REQUIRED = {
    'docs/prototypes/backend-prototype-directions.md',
    'docs/plans/backend-prototype-handoff.md',
    'docs/ux/student-journey-odia-ece.md',
    'docs/ux/experiment-recommendation-simulink.md',
    'data-model/types/content.ts', 'data-model/types/intake.ts',
    'data-model/types/learner.ts',
}


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encoded(value):
    return (json.dumps(value, indent=2, sort_keys=True) + '\n').encode()


def build(revision):
    if not re.fullmatch(r'[0-9a-f]{40}', revision):
        raise ValueError('Use a full, pinned 40-character source commit SHA')
    resolved = subprocess.check_output(
        ['git', 'rev-parse', '--verify', revision + '^{commit}'], cwd=ROOT, text=True
    ).strip()
    if resolved != revision:
        raise ValueError('Source must identify a commit directly')
    archive = subprocess.check_output(['git', 'archive', revision], cwd=ROOT)
    with tempfile.TemporaryDirectory(prefix='kiki-source-') as folder:
        checkout = Path(folder)
        with tarfile.open(fileobj=io.BytesIO(archive)) as source:
            members = source.getmembers()
            for member in members:
                path = Path(member.name)
                if path.is_absolute() or '..' in path.parts or not (member.isfile() or member.isdir()):
                    raise ValueError('Source archive contains an unsupported path or file type')
            source.extractall(checkout, filter='data')
        spec = importlib.util.spec_from_file_location(
            'pinned_bb8_bootstrap', checkout / 'bb8/provisioning/bootstrap.py'
        )
        bootstrap = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(bootstrap)
        files = bootstrap.bundle(root=checkout)
        files['.bb8-bootstrap.json'] = encoded({
            'schema_version': 1, 'status': 'complete', 'plugin': 'bb8',
            'plugin_version': '0.2.1', 'source_revision': revision,
            'bundle_sha256': bootstrap.bundle_digest(files),
        })
        snapshot = {}
        for path in sorted(checkout.rglob('*')):
            if not path.is_file():
                continue
            name = path.relative_to(checkout).as_posix()
            if name in ROOT_FILES or name.startswith(PREFIXES):
                if path.name.startswith('.env') or path.suffix in {'.pem', '.key', '.p12', '.pfx'}:
                    raise ValueError('Unexpected credential-shaped file in product context')
                raw = path.read_bytes()
                files['context/design-thinking/' + name] = raw
                snapshot[name] = {'bytes': len(raw), 'sha256': sha(raw)}
        missing = REQUIRED - snapshot.keys()
        if missing:
            raise ValueError('Source revision lacks required context: ' + ', '.join(sorted(missing)))
        files['context/design-thinking/SOURCE.json'] = encoded({
            'schema_version': 1,
            'repository': 'https://github.com/Kikiland-ai/Design-Thinking',
            'source_revision': revision,
            'files': snapshot,
        })
        for path in sorted(TEMPLATES.rglob('*')):
            if path.is_symlink():
                raise ValueError('Symlinked starter template')
            if path.is_file():
                name = path.relative_to(TEMPLATES).as_posix()
                if name == 'AGENTS.backend.md':
                    files['AGENTS.md'] += b'\n' + path.read_bytes()
                else:
                    if name in files:
                        raise ValueError('Template conflicts with generated starter: ' + name)
                    files[name] = path.read_bytes()
        if not TEMPLATES.is_dir() or 'SETUP.md' not in files:
            raise ValueError('Starter templates are unavailable')
        # This records initial bundle contents, not a permanent lock on backend implementation.
        files['STARTER-MANIFEST.json'] = encoded({
            'schema_version': 1, 'source_revision': revision,
            'generator_sha256': sha(Path(__file__).read_bytes()),
            'files': {name: {'bytes': len(raw), 'sha256': sha(raw)}
                      for name, raw in sorted(files.items())},
        })
        return files


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-revision', required=True)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    try:
        if args.output.exists():
            raise ValueError('Output already exists; refusing to overwrite it')
        files = build(args.source_revision)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(args.output, 'x', compression=zipfile.ZIP_DEFLATED) as output:
            for name, raw in sorted(files.items()):
                entry = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
                entry.compress_type = zipfile.ZIP_DEFLATED
                entry.external_attr = 0o100644 << 16
                output.writestr(entry, raw)
        print(json.dumps({'status': 'packaged', 'source_revision': args.source_revision,
                          'files': len(files), 'archive_sha256': sha(args.output.read_bytes()),
                          'output': str(args.output)}))
        return 0
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        print(str(error))
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
