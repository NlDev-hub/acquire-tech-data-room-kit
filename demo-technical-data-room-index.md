# Demo Technical Data Room Index — Fictional Micro-SaaS

Status: public synthetic sample.
external_action_authorized=low_risk_niko_only_public_validation_only
real_company_data_authorized=false

## Fictional context

Product: DemoDesk, a fictional appointment reminder SaaS.
Use: demonstration only. No real company data.

## Technical snapshot

- Product function: sends appointment reminder emails for fictional service teams.
- Stack: TypeScript frontend, Python API, PostgreSQL, background worker.
- Hosting: fictional container host.
- Critical third-party services: demo email provider, demo billing placeholder.
- Current technical owner: unknown in sample.

## Repository inventory

| Repo | Purpose | Visibility | Primary stack | Last active | CI status | Notes |
|---|---|---|---|---|---|---|
| demo/frontend | user dashboard | synthetic | TypeScript | 2026-05-01 | unknown | sample only |
| demo/api | API and worker | synthetic | Python | 2026-05-01 | unknown | sample only |

## Evidence folder map

- `/architecture/overview.md` — system sketch and component notes.
- `/repos/repo-inventory.csv` — repository list.
- `/dependencies/sbom.json` — optional generated SBOM if available.
- `/operations/deploy-runbook.md` — deployment and rollback steps.
- `/access/admin-roles.md` — access inventory.
- `/security/incident-history.md` — known/unknown incident notes.
- `/buyer-faq/technical-faq.md` — buyer FAQ draft.

## Red flags / unknowns

| Item | Severity | Why it matters | Evidence needed | Owner |
|---|---|---|---|---|
| Rollback not recently tested | medium | buyer needs operability confidence | dated rollback test note | technical owner |
| Admin role inventory incomplete | high | transfer risk | service-by-service admin list | founder |
| Dependency scan missing | medium | diligence gap | SBOM or dependency scan output | maintainer |

## Approval boundary

No payment, checkout, invoice, contract, refund, support, real company data, legal, tax, valuation, investment, M&A, security, compliance, certification, ROI, sale-readiness, or outcome claim. This is a public synthetic validation sample only.
