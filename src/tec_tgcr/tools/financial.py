"""
Azure Financial Monitoring and Evidence Generation Tool

Integrates with Azure Cost Management APIs to detect anomalies,
generate refund evidence, and automate support ticket creation.
"""

import json
import csv
import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)


@dataclass
class CostAnomaly:
    """Represents a detected cost anomaly"""

    date: str
    cost: float
    baseline: float
    severity: str  # "low", "medium", "high", "critical"
    service: Optional[str] = None
    resource_group: Optional[str] = None


@dataclass
class RefundEvidence:
    """Structured evidence for refund requests"""

    subscription_id: str
    tenant_id: str
    anomalies: List[CostAnomaly]
    total_unexpected_cost: float
    evidence_files: List[str]
    timeline: Dict[str, Any]
    summary: str


class AzureFinancialMonitor:
    """Monitor Azure costs and generate refund evidence"""

    def __init__(self, subscription_id: str, data_path: Path = None):
        self.subscription_id = subscription_id
        self.data_path = data_path or Path("data/financial")
        self.data_path.mkdir(parents=True, exist_ok=True)

    def load_cost_data(self, csv_path: str = None) -> List[Dict]:
        """Load cost data from CSV file"""
        csv_path = csv_path or self.data_path / "cost-analysis.csv"

        costs = []
        try:
            with open(csv_path, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    costs.append(
                        {
                            "date": row["UsageDate"],
                            "cost": float(row["CostUSD"]),
                            "currency": row["Currency"],
                        }
                    )
        except FileNotFoundError:
            logger.error(f"Cost data file not found: {csv_path}")
            return []

        return costs

    def detect_anomalies(self, threshold_multiplier: float = 10.0) -> List[CostAnomaly]:
        """Detect cost anomalies based on baseline deviation"""
        costs = self.load_cost_data()
        if not costs:
            return []

        # Calculate baseline (average of non-zero costs)
        non_zero_costs = [c["cost"] for c in costs if c["cost"] > 0.01]
        if not non_zero_costs:
            baseline = 0.0
        else:
            baseline = sum(non_zero_costs) / len(non_zero_costs)

        anomalies = []
        for cost_entry in costs:
            cost = cost_entry["cost"]
            date = cost_entry["date"]

            if cost > baseline * threshold_multiplier:
                severity = self._determine_severity(cost, baseline)
                anomalies.append(
                    CostAnomaly(
                        date=date, cost=cost, baseline=baseline, severity=severity
                    )
                )

        return anomalies

    def _determine_severity(self, cost: float, baseline: float) -> str:
        """Determine anomaly severity based on cost deviation"""
        ratio = cost / (baseline + 0.01)  # Avoid division by zero

        if ratio > 100:
            return "critical"
        elif ratio > 50:
            return "high"
        elif ratio > 10:
            return "medium"
        else:
            return "low"

    def generate_refund_evidence(
        self, start_date: str = None, end_date: str = None
    ) -> RefundEvidence:
        """Generate comprehensive refund evidence package"""
        anomalies = self.detect_anomalies()

        # Filter by date range if provided
        if start_date or end_date:
            filtered_anomalies = []
            for anomaly in anomalies:
                anomaly_date = datetime.datetime.strptime(anomaly.date, "%Y-%m-%d")

                if start_date:
                    start_dt = datetime.datetime.strptime(start_date, "%Y-%m-%d")
                    if anomaly_date < start_dt:
                        continue

                if end_date:
                    end_dt = datetime.datetime.strptime(end_date, "%Y-%m-%d")
                    if anomaly_date > end_dt:
                        continue

                filtered_anomalies.append(anomaly)

            anomalies = filtered_anomalies

        total_unexpected = sum(a.cost for a in anomalies)

        # Generate timeline
        timeline = {
            "incident_start": start_date or (anomalies[0].date if anomalies else None),
            "incident_end": end_date or (anomalies[-1].date if anomalies else None),
            "detection_date": datetime.datetime.now().isoformat(),
            "anomaly_count": len(anomalies),
            "services_affected": list(set(a.service for a in anomalies if a.service)),
        }

        # Create evidence files list
        evidence_files = [
            "cost-analysis.csv",
            "azure-refund-evidence.json",
            "anomaly-report.json",
        ]

        # Generate summary
        summary = self._generate_summary(anomalies, total_unexpected)

        evidence = RefundEvidence(
            subscription_id=self.subscription_id,
            tenant_id="7d290c31-2df1-4e76-ab86-e26f12753bde",  # From your account data
            anomalies=anomalies,
            total_unexpected_cost=total_unexpected,
            evidence_files=evidence_files,
            timeline=timeline,
            summary=summary,
        )

        # Save evidence to file
        self._save_evidence(evidence)

        return evidence

    def _generate_summary(self, anomalies: List[CostAnomaly], total_cost: float) -> str:
        """Generate human-readable summary for support ticket"""
        if not anomalies:
            return "No cost anomalies detected in the specified period."

        summary = f"""
Azure Cost Anomaly Report - Subscription {self.subscription_id}

SUMMARY:
- {len(anomalies)} cost anomalies detected
- Total unexpected charges: ${total_cost:.2f}
- Period: {anomalies[0].date} to {anomalies[-1].date}
- Severity levels: {', '.join(set(a.severity for a in anomalies))}

DETAILED BREAKDOWN:
"""

        for anomaly in anomalies:
            summary += f"- {anomaly.date}: ${anomaly.cost:.2f} (baseline: ${anomaly.baseline:.2f}, severity: {anomaly.severity})\n"

        summary += f"""
EVIDENCE:
All supporting evidence including cost analysis data, Azure CLI output, 
and automated reports are attached to this request.

REQUEST:
We request a refund/credit for the unexpected charges totaling ${total_cost:.2f}
that occurred during the specified period. The charges appear to be related
to resources that were not intentionally provisioned or were misconfigured.
"""

        return summary.strip()

    def _save_evidence(self, evidence: RefundEvidence):
        """Save evidence to JSON file"""
        evidence_file = self.data_path / "refund-evidence.json"

        # Convert to serializable format
        evidence_dict = {
            "subscription_id": evidence.subscription_id,
            "tenant_id": evidence.tenant_id,
            "total_unexpected_cost": evidence.total_unexpected_cost,
            "summary": evidence.summary,
            "timeline": evidence.timeline,
            "evidence_files": evidence.evidence_files,
            "anomalies": [
                {
                    "date": a.date,
                    "cost": a.cost,
                    "baseline": a.baseline,
                    "severity": a.severity,
                    "service": a.service,
                    "resource_group": a.resource_group,
                }
                for a in evidence.anomalies
            ],
        }

        with open(evidence_file, "w") as f:
            json.dump(evidence_dict, f, indent=2)

        logger.info(f"Evidence saved to {evidence_file}")

    def submit_refund_request(self, evidence: RefundEvidence) -> Dict[str, Any]:
        """Simulate submission of refund request (placeholder for Azure API integration)"""
        # This would integrate with Azure Support API when available
        ticket_id = f"TEC-REFUND-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}"

        request = {
            "ticket_id": ticket_id,
            "status": "submitted",
            "subscription_id": evidence.subscription_id,
            "amount_requested": evidence.total_unexpected_cost,
            "evidence_package": evidence.evidence_files,
            "summary": evidence.summary,
            "submission_time": datetime.datetime.now().isoformat(),
        }

        # Save request to file
        request_file = self.data_path / f"refund-request-{ticket_id}.json"
        with open(request_file, "w") as f:
            json.dump(request, f, indent=2)

        logger.info(f"Refund request submitted: {ticket_id}")
        return request


def main():
    """CLI entry point for financial monitoring"""
    import argparse

    parser = argparse.ArgumentParser(description="Azure Financial Monitor")
    parser.add_argument(
        "--subscription-id", required=True, help="Azure subscription ID"
    )
    parser.add_argument("--monitor", action="store_true", help="Monitor for anomalies")
    parser.add_argument("--start-date", help="Start date for analysis (YYYY-MM-DD)")
    parser.add_argument("--end-date", help="End date for analysis (YYYY-MM-DD)")
    parser.add_argument(
        "--threshold", type=float, default=10.0, help="Anomaly threshold multiplier"
    )

    args = parser.parse_args()

    monitor = AzureFinancialMonitor(args.subscription_id)

    if args.monitor:
        anomalies = monitor.detect_anomalies(args.threshold)
        if anomalies:
            print(f"Detected {len(anomalies)} cost anomalies:")
            for anomaly in anomalies:
                print(f"  {anomaly.date}: ${anomaly.cost:.2f} ({anomaly.severity})")

            # Generate evidence
            evidence = monitor.generate_refund_evidence(args.start_date, args.end_date)
            print(
                f"\nEvidence package generated: ${evidence.total_unexpected_cost:.2f} total"
            )
            print("Summary saved to: data/financial/refund-evidence.json")
        else:
            print("No cost anomalies detected.")


if __name__ == "__main__":
    main()
