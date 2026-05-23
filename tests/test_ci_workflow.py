from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / '.github' / 'workflows' / 'validate.yml'


class CiWorkflowTests(unittest.TestCase):
    def test_validate_workflow_runs_public_safety_gate(self):
        text = WORKFLOW.read_text(encoding='utf-8')
        self.assertIn('python3 -m unittest tests/test_public_package.py -v', text)
        self.assertIn('python3 scripts/validate_public_package.py', text)
        self.assertIn('python3 -m py_compile scripts/validate_public_package.py tests/test_public_package.py', text)
        self.assertIn('permissions:', text)
        self.assertIn('contents: read', text)
        self.assertIn('persist-credentials: false', text)


if __name__ == '__main__':
    unittest.main()
