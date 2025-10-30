"""
Evidence Processing and Timeline Generation Tool

Processes audio/text evidence files to extract timelines,
key events, and generate structured reports for legal/administrative use.
"""

import json
import re
import datetime
from pathlib import Path
from typing import List, Optional
from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)


@dataclass
class TimelineEvent:
    """Represents a timestamped event in evidence"""

    timestamp: Optional[str]
    event_type: str
    description: str
    participants: List[str]
    significance: str  # "critical", "important", "informational"
    source_file: str


@dataclass
class EvidenceReport:
    """Structured report from evidence processing"""

    case_id: str
    timeline: List[TimelineEvent]
    participants: List[str]
    key_issues: List[str]
    summary: str
    source_files: List[str]
    processing_date: str


class EvidenceProcessor:
    """Process evidence files and generate structured reports"""

    def __init__(self, data_path: Optional[Path] = None):
        self.data_path = data_path or Path("data/evidence")
        self.data_path.mkdir(parents=True, exist_ok=True)

    def process_text_file(self, file_path: str) -> List[TimelineEvent]:
        """Process text transcript file to extract timeline events"""
        events = []

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
        except FileNotFoundError:
            logger.error(f"Evidence file not found: {file_path}")
            return []

        # Extract timestamps and events
        file_name = Path(file_path).name

        # Look for time patterns (various formats)
        time_patterns = [
            r"(\d{1,2}:\d{2}(?::\d{2})?\s*(?:AM|PM)?)",  # 10:47 AM, 8:58 AM
            r"(Oct\s+\d{1,2}\s+at\s+\d{1,2}-\d{2}\s*(?:AM|PM))",  # Oct 10 at 10-47 AM
            r"(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2})",  # 2024-10-10 10:47
        ]

        lines = content.split("\n")
        current_timestamp = None

        for i, line in enumerate(lines):
            line = line.strip()
            if not line:
                continue

            # Check for timestamp
            timestamp_found = None
            for pattern in time_patterns:
                match = re.search(pattern, line, re.IGNORECASE)
                if match:
                    timestamp_found = match.group(1)
                    current_timestamp = timestamp_found
                    break

            # Extract participant speech patterns
            speaker_match = re.match(r"^([A-Z][a-zA-Z\s]+):\s*(.+)", line)
            if speaker_match:
                speaker = speaker_match.group(1).strip()
                statement = speaker_match.group(2).strip()

                # Determine significance
                significance = self._analyze_significance(statement)

                events.append(
                    TimelineEvent(
                        timestamp=current_timestamp,
                        event_type="statement",
                        description=f"{speaker}: {statement}",
                        participants=[speaker],
                        significance=significance,
                        source_file=file_name,
                    )
                )

            # Look for action descriptions
            elif any(
                keyword in line.lower()
                for keyword in [
                    "meeting",
                    "called",
                    "arrived",
                    "left",
                    "decided",
                    "agreed",
                    "objected",
                    "requested",
                    "filed",
                    "submitted",
                ]
            ):
                significance = self._analyze_significance(line)
                events.append(
                    TimelineEvent(
                        timestamp=current_timestamp,
                        event_type="action",
                        description=line,
                        participants=self._extract_participants(line),
                        significance=significance,
                        source_file=file_name,
                    )
                )

        return events

    def process_audio_metadata(self, file_path: str) -> List[TimelineEvent]:
        """Process audio file metadata (placeholder for audio processing)"""
        # For AMR files, we would need audio processing libraries
        # For now, extract what we can from filename and metadata

        file_name = Path(file_path).name
        file_stats = Path(file_path).stat()

        events = [
            TimelineEvent(
                timestamp=datetime.datetime.fromtimestamp(
                    file_stats.st_ctime
                ).isoformat(),
                event_type="audio_recording",
                description=f"Audio recording created: {file_name}",
                participants=["unknown"],
                significance="important",
                source_file=file_name,
            )
        ]

        return events

    def _analyze_significance(self, text: str) -> str:
        """Analyze text to determine event significance"""
        text_lower = text.lower()

        # Critical indicators
        critical_keywords = [
            "violation",
            "illegal",
            "lawsuit",
            "court",
            "judge",
            "ruling",
            "emergency",
            "urgent",
            "immediate",
            "suspended",
            "expelled",
            "terminated",
            "fired",
            "dismissed",
        ]

        # Important indicators
        important_keywords = [
            "meeting",
            "decision",
            "policy",
            "requirement",
            "deadline",
            "obligation",
            "responsibility",
            "agreement",
            "contract",
            "notification",
            "warning",
            "concern",
            "issue",
        ]

        if any(keyword in text_lower for keyword in critical_keywords):
            return "critical"
        elif any(keyword in text_lower for keyword in important_keywords):
            return "important"
        else:
            return "informational"

    def _extract_participants(self, text: str) -> List[str]:
        """Extract participant names from text"""
        # Simple name extraction - look for capitalized words
        words = text.split()
        participants = []

        for i, word in enumerate(words):
            if word[0].isupper() and len(word) > 2:
                # Check if it's likely a name (not common words)
                if word.lower() not in [
                    "the",
                    "and",
                    "but",
                    "for",
                    "with",
                    "this",
                    "that",
                ]:
                    # Check if next word is also capitalized (full name)
                    if i + 1 < len(words) and words[i + 1][0].isupper():
                        participants.append(f"{word} {words[i + 1]}")
                    else:
                        participants.append(word)

        return list(set(participants))  # Remove duplicates

    def generate_report(
        self, case_id: str, file_patterns: Optional[List[str]] = None
    ) -> EvidenceReport:
        """Generate comprehensive evidence report"""
        if file_patterns is None:
            file_patterns = ["*.txt", "*.amr", "*.mp3", "*.wav"]

        all_events = []
        all_participants = set()
        source_files = []

        # Process all matching files in evidence directory
        for pattern in file_patterns:
            for file_path in self.data_path.glob(pattern):
                source_files.append(str(file_path))

                if file_path.suffix.lower() in [".txt"]:
                    events = self.process_text_file(str(file_path))
                elif file_path.suffix.lower() in [".amr", ".mp3", ".wav"]:
                    events = self.process_audio_metadata(str(file_path))
                else:
                    continue

                all_events.extend(events)
                for event in events:
                    all_participants.update(event.participants)

        # Sort events by timestamp
        all_events.sort(key=lambda x: x.timestamp or "")

        # Extract key issues
        key_issues = self._extract_key_issues(all_events)

        # Generate summary
        summary = self._generate_summary(all_events, list(all_participants), key_issues)

        report = EvidenceReport(
            case_id=case_id,
            timeline=all_events,
            participants=list(all_participants),
            key_issues=key_issues,
            summary=summary,
            source_files=source_files,
            processing_date=datetime.datetime.now().isoformat(),
        )

        # Save report
        self._save_report(report)

        return report

    def _extract_key_issues(self, events: List[TimelineEvent]) -> List[str]:
        """Extract key issues from timeline events"""
        issues = set()

        for event in events:
            desc_lower = event.description.lower()

            # Look for issue keywords
            if "violation" in desc_lower:
                issues.add("Policy/Rule Violations")
            if any(word in desc_lower for word in ["iep", "special education", "504"]):
                issues.add("Special Education Services")
            if any(word in desc_lower for word in ["discrimination", "bias", "unfair"]):
                issues.add("Discrimination/Unfair Treatment")
            if any(word in desc_lower for word in ["deadline", "timeline", "late"]):
                issues.add("Timeline/Deadline Issues")
            if any(
                word in desc_lower
                for word in ["communication", "notification", "inform"]
            ):
                issues.add("Communication Issues")
            if any(
                word in desc_lower for word in ["service", "support", "accommodation"]
            ):
                issues.add("Service Provision")

        return list(issues)

    def _generate_summary(
        self,
        events: List[TimelineEvent],
        participants: List[str],
        key_issues: List[str],
    ) -> str:
        """Generate human-readable summary"""
        critical_events = [e for e in events if e.significance == "critical"]
        important_events = [e for e in events if e.significance == "important"]

        summary = f"""
EVIDENCE PROCESSING SUMMARY

Timeline Analysis:
- Total events processed: {len(events)}
- Critical events: {len(critical_events)}
- Important events: {len(important_events)}
- Participants identified: {len(participants)}

Key Participants:
{', '.join(participants[:10])}  # Limit to first 10

Key Issues Identified:
{chr(10).join(f"- {issue}" for issue in key_issues)}

Critical Events Timeline:
"""

        for event in critical_events[:5]:  # Top 5 critical events
            summary += (
                f"- {event.timestamp or 'No timestamp'}: {event.description[:100]}...\n"
            )

        if len(critical_events) > 5:
            summary += f"... and {len(critical_events) - 5} more critical events\n"

        summary += f"""
Processing completed on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

This automated analysis provides a structured view of the evidence timeline.
For legal proceedings, human review and verification is recommended.
"""

        return summary.strip()

    def _save_report(self, report: EvidenceReport):
        """Save evidence report to JSON file"""
        report_file = self.data_path / f"evidence-report-{report.case_id}.json"

        # Convert to serializable format
        report_dict = {
            "case_id": report.case_id,
            "processing_date": report.processing_date,
            "summary": report.summary,
            "participants": report.participants,
            "key_issues": report.key_issues,
            "source_files": report.source_files,
            "timeline": [
                {
                    "timestamp": e.timestamp,
                    "event_type": e.event_type,
                    "description": e.description,
                    "participants": e.participants,
                    "significance": e.significance,
                    "source_file": e.source_file,
                }
                for e in report.timeline
            ],
        }

        with open(report_file, "w") as f:
            json.dump(report_dict, f, indent=2)

        logger.info(f"Evidence report saved to {report_file}")

    def export_timeline_csv(
        self, report: EvidenceReport, output_file: Optional[str] = None
    ):
        """Export timeline to CSV format"""
        import csv

        output_path = (
            Path(output_file)
            if output_file
            else self.data_path / f"timeline-{report.case_id}.csv"
        )

        with open(output_path, "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = [
                "timestamp",
                "event_type",
                "description",
                "participants",
                "significance",
                "source_file",
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for event in report.timeline:
                writer.writerow(
                    {
                        "timestamp": event.timestamp or "",
                        "event_type": event.event_type,
                        "description": event.description,
                        "participants": "; ".join(event.participants),
                        "significance": event.significance,
                        "source_file": event.source_file,
                    }
                )

        logger.info(f"Timeline exported to {output_path}")


def main():
    """CLI entry point for evidence processing"""
    import argparse

    parser = argparse.ArgumentParser(description="Evidence Processor")
    parser.add_argument("--case-id", required=True, help="Case identifier")
    parser.add_argument("--process", action="store_true", help="Process evidence files")
    parser.add_argument(
        "--export-csv", action="store_true", help="Export timeline to CSV"
    )
    parser.add_argument("--files", nargs="*", help="Specific files to process")

    args = parser.parse_args()

    processor = EvidenceProcessor()

    if args.process:
        file_patterns = args.files if args.files else None
        report = processor.generate_report(args.case_id, file_patterns)

        print(f"Evidence processing complete for case: {args.case_id}")
        print(f"Events processed: {len(report.timeline)}")
        print(f"Participants identified: {len(report.participants)}")
        print(f"Key issues: {len(report.key_issues)}")
        print(f"Report saved to: data/evidence/evidence-report-{args.case_id}.json")

        if args.export_csv:
            processor.export_timeline_csv(report)
            print(f"Timeline exported to: data/evidence/timeline-{args.case_id}.csv")


if __name__ == "__main__":
    main()
