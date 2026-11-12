# MMSP Portal QA and Release Gate

**Review date:** 2026-11-12. **Scope:** feature branch integration candidate.
**Prior package evidence:** 12/12 model tests, simulated complete journey, desktop and 390px mobile browsing reported in earlier builder session. Those tests are historical and must run again against this branch.

## Acceptance checks to execute
- User can state intention, explore temples, add activities and evidence, optionally request review, see demo recognition and restart.
- No fake staff appointment / accreditation / signed charter is represented as fact.
- No sensitive data is sent to a network endpoint or shared outside the browser.
- Keyboard access, contrast, screen-reader labels and mobile layout.
- Review evidence snapshot cannot silently change post submission.
- Build output is reproducible; dependency scan; negative tests for invalid user data.

## Blockers to production
No real identity/access control, encrypted private records, verified faculty, external communication, institutional review authority, safeguarding procedures, privacy/legal review, or approved credentials. Production remains HOLD.
