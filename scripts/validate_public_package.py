#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

REQUIRED_FILES = [
    'README.md',
    'technical-data-room-index.md',
    'buyer-faq.md',
    'demo-technical-data-room-index.md',
]

REQUIRED_MARKERS = [
    'not legal advice',
    'not tax advice',
    'not M&A advice',
    'not valuation advice',
    'not security certification',
    'compliance readiness',
    'No real company data',
]

UNSAFE_PATTERNS = [
    r'\b(?:upload|paste|send|share|attach|email|dm|message|contact|submit)\b[^\n.;]*(?:real company data|real client data|customer data|confidential|credentials|secrets|private repo|repository access|payment)\b',
    r'\b(?:sale-ready|sale readiness|buyer approved|buyer approval|guaranteed|guarantee|better valuation|increase valuation|improves valuation|deal outcome|ROI)\b',
    r'\b(?:legal|tax|M&A|valuation|investment|security|compliance|certification)\b[^\n.;]*(?:advice|guarantee|guaranteed|certified|ready|approved|increase|improve|claim)\b',
    r'\b(?:buy now|checkout|payment link|invoice|contract|refund|support promise)\b',
]

SAFE_CONTEXT = re.compile(
    r'\b(?:no|not|do not|without|blocked|disclaimer|disclaim|not requested|not included|not used)\b',
    re.IGNORECASE,
)


def _sentence_context(text: str, start: int) -> str:
    left = max(text.rfind('\n', 0, start), text.rfind('.', 0, start), text.rfind(';', 0, start)) + 1
    rights = [p for p in (text.find('\n', start), text.find('.', start), text.find(';', start)) if p != -1]
    right = min(rights) if rights else len(text)
    return text[left:right]


def validate_text(text: str, rel: str) -> list[str]:
    errors: list[str] = []
    for pattern in UNSAFE_PATTERNS:
        for match in re.finditer(pattern, text, flags=re.IGNORECASE):
            if not SAFE_CONTEXT.search(_sentence_context(text, match.start())):
                errors.append(f'{rel}: unsafe language: {match.group(0)}')
                break
    return errors


def validate_package(root: Path | str | None = None) -> list[str]:
    base = Path(root) if root is not None else Path(__file__).resolve().parents[1]
    errors: list[str] = []
    combined = ''
    for rel in REQUIRED_FILES:
        path = base / rel
        if not path.exists():
            errors.append(f'missing required file: {rel}')
            continue
        text = path.read_text(encoding='utf-8')
        combined += '\n' + text
        errors.extend(validate_text(text, rel))
    low = combined.lower()
    for marker in REQUIRED_MARKERS:
        if marker.lower() not in low:
            errors.append(f'missing required marker: {marker}')
    return errors


def main() -> int:
    errors = validate_package()
    if errors:
        print('FAIL: public package validation failed')
        for error in errors:
            print(f'- {error}')
        return 1
    print('PASS: public package validation passed')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
