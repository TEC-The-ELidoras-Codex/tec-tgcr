# TEC_TCGR — project documentation

Purpose
-------
This document explains the TEC_TCGR project's documentation rules and schema for archiving and annotating real-world conversational material. The corpus may include intentionally abrasive or offensive language which, for analytic purposes, should be preserved as raw text but clearly labeled and annotated. The aim is documentation and analysis, not endorsement.

Primary principles
------------------
- Preserve speaker narrative ownership: if the speaker uses self-identifiers (for example, invented terms such as "Kaznak") or offensive language intentionally as part of their narrative, preserve those tokens verbatim in the raw text field and mark an ownership flag.
- Flag offensive language and intent: store both the raw text and a separate sanitized or context field. Include an `offensive_language_flag` and `offensive_intent` note (purposeful emphasis, performative, accidental, etc.).
- Apply the ANONYMOUS rule for composites: when storing demographic or contextual composites, only record aggregated, non-identifying categories (see `docs/anonymous_composites.md`).
- Consent & narrative ownership: if material will be published, ensure consent or remove directly identifying data. Preserve user-chosen terms only when there's explicit permission or the data is intended as internal analysis.

Recommended metadata schema (per record)
---------------------------------------
- id: anonymous record id (uuid)
- source_file: path or origin (e.g., `docs/archive/notes/2025-10-30-gpt103025.md`)
- date_collected: ISO date
- speaker_id: anonymized speaker id (e.g., speaker_001)
- raw_text: original verbatim text (preserve punctuation, capitalization, and offensive tokens)
- sanitized_text: optional cleaned version for public consumption (if needed)
- offensive_language_flag: boolean
- offensive_intent: enum {performative, emphasis, insult, reclaimed, neutral}
- owner_narrative_flag: boolean (true if the speaker explicitly claims or reclaims terms)
- composite_gender: anonymized value (see `docs/anonymous_composites.md`)
- composite_age_range: anonymized value
- composite_status: anonymized value (e.g., "status: housing_insecure", or the project's chosen bucket)
- notes: freeform annotator notes (explain why preserved, privacy considerations)

JSON example
------------
{
  "id": "uuid-0000",
  "source_file": "docs/archive/notes/2025-10-30-gpt103025.md",
  "date_collected": "2025-10-30",
  "speaker_id": "speaker_001",
  "raw_text": "I’m a Addict I’m a Junkie I made my own word up... Kaznak...",
  "sanitized_text": "[speaker reclaims term 'Kaznak' to self-identify; content includes strong language]",
  "offensive_language_flag": true,
  "offensive_intent": "reclaimed",
  "owner_narrative_flag": true,
  "composite_gender": "non-disclosed",
  "composite_age_range": "40-50",
  "composite_status": "status: past_substance_use",
  "notes": "Speaker reclaims terms; preserve raw token 'Kaznak' as ownership artifact. Remove direct PII if publishing."
}

Handling offensive language and researcher notes
----------------------------------------------
- Keep raw_text untouched. Never alter the speaker's words in the archival raw field.
- Provide a sanitized_text for public outputs when necessary, with a short rationale in `notes`.
- In annotations, include `offensive_intent` to capture whether language is used for emphasis, provocation, identity reclamation, or otherwise.

Automation
----------
- Store raw transcripts as markdown notes under `docs/archive/notes/` with YAML front matter that defines the `archive.slug` and `archive.basename` keys.
- Run `python scripts/parse_brain_dump.py` to regenerate the JSON/CSV snapshots under `data/archives/transcripts/<slug>/`.
- Update `data/knowledge_map.yml` if you add a new archive slug so the dataset is discoverable.

Search & revisions
------------------
- When searching the corpus, queries should default to sanitized_text unless an analyst explicitly requests raw_text (and documents justification).
- When editing or redacting, record the edit operation in `notes` with timestamp and reason.

Ethics & publication
---------------------
- For publication, prefer aggregated statistics and anonymized composites. Avoid quoting direct raw_text without consent unless redaction or paraphrase is applied and documented.
- If the speaker has invented identity terms (e.g., "Kaznak") and wants them preserved, add an explicit `consent_preserve_label` record to the metadata.

Contact
-------
If you want changes to the schema or additions to the composite buckets, open an issue or request edits in this repo and indicate the rationale.
