# MMSP Functional Specification — v0.1

**State:** Draft for founder + community review. **Baseline:** 2025 book B0. **Domain:** manitoumysteryschool.com.

## Mission
Offer a sovereign, learner-directed, community-supported school of study, practice, ethical action, and service. The student's **Journey** is the system's central object. The 13 Temples are a map, not a compulsory major or linear ladder.

## Actors
Visitor, Seeker, Student, Traveler, Guide, Dean, Deacon, Board Reviewer, Editor, Administrator, and Institutional Steward. The system must not present fictional or unverified people as appointed staff.

## Requirements
| ID | Priority | Capability / acceptance intent |
|---|---|---|
| JRN-001 | P0 | Welcome visitors with clear, concise, non-coercive language. |
| JRN-002 | P0 | Ask about the seeker's intent; suggest relevant Temples and next actions, not an authoritative spiritual diagnosis. |
| JRN-003 | P0 | Browse 13 Temples with traceable 2025 source descriptions. |
| JRN-004 | P0 | Create a learner-authored Journey: intention, inquiries, chosen Temples and activities. |
| JRN-005 | P0 | Edit/reorder Journey without destroying prior records. |
| JRN-006 | P0 | Study planning: activities, deadlines optional, progress markers. |
| JRN-007 | P0 | Add learner-controlled journal / portfolio evidence; no automatic publication. |
| JRN-008 | P0 | Distinguish demo data from live records and recognition. |
| JRN-009 | P0 | Accessible, keyboard-operable responsive browser experience. |
| JRN-010 | P0 | Version and provenance for curriculum, learner records, and review outcomes. |
| JRN-011 | P1 | Verified profiles, qualifications and availability of guides, Deans, Deacons. |
| JRN-012 | P1 | Opt-in circles, events and independent community affiliations. |
| JRN-013 | P1 | Private mentorship requests and consent-limited sharing. |
| JRN-014 | P1 | Submit selected portfolio items to a Community Board of Review. |
| JRN-015 | P1 | Immutable reviewed snapshot, reviewer conflict disclosures, objective rubrics and appeal path. |
| JRN-016 | P1 | Record demonstrated skills and feedback; no AI verdict of enlightenment. |
| JRN-017 | P1 | Controlled approval and publication of community-contributed learning resources. |
| JRN-018 | P1 | Student export/deletion rights, retention and access controls. |
| JRN-019 | P1 | Role-based institution governance and auditable approvals. |
| JRN-020 | P2 | Accredited-pathway evidence export, only after authorization review. |
| JRN-021 | P2 | Verified completion records; no accreditation claim absent proper approval. |
| JRN-022 | P2 | AI guide grounded in approved texts, able to say 'I don't know' and connect to humans. |

## Data model
`Journey {id, owner, intention, inquiries[], selectedTempleIds[], activities[], evidence[], revisions[], status}`.
`Temple {id, title, theme, sources[], practices[], outcomes[]}`.
`Guide {id, verifiedStatus, roles[], qualifications[], scopeOfPractice, consentToContact}`.
`Review {id, journeyId, evidenceSnapshot, panel[], rubrics[], decision, explanation, appealStatus}`.
`Credential {id, issuer, authority, recipient, competencies[], issuedAt, verification}` — deferred.

## Journey lifecycle
Discover → Intend → Explore → Study → Practice → Reflect → Contribute → Request Review → Demonstrate → Receive Feedback/Recognition → Return. Steps are repeatable; a review is optional; no forced spirituality ranking.

## Quality and safety
Separate documented scientific findings from spiritual doctrine and symbolic interpretation; protect restricted cultural knowledge; no medical diagnosis or treatment promises. Respect student privacy, do not publish journals by default, obtain permission before sharing personal records. Real accounts require authentication, encryption, authorization, backups, audit log, retention policy, and safeguarding procedures.

## MVP boundary
The current prototype is synthetic and local-browser only. It may demonstrate review and graduation mechanics, but cannot certify learning, issue authentic credentials, schedule real faculty, or store confidential data in a hosted institution.

## Gate acceptance
G0: confirm source and founding authority. G1: owner-approved FS. G2: design & threats. G3: working beta. G4: QA, security, accessibility, privacy, and curriculum approvals. G5: founder Go and public launch.
