# Technical Data Room Index Template

Status: public validation template. No payment, real-data, legal/tax/M&A, compliance/security, or outcome claims authorized.

Use fake/demo data only in this public validation package.

## 1. Company technical snapshot

- Product name:
- One-sentence product function:
- Primary user types:
- Hosting model:
- Critical third-party services:
- Environments: production / staging / local
- Current technical owner:

## 2. Architecture overview

- System diagram placeholder:
- Main app components:
- Data stores:
- Background jobs / queues:
- Authentication / authorization model:
- External APIs:
- Known architectural constraints:

## 3. Repository inventory

| Repo | Purpose | Visibility | Primary stack | Last active | CI status | Notes |
|---|---|---|---|---|---|---|
| demo/frontend | UI | private demo | TypeScript | YYYY-MM-DD | unknown | example row |

## 4. Dependency and SBOM evidence

- Package manager(s):
- Lockfiles present:
- SBOM generated: yes/no/unknown
- Vulnerability scan evidence: yes/no/unknown
- License inventory: yes/no/unknown
- Known unsupported/end-of-life dependencies:
- Evidence folder path/name:

## 5. Deployment and operations

- Hosting provider:
- Deployment method:
- Rollback method:
- Backup location/type:
- Monitoring/alerting:
- Incident log location:
- Runbook location:
- Recovery-time unknowns:

## 6. Access and roles

| System | Admins | Service accounts | MFA status | Offboarding notes |
|---|---|---|---|---|
| demo hosting | unknown | unknown | unknown | verify before diligence |

## 7. Security and incident history prompts

This section is a prompt list, not a claim.

- Any known breaches or incidents?
- Any unresolved vulnerability reports?
- Any customer data exposure events?
- Any privileged shared accounts?
- Any secrets in repos or build logs?
- Any missing MFA on critical services?
- Any unsupported dependencies?

Allowed answer styles:
- known / unknown / not applicable;
- evidence path;
- owner;
- date last checked.

## 8. Buyer FAQ starter

- How is the product deployed?
- What would break if the founder left tomorrow?
- Which systems need credential transfer?
- What data is stored and where?
- What is the highest-risk technical debt?
- What must be checked before closing?

## 9. Red flags / unknowns list

| Item | Severity | Why it matters | Evidence needed | Owner |
|---|---|---|---|---|
| Missing rollback test | medium | buyer wants operability proof | runbook / test date | TBD |

## 10. Boundary

This index does not provide legal, tax, valuation, investment, M&A, security, compliance, certification, ROI, sale-readiness, or outcome advice. It is a technical organization checklist only.
