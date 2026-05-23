from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / 'scripts' / 'validate_public_package.py'


def load_validator():
    spec = importlib.util.spec_from_file_location('validate_public_package', VALIDATOR)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class PublicPackageTests(unittest.TestCase):
    def setUp(self):
        self.validator = load_validator()

    def test_public_package_validates(self):
        self.assertEqual(self.validator.validate_package(ROOT), [])

    def test_rejects_real_data_and_overclaim_language(self):
        unsafe = [
            'Upload your real company data for review.',
            'This kit makes your SaaS sale-ready.',
            'This proves sale readiness for buyers.',
            'Guaranteed buyer approval and better valuation.',
            'This will increase valuation.',
            'This provides legal advice and compliance readiness.',
            'Send confidential repository access in an issue.',
            'Contact us for payment.',
        ]
        for text in unsafe:
            with self.subTest(text=text):
                self.assertTrue(self.validator.validate_text(text, 'unsafe-fixture'))

    def test_safe_boundary_language_passes(self):
        safe = [
            'No real company data is requested or included.',
            'Do not paste confidential data, credentials, customer data, or private repository links.',
            'This is not legal advice, tax advice, M&A advice, valuation advice, security certification, compliance readiness, or an outcome guarantee.',
        ]
        for text in safe:
            with self.subTest(text=text):
                self.assertEqual(self.validator.validate_text(text, 'safe-fixture'), [])


if __name__ == '__main__':
    unittest.main()
