# ANONYMOUS COMPOSITES — template and guidance

Purpose
-------
Define how to record high-level, non-identifying composite attributes for speakers. These composites are intentionally broad buckets (not PII) and are used to support aggregate analysis while protecting identity.

Composites (recommended fields)
- composite_gender: one of {male,female,non-binary,non-disclosed}
- composite_age_range: buckets such as {under_18,18-24,25-34,35-44,45-54,55-64,65_plus,non-disclosed}
- composite_status: project-dependent bucket (examples below)

Examples for `composite_status` buckets (choose project-appropriate names)
- status: current_substance_use
- status: past_substance_use
- status: housing_insecure
- status: unemployed
- status: employed
- status: non-disclosed

CSV header example
------------------
id,source_file,date_collected,speaker_id,composite_gender,composite_age_range,composite_status,offensive_language_flag,owner_narrative_flag,notes

Sample row
---------
uuid-0000,docs/archive/notes/2025-10-30-gpt103025.md,2025-10-30,speaker_001,non-disclosed,45-54,status:past_substance_use,TRUE,TRUE,"Speaker reclaims label 'Kaznak' — preserve raw_text; sanitize for public releases."

Notes on aggregation and privacy
--------------------------------
- Choose buckets wide enough to prevent re-identification but fine-grained enough for analysis.
- Avoid combining composites that together could identify a person in small populations (e.g., very narrow age range + rare status + small location). If in doubt, widen the bucket or use non-disclosed.

Implementation tip
------------------
- Use this CSV/JSON structure for ingestion. Keep a separate `raw_text` store (file path or blob storage) and reference it by `id` in the composite CSV.
- Keep an internal access policy for raw_text: only approved analysts can read raw_text, and access must be logged.
