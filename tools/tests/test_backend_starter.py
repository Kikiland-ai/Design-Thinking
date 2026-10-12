"""Integration checks for source preservation, reproducibility, and import guards."""
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / 'tools/prepare_backend_starter.py'
REVISION = '9a7f369192aaa1be49eeff8535b24d2543be45b8'


class BackendStarterChecks(unittest.TestCase):
    def run_export(self, output, revision=REVISION):
        return subprocess.run(['python', str(SCRIPT), '--source-revision', revision,
                               '--output', str(output)], capture_output=True, text=True)

    def test_pinned_bytes_and_required_assets(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / 'starter.zip'
            result = self.run_export(output)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            with zipfile.ZipFile(output) as z:
                manifest = json.loads(z.read('context/design-thinking/SOURCE.json'))
                self.assertEqual(manifest['source_revision'], REVISION)
                for name, expected in manifest['files'].items():
                    raw = z.read('context/design-thinking/' + name)
                    original = subprocess.check_output(['git', 'show', REVISION + ':' + name], cwd=ROOT)
                    self.assertEqual(raw, original, name)
                    self.assertEqual(hashlib.sha256(raw).hexdigest(), expected['sha256'])
                for name in ['AGENTS.md', 'CONTEXT-BOOT.md', 'SETUP.md', 'context/KNOWN-GAPS.md',
                             '.agents/skills/bb8/SKILL.md', '.claude/skills/bb8/SKILL.md',
                             '.agents/plugins/marketplace.json', 'firebase.json']:
                    self.assertIn(name, z.namelist())
                self.assertNotIn('.github/workflows/bb8-org-bootstrap.yml', z.namelist())
                self.assertNotIn('.env', z.namelist())
                self.assertNotIn('tools/prepare_backend_starter.py', z.namelist())

    def test_reproducible_archive(self):
        with tempfile.TemporaryDirectory() as tmp:
            a, b = Path(tmp) / 'a.zip', Path(tmp) / 'b.zip'
            self.assertEqual(self.run_export(a).returncode, 0)
            self.assertEqual(self.run_export(b).returncode, 0)
            self.assertEqual(a.read_bytes(), b.read_bytes())

    def test_refuses_overwrite_and_unpinned_revision(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / 'existing.zip'
            output.write_bytes(b'preserve me')
            self.assertNotEqual(self.run_export(output).returncode, 0)
            self.assertEqual(output.read_bytes(), b'preserve me')
            new = Path(tmp) / 'new.zip'
            self.assertNotEqual(self.run_export(new, 'main').returncode, 0)
            self.assertFalse(new.exists())

    def test_context_checker_detects_changed_source(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            output = root / 'starter.zip'
            self.assertEqual(self.run_export(output).returncode, 0)
            with zipfile.ZipFile(output) as z:
                z.extractall(root / 'repo')
            checker = root / 'repo/scripts/verify-context.py'
            self.assertEqual(subprocess.run(['python', str(checker)], capture_output=True).returncode, 0)
            target = root / 'repo/context/design-thinking/docs/prototypes/backend-prototype-directions.md'
            target.write_bytes(target.read_bytes() + b'\nchanged\n')
            self.assertNotEqual(subprocess.run(['python', str(checker)], capture_output=True).returncode, 0)


if __name__ == '__main__':
    unittest.main()
