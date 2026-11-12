# MMSP Journey Demo

Open `index.html` in a browser to explore the local-only learning experience.

Workflow: intention → 13 Temple selection → plan activities → private reflections → mock review snapshot → non-credential Return.

- No dependencies, network calls, user accounts or external services.
- Saved records use browser `localStorage` and can be erased or exported as JSON.
- **Do not use real sensitive learner data.** Browser storage is not secure enough for production.
- No genuine faculty appointments, accreditation or academic awards are implied.
- Temple names follow the detailed chapters of *Manitou Mystery School 2025* (B0), pending resolution of summary-table inconsistencies.

## QA
`node --test site/tests/static.test.mjs` from repo root. Also perform manual keyboard and mobile-browser checks.

## Next
A real system needs authenticated identities, access control, encryption, review panels, controlled content, multi-user services, backup, and a privacy/safeguarding program.
