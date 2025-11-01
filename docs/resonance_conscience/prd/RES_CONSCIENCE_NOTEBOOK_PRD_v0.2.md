# Resonance Conscience Notebook — PRD v0.2 (Implementation Blueprint)

*A TEC Instrument: A Contextualized Cognitive Journal with Music‑Mediated Resonance Dynamics*

---

## 0) Conceptual Apex (Reaffirmed)

**Thesis.** Writing is an empirical affirmation of existence. The instrument quantifies the transformation of cognition into durable meaning by capturing temporal vitality (**φᵗ**), structural coherence (**ψʳ**), and contextual resonance (**Φᴱ**). Musical data provides an emotional calibration layer linking physiology, mood, and narrative.

**Why this matters now.** Reliable self‑observation tools are scarce; current AI notebooks omit provenance, determinism, and affective grounding. This notebook unifies **reproducible analytics** with **music‑mediated context**, enabling verifiable introspection and cross‑session continuity.

---

## Definition of Completion (AIRTH Gate)

* **Reproducibility:** Deterministic ingestion → retrieval → synthesis with logged seeds/checkpoints.
* **Integrity:** Cryptographic signatures for runs; schema migration rollbacks.
* **Security:** Local‑first encryption, key rotation, audit trails.
* **Performance:** SUS > 80; P95 retrieval < 2s @ 10k+ notes; ψʳ integrity > 99.9% (index parity checks).
* **Affective Validity:** Statistically significant mood‑stabilization correlation (p < 0.05).

---

## 1) Core Functional Objectives (v0.2)

1. **Cognitive Capture:** Frictionless multimodal input (text/audio/image).
2. **Audio Recording + Transcription:** Built‑in recorder; primary ASR via **Whisper/Faster‑Whisper** with fallback models.
3. **Contextual Integration:** Semantic mapping across entries, tags, relations, and **music context** (tempo, key, valence, energy).
4. **Resonance Synthesis:** Automated summaries combining journal + audio + track metadata.
5. **Reflexive Retrieval:** Queries like *“When did music stabilize my mood most effectively?”*
6. **Continuity Preservation:** Offline operation, autosave redundancy, immutable version history.
7. **Legal Lyrics Lookup:** Licensed APIs (no scraping) with cached excerpts + citation and provenance.

---

## 2) Minimum Viable Configuration (expanded)

* **Editor:** Markdown with hierarchical tags, entity linking, checklists, inline audio blocks.
* **Music Module:** Spotify sync (tracks, features, playback history). Optional Apple Music adapter.
* **ASR Module:** On‑device recording; Whisper/Faster‑Whisper transcription; diarization (optional WhisperX/VAD).
* **Analytical Panels:** NotebookLM‑style hypothesis space; cross‑domain correlation views.
* **Deterministic LLM:** Manifest‑logged prompts/seeds for summaries and Q&A.

---

## 3) System Architecture

**Flow:** acquisition → local data lake (SQLite + Parquet) & vector index → summarization → analytics → export. Optional encrypted cloud sync.

**Stack:**

* **UI:** Tauri (Rust) or Electron/PWA (Windows‑first). Tailwind/React for views.
* **DB:** SQLite (WAL), DuckDB/Parquet for analytics; **FAISS‑lite** or **Qdrant (embedded)** for vectors.
* **ASR:** whisper.cpp / Faster‑Whisper GPU if available.
* **Model Orchestration:** OpenAI / Anthropic / xAI; **Ollama** for local LLMs; **Unsloth** for efficient fine‑tuning.
* **RAG:** Local documents + transcripts + summaries with retrieval pipelines (rerank on device where possible).
* **Crypto:** libsodium / age; per‑run signing.

---

## 4) Data Schema (ψʳ) — extended

```yaml
Note: { id, created_at, updated_at, title?, body_md, tags[], mood?, privacy, version }
Track: { id, provider, title, artist, album, tempo?, key?, energy?, valence?, uri }
Audio: { id, note_id?, path, duration_s, samplerate, channels, transcription_id?, diarization?, checksum }
Transcript: { id, audio_id, model, lang, text_md, words_json?, confidence, seed?, created_at }
Lyrics: { id, track_id, provider, excerpt_md, sync_lrc?, license_ref, checksum }
Link: { id, from_id, to_id, type, weight }
Run: { id, seed, model, prompt_hash, inputs_hash, outputs_hash, created_at, signer }
Summary: { id, note_ids[], run_id, type: ['daily','weekly','query'], text_md, citations[] }
Settings: { id, key, value_json, updated_at }
```

**Indexes:** full‑text on `Note.body_md` + `Transcript.text_md`; vector embeddings for Notes/Transcripts/Lyrics.

---

## 5) AI Agency Suite

* **Resonance Engine (R):** Fuse journal embeddings + track features + affect logs → coherence score/time.
* **Music Sentinel (φᵗ ↔ Φᴱ):** Detects spectral patterns, predicts mood response windows; suggests playlists.
* **Journal Guardian (ψʳ):** Flags uncertainty, generates counterfactual prompts, ensures coverage of blind spots.

---

## 6) Privacy, Security, Provenance

* **Local‑first:** Data stays on device unless explicit opt‑in.
* **Encryption:** AES‑GCM for storage; key isolation, rotation policy; OS keyring integration.
* **Provenance:** Each generated artifact binds to a **signed Run Manifest**; export includes signatures and checksums.

---

## 7) Evaluation Metrics

* **Engagement:** ≥ 60% daily journaling.
* **Latency:** < 2s P95 retrieval on 10k+ notes.
* **Affective Outcome:** Mood stabilization correlation p < 0.05.
* **Transcription QoS:** WER < 12% (general), < 6% (clean speech) with chosen model tier.

---

## 8) Roadmap & Protocols

**Phase I (M0‑M1):** Core shell, autosave, tagging, Spotify sync, audio capture + Whisper.
**Phase II (M1‑M2):** Summarization, run manifests, export pipeline, basic RAG Q&A.
**Phase III (M2‑M3):** Music Sentinel, affect index, Journal Guardian, licensed lyrics.

**Dev Protocols:**

* Secrets in `secrets-local/`; manifests in `runs/<timestamp>/`.
* Pre‑commit hooks: ruff/black (py), eslint/biome (js), markdownlint.
* Unit tests: pytest + Playwright; target ≥ 85% coverage on core libs.

---

## 9) Implementation Blueprint (Windows‑first)

### 9.1 Environment Bootstrap (PowerShell 7)

```powershell
# Create workspace
mkdir TEC_Resonance; cd TEC_Resonance
python -m venv .venv; .\.venv\Scripts\Activate.ps1
pip install --upgrade pip

# Core Python deps
pip install fastapi uvicorn[standard] pydantic[dotenv] sqlalchemy duckdb pandas
pip install faiss-cpu sentence-transformers qdrant-client

# ASR
pip install faster-whisper==1.*  # GPU-optional
# optional: whisperx for diarization
pip install git+https://github.com/m-bain/whisperx.git

# Desktop shell
npm create vite@latest app -- --template react-ts
cd app; npm i tailwindcss postcss autoprefixer chart.js lucide-react
npx tailwindcss init -p
```

### 9.2 Local Models (Ollama) & Fine‑tuning (Unsloth)

```powershell
# Ollama
winget install Ollama.Ollama
ollama pull llama3.1:8b  # baseline local model

# Unsloth (CUDA recommended)
pip install unsloth
# fine-tune small instruct model on anonymized journal patterns (opt-in only)
```

### 9.3 RAG Mini‑Stack

* Embed: `sentence-transformers` (e5‑small / all‑MiniLM) → FAISS/Qdrant.
* Retrieve top‑k across Notes/Transcripts/Lyrics; rerank (local cross‑encoder) before LLM answer.

### 9.4 ASR Pipeline

1. Record WAV (48kHz) in app →
2. Queue to ASR worker → Faster‑Whisper (or whisper.cpp if CPU‑only) →
3. (Optional) WhisperX align + diarize →
4. Persist `Audio` + `Transcript` rows; link to `Note` by timestamp.

### 9.5 Music & Lyrics (Legal)

* **Spotify Web API:** playback history, audio features (tempo/key/energy/valence).
* **Lyrics Providers (licensed):**

  * **Musixmatch API** (commercial & attribution), or
  * **Genius API** (metadata only; respect TOS; no unauthorized scraping).
* Cache **excerpts** + license reference in `Lyrics.license_ref`; store full text **only if license permits**.

### 9.6 LLM Orchestration

* Provider adapters: OpenAI / Anthropic / xAI; **local fallback via Ollama**.
* Determinism: fixed seeds where supported; log `Run` manifest (model, prompt hash, inputs/outputs hashes, signer).

### 9.7 Security

* Encrypt DB at rest; field‑level encryption for sensitive notes.
* Sign exports with age/sig; verify on import.
* Audit log for external calls (provider, scope, token alias).

---

## 10) UX Flows (Golden Paths)

1. **Capture → Transcribe → Tag:** User records a thought, Whisper transcribes, user tags mood + links Spotify track.
2. **Daily Synthesis:** At day’s end, Resonance Engine produces a signed summary with citations to entries, tracks, and transcripts.
3. **Reflexive Query:** *“Show weeks where tempo 80–110 BPM correlated with reduced ADR and higher OXY tone.”*

---

## 11) Test Plan (Airth)

* **Unit:** schema ops, embeddings, ASR wrappers, Spotify adapter.
* **Integration:** end‑to‑end capture → summary; RAG retrieval sanity.
* **Determinism:** same seed/prompt → identical summary hash.
* **Affective Validation:** A/B playlist recommendations; record mood deltas.

---

## 12) Risk & Mitigation

* **Licensing risk (lyrics):** Use provider SDKs; store excerpts + IDs; no scraping.
* **Privacy:** Local‑first; redact PII in fine‑tune datasets; opt‑in only.
* **Vendor drift:** Multi‑provider adapters + local Ollama fallback.
* **Compute limits:** Graceful degradation (CPU ASR, smaller models).

---

## 13) For Codex (STEP‑BY‑STEP — what/why/how)

**What we are building:** A local‑first, cryptographically‑verifiable journal that merges writing, audio, and music analytics to model personal resonance.

**Why it matters:** It enables trustworthy self‑measurement (not surveillance), turning media habits into actionable affective insights while preserving privacy and provenance.

**How we proceed (sequenced):**

1. **Repo Init & CI:** Scaffold monorepo; add lint/test workflows; secrets template.
2. **Schema & Migrations:** Implement SQLite models; write initial migrations.
3. **ASR Service:** Wire audio capture → Faster‑Whisper; persist `Audio`/`Transcript`.
4. **Spotify Adapter:** OAuth, playback history, audio features; nightly sync job.
5. **Embedding & Index:** Build embedding service; FAISS/Qdrant; backfill existing notes.
6. **LLM Orchestrator:** Provider adapters (OpenAI/Anthropic/xAI + Ollama); `Run` manifests.
7. **Summarizer:** Daily/weekly synthesis with citations; deterministic seeds.
8. **RAG Q&A:** Cross‑corpus retrieval; rerank; answer with provenance.
9. **Lyrics Module:** Integrate licensed API; cache excerpts + license refs; UI viewer with attribution.
10. **Security:** Encryption at rest; key mgmt; signed exports/imports.
11. **Analytics Panels:** Correlate mood vs. track features; affective bubble chart (DOP/OXY/ADR).
12. **Packaging:** Tauri/Electron build; auto‑update; crash reporting (local redact).

**Done =** All steps shipped with passing tests, signed manifests, SUS ≥ 80, P95 < 2s.

---

## 14) Backlog (Prioritized)

1. Audio recorder UI + ASR worker (GPU/CPU).
2. Spotify sync + feature cache.
3. Deterministic summarizer + Run manifests.
4. Vector index + RAG.
5. Lyrics provider integration (Musixmatch first).
6. Security hardening (encryption, signing, audit).
7. Affective analytics (DOP/OXY/ADR).
8. Local LLM via Ollama; Unsloth fine‑tune pipeline.

---

## 15) Provenance & Licensing

* Source of truth: local signed manifests; exports include checksums.
* Respect provider TOS; include attribution in UI; no unauthorized scraping.

**Status:** v0.2 — ready for decomposition into tickets and prototype implementation. Project kickoff recommended.
