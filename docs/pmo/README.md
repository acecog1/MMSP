# MMSP Mission Control — PMO operating baseline v0.1

**Effective proposal:** 2026-11-12. **WBS steward:** PMO. **Source of truth:** GitHub on merged `main`; proposed changes are reviewed through PRs. The 2025 handbook is immutable baseline B0, not an assumed ratified charter.

## Cadence
- Hourly ChatGPT PMO check: inspect live `main`, PRs, issues, workflow status; update WBS/FS/change register through a branch and PR when authorized and beneficial; post a concise briefing.
- On-demand: owner says "MC brief"; run the same reconciliation immediately.
- GitHub Actions PMO lint runs on PR changes to the WBS; recurring schedule can run on `main` after owner-approved merge. A cron run is not proof that the agent executed work.
- No false completion: require linked commit, PR, test report or recorded approval before marking complete.

## Autonomous permission envelope
**Allowed:** Draft/maintain WBS, dependency order, requests, nonbinding architecture documentation, QA reviews, tests, approved prototype implementation on feature branches, and PRs. Advance ready tasks when prerequisites and authority are documented.
**Owner approval required:** merges to `main`, production publication, financial commitments, collecting identifiable student data, issuing credentials, legal status/charter amendments, external outreach, named faculty appointments, security exceptions, and public accreditation claims.
**Never:** fabricate test evidence, silently modify B0, approve one's own independent QA, or change live school records in unreviewed automation.

## Role contracts
PMO — WBS and state reconciliation, critical path and brief. Builder — implementation and FS change proposals. QA — independent release-gate findings. Creative — concise, pure-intent seeker experience. Deans — curriculum and educational evidence. Deacons — community care and participation. Owner — legal and final gates.

## Cycle
1. Read latest repository state, issue/PR evidence and records.
2. Compare to `models/mmsp-wbs-v0.1.csv`, note changes/blockers.
3. Validate dependencies: a task is ready only if its predecessors are complete and authority exists.
4. Perform allowed work where possible; otherwise create a specific work order/PR.
5. Write a briefing: shipped, condition, critical path, assigned next actions, one owner decision if needed.
6. Propose controlled WBS/FS amendments and advance verified state only.

## State semantics
`blocked`: dependency/approval absent. `ready`: unblocked, unassigned or assigned. `in_progress`: evidence of work. `in_review`: PR or review pending. `done`: evidence and acceptance recorded. No invented percent-complete or dates.

## Initial priorities
1. Import B0 book exactly and verify digest.
2. Review PR #1 and establish independent QA.
3. Resolve charter authority and G1 FS baseline.
4. Build secure learner architecture, then real school workflows.
