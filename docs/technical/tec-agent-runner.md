# TEC Agent Runner (Single-File)

`tec_agent_runner.py` provides a standalone entry point for the TEC-TGCR framework.  
It is designed for quick execution in environments like Codebase, GitHub Codespaces, or local shells where a single command is preferred.

## Features
- Print the LuminAI activation prompt (`prompt`)
- Show the LuminAI term pack (`terms`)
- Run financial anomaly detection (`financial`)
- Process evidence folders (`evidence`)
- Execute integration workflows (`integrate`)

## Usage

```bash
# Show activation prompt
python tec_agent_runner.py prompt

# List LuminAI term pack (pretty JSON)
python tec_agent_runner.py terms --pretty

# Detect anomalies and generate evidence
python tec_agent_runner.py financial --threshold 5.0 --submit

# Process evidence for a case and export CSV
python tec_agent_runner.py evidence --case-id SCHOOL-2024-OCT --export-csv

# Run comprehensive integration status check
python tec_agent_runner.py integrate --mode status
```

Add `-v` or `-vv` to any command to enable info or debug logs.
