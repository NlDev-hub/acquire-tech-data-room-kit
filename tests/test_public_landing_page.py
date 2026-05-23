from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LANDING = ROOT / 'docs' / 'index.html'


class PublicLandingPageTests(unittest.TestCase):
    def test_landing_page_exists_and_keeps_validation_boundary(self):
        text = LANDING.read_text(encoding='utf-8')
        lower = text.lower().replace('&amp;', '&')
        required = [
            'acquire-ready technical data room kit',
            'would this checklist save you time',
            'no real company data',
            'not legal advice',
            'not tax advice',
            'not m&a advice',
            'not valuation advice',
            'not security certification',
            'no checkout',
            'no payment',
            'no upload',
            'do not post confidential',
            'company-private information',
            'public feedback only',
        ]
        for marker in required:
            with self.subTest(marker=marker):
                self.assertIn(marker, lower)

    def test_landing_page_has_no_runtime_collection_or_payment_surface(self):
        text = LANDING.read_text(encoding='utf-8').lower()
        banned = [
            '<form',
            'fetch(',
            'xmlhttprequest',
            'websocket',
            'localstorage',
            'sessionstorage',
            'indexeddb',
            'buy now',
            'payment link',
            'checkout button',
            'upload your data',
            'paste confidential',
            'sale-ready',
            'increase valuation',
        ]
        for marker in banned:
            with self.subTest(marker=marker):
                self.assertNotIn(marker, text)


if __name__ == '__main__':
    unittest.main()
