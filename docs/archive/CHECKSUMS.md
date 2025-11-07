# TEC TGCR Checksums (SHA256)

**Generated:** 2025-10-17T18:30:00-04:00
**Commit:** 40d606859ea5f39d7e3aa0d26f20c6be014bd9bf
**Branch:** main
**Status:** dirty (uncommitted changes present)

This file contains SHA256 fingerprints for key artifacts, documentation, and source files. Use these hashes to verify file integrity and detect tampering.

## How to Verify

### Single file

```powershell
Get-FileHash -Algorithm SHA256 <filepath>
```

### All files (automated)

```powershell
pwsh -NoProfile -ExecutionPolicy Bypass -File scripts/verify_checksums.ps1
```

---

## Documentation

| File | SHA256 |
|------|--------|
| `docs/AGENT_AIRTH.md` | `7611BF9266BAF0FD59F380A5BF7FE1EA90A2CBE08224193536C4C7581285354E` |
| `docs/DESIGN_SPIN_MODEL.md` | `DAE1BE835B77925C8652CDA59CEC5BD2110264928FA42A8FB082519DD8C87BBF` |
| `docs/WORDPRESS_WPCOM_OPS.md` | `6991E63C162CD8F221E9B59A993BB4C3D8C5C3AA63F039259FC940FA0025ECFC` |
| `docs/examples/spinning_svg.html` | `0303E4B05C443153D3FA6259D9810596FC1850A86B39D3A26E11B55B2CE6A63E` |

## Artifacts (Built)

| File | SHA256 |
|------|--------|
| `exports/wp-plugin/tec-tgcr-1.0.1.zip` | `3F3F399D811BEA06A045E324DD0436CC77BE6C68F60AC3627158039C21F8FC30` |

## Source Code (Core)

| File | SHA256 |
|------|--------|
| `apps/wordpress/tec-tgcr/tec-tgcr.php` | `A2C378CAA892645F2C479A4146E34C0DA9A1C4BEBF2EFC773EEBA591E36CBEAC` |
| `src/tec_tgcr/__init__.py` | `F17E43B8C4D879CED5A14E9CDF03D139280416FDC3E2B09C658D30C1280736BD` |
| `src/tec_tgcr/cli.py` | `9407CAE42B38982EC1B782DCE3CE3E37E89049D8B48C0D3B8F65767B75A71794` |
| `src/tec_tgcr/session.py` | `224AB32D78D6C8A2FC48E562C53E4EB712F29E61AEE5AFD338EB91F8617AB923` |

## Configuration & Data

| File | SHA256 |
|------|--------|
| `config/agent.yml` | `D718772520B99658BC960DDF26ACCBEC5D5C41DA4877FB33E9BAA348F01CBD2A` |
| `data/knowledge_map.yml` | `5F51CAE3A7C913AA95FF3B941C3E8E4BA6D4236457D0C3811B6C357026476B41` |

---

## Notes

- **Dirty flag:** Working tree has uncommitted changes; hashes reflect the current file state, not the last commit.
- **Plugin artifact:** Contains embedded `build-info.json` with commit, timestamp, and main file hash.
- **Verification script:** Run `scripts/verify_checksums.ps1` to automatically compare current file hashes against this manifest.

## Updating This File

Regenerate checksums after any code change:

```powershell
pwsh -NoProfile -ExecutionPolicy Bypass -File scripts/generate_checksums.ps1
```

---

*Where gravity curves spacetime, resonance curves meaning-space.*
