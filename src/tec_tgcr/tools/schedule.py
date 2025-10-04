"""Schedule assistant for aligning work sessions and shifts."""
from __future__ import annotations

import csv
import io
import uuid
from datetime import UTC, datetime
from typing import Dict, Iterable, List, Tuple


class ScheduleTool:
    """Provides formatted schedule summaries and export utilities."""

    name = "schedule_planner"
    description = "Summarize planned TEC build sessions, shifts, and export cadence artifacts."

    def __init__(
        self,
        sessions: Iterable[Dict[str, str] | Tuple[str, str]],
        shifts: Iterable[Dict[str, str] | Tuple[str, str]],
        ics_name: str = "tec_schedule",
        planner_bucket: str = "Operations",
    ) -> None:
        self.sessions = [self._normalise_record(record) for record in sessions]
        self.shifts = [self._normalise_record(record) for record in shifts]
        self.ics_name = ics_name
        self.planner_bucket = planner_bucket

    def run(self, query: str) -> str:
        query_lower = query.lower()
        parts: List[str] = []

        if "tec" in query_lower or "build" in query_lower:
            parts.append("TEC Build Sessions:")
            parts.extend(self._format_lines(self.sessions))

        if "shift" in query_lower or "7-eleven" in query_lower or "711" in query_lower:
            parts.append("7-Eleven Shifts:")
            parts.extend(self._format_lines(self.shifts))

        if "ics" in query_lower or "calendar" in query_lower:
            ics_content = self._generate_ics()
            parts.append("ICS Export (copy into a .ics file):")
            parts.append(f"```ical\n{ics_content}\n```")

        if "planner" in query_lower or "csv" in query_lower:
            csv_content = self._generate_planner_csv()
            parts.append("Planner CSV (import into Microsoft Planner):")
            parts.append(f"```csv\n{csv_content}\n```")

        if not parts:
            parts.append("Current cadence:")
            parts.append("TEC Build Sessions:")
            parts.extend(self._format_lines(self.sessions))
            parts.append("7-Eleven Shifts:")
            parts.extend(self._format_lines(self.shifts))

        parts.append(f"Generated {datetime.now(UTC).isoformat()}")
        return "\n".join(parts)

    # === Helpers ===
    @staticmethod
    def _normalise_record(record: Dict[str, str] | Tuple[str, str]) -> Dict[str, str]:
        if isinstance(record, dict):
            return record
        label, window = record
        return {"label": label, "window": window}

    @staticmethod
    def _format_lines(items: List[Dict[str, str]]) -> List[str]:
        lines: List[str] = []
        for item in items:
            label = item.get("label", "")
            window = item.get("window", "")
            lines.append(f"  - {label}: {window}")
        return lines

    def _generate_ics(self) -> str:
        events = [item for item in self.sessions + self.shifts if item.get("start") and item.get("end")]
        if not events:
            return "No dated events configured. Add start/end ISO timestamps in tool settings."

        dtstamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
        lines = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//TEC//Schedule//EN"]
        for event in events:
            start = self._to_ics_timestamp(event["start"])
            end = self._to_ics_timestamp(event["end"])
            uid = event.get("uid") or f"{uuid.uuid4()}@tec-tgcr"
            summary = event.get("label", "TEC Event")
            description = event.get("window", "")
            location = event.get("location", "")
            lines.extend(
                [
                    "BEGIN:VEVENT",
                    f"UID:{uid}",
                    f"DTSTAMP:{dtstamp}",
                    f"DTSTART:{start}",
                    f"DTEND:{end}",
                    f"SUMMARY:{summary}",
                    f"DESCRIPTION:{description}",
                    f"LOCATION:{location}",
                ]
            )
            if event.get("rrule"):
                lines.append(f"RRULE:{event['rrule']}")
            lines.append("END:VEVENT")
        lines.append("END:VCALENDAR")
        return "\n".join(lines)

    def _generate_planner_csv(self) -> str:
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(["Title", "Bucket", "Start Date", "Due Date", "Notes"])
        for event in self.sessions + self.shifts:
            start = event.get("start", "")
            end = event.get("end", "")
            notes = event.get("window", "")
            writer.writerow([
                event.get("label", "TEC Task"),
                self.planner_bucket,
                start,
                end,
                notes,
            ])
        return output.getvalue().strip()

    @staticmethod
    def _to_ics_timestamp(value: str) -> str:
        dt = datetime.fromisoformat(value)
        return dt.astimezone(UTC).strftime("%Y%m%dT%H%M%SZ")
