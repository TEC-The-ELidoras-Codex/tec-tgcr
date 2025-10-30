"""
TEC Agent Tool Integration

Integrates financial monitoring and evidence processing tools
with the main TEC-TGCR agent system for automated operations.
"""

import logging
from pathlib import Path
from typing import Dict, Any, Optional
from datetime import datetime, timedelta

from .financial import AzureFinancialMonitor
from .evidence import EvidenceProcessor

logger = logging.getLogger(__name__)


class TECToolIntegration:
    """Central integration point for TEC agent tools"""
    
    def __init__(self, 
                 subscription_id: str = "89d36e9a-a518-4151-95b3-087ec1b88ec5",
                 data_path: Optional[Path] = None):
        self.subscription_id = subscription_id
        self.data_path = data_path or Path("data")
        
        # Initialize tool components
        self.financial_monitor = AzureFinancialMonitor(
            subscription_id, 
            self.data_path / "financial"
        )
        self.evidence_processor = EvidenceProcessor(self.data_path / "evidence")
        
        # Ensure data directories exist
        (self.data_path / "financial").mkdir(parents=True, exist_ok=True)
        (self.data_path / "evidence").mkdir(parents=True, exist_ok=True)
    
    def daily_financial_check(self) -> Dict[str, Any]:
        """Daily automated financial monitoring check"""
        logger.info("Starting daily financial monitoring check")
        
        try:
            # Detect cost anomalies
            anomalies = self.financial_monitor.detect_anomalies(threshold_multiplier=5.0)
            
            result = {
                "check_date": datetime.now().isoformat(),
                "status": "completed",
                "anomalies_found": len(anomalies),
                "total_unexpected_cost": sum(a.cost for a in anomalies),
                "anomalies": [
                    {
                        "date": a.date,
                        "cost": a.cost,
                        "severity": a.severity
                    }
                    for a in anomalies
                ],
                "actions_taken": []
            }
            
            # Auto-generate refund evidence if critical anomalies found
            critical_anomalies = [a for a in anomalies if a.severity in ["critical", "high"]]
            if critical_anomalies:
                logger.warning(f"Found {len(critical_anomalies)} critical cost anomalies")
                
                # Generate evidence package
                evidence = self.financial_monitor.generate_refund_evidence()
                result["evidence_generated"] = True
                result["evidence_total"] = evidence.total_unexpected_cost
                result["actions_taken"].append("Generated refund evidence package")
                
                # Auto-submit if over threshold
                if evidence.total_unexpected_cost > 50.0:  # $50 threshold
                    request = self.financial_monitor.submit_refund_request(evidence)
                    result["refund_request_submitted"] = True
                    result["ticket_id"] = request["ticket_id"]
                    result["actions_taken"].append(f"Submitted refund request: {request['ticket_id']}")
                    
                    logger.info(f"Auto-submitted refund request: {request['ticket_id']}")
            
            logger.info(f"Daily financial check completed: {len(anomalies)} anomalies found")
            return result
            
        except Exception as e:
            logger.error(f"Daily financial check failed: {e}")
            return {
                "check_date": datetime.now().isoformat(),
                "status": "failed",
                "error": str(e)
            }
    
    def process_new_evidence(self, case_id: Optional[str] = None) -> Dict[str, Any]:
        """Process any new evidence files in the evidence directory"""
        logger.info("Starting evidence processing")
        
        try:
            # Use timestamp as case ID if not provided
            case_id = case_id or f"TEC-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
            
            # Generate evidence report
            report = self.evidence_processor.generate_report(case_id)
            
            result = {
                "processing_date": datetime.now().isoformat(),
                "case_id": case_id,
                "status": "completed",
                "events_processed": len(report.timeline),
                "participants_identified": len(report.participants),
                "key_issues": report.key_issues,
                "critical_events": len([e for e in report.timeline if e.significance == "critical"]),
                "source_files": report.source_files
            }
            
            # Export timeline to CSV for external use
            self.evidence_processor.export_timeline_csv(report)
            result["csv_exported"] = True
            
            logger.info(f"Evidence processing completed for case: {case_id}")
            return result
            
        except Exception as e:
            logger.error(f"Evidence processing failed: {e}")
            return {
                "processing_date": datetime.now().isoformat(),
                "case_id": case_id,
                "status": "failed",
                "error": str(e)
            }
    
    def get_financial_status(self) -> Dict[str, Any]:
        """Get current financial status and recent activity"""
        try:
            costs = self.financial_monitor.load_cost_data()
            if not costs:
                return {"status": "no_data", "message": "No cost data available"}
            
            # Calculate recent metrics
            recent_costs = costs[-7:]  # Last 7 entries
            total_recent = sum(c['cost'] for c in recent_costs)
            avg_daily = total_recent / len(recent_costs) if recent_costs else 0
            
            # Get anomalies
            anomalies = self.financial_monitor.detect_anomalies()
            recent_anomalies = [a for a in anomalies 
                              if datetime.strptime(a.date, "%Y-%m-%d") > 
                              datetime.now() - timedelta(days=7)]
            
            return {
                "status": "active",
                "subscription_id": self.subscription_id,
                "recent_total_cost": total_recent,
                "average_daily_cost": avg_daily,
                "total_anomalies": len(anomalies),
                "recent_anomalies": len(recent_anomalies),
                "last_update": costs[-1]['date'] if costs else None,
                "data_points": len(costs)
            }
            
        except Exception as e:
            logger.error(f"Failed to get financial status: {e}")
            return {"status": "error", "error": str(e)}
    
    def get_evidence_status(self) -> Dict[str, Any]:
        """Get current evidence processing status"""
        try:
            evidence_dir = self.data_path / "evidence"
            
            # Count files by type
            text_files = list(evidence_dir.glob("*.txt"))
            audio_files = list(evidence_dir.glob("*.amr")) + list(evidence_dir.glob("*.mp3"))
            report_files = list(evidence_dir.glob("evidence-report-*.json"))
            
            return {
                "status": "active",
                "evidence_directory": str(evidence_dir),
                "text_files": len(text_files),
                "audio_files": len(audio_files),
                "processed_reports": len(report_files),
                "total_files": len(text_files) + len(audio_files),
                "recent_files": [
                    f.name for f in sorted(
                        text_files + audio_files, 
                        key=lambda x: x.stat().st_mtime, 
                        reverse=True
                    )[:5]  # Most recent 5 files
                ]
            }
            
        except Exception as e:
            logger.error(f"Failed to get evidence status: {e}")
            return {"status": "error", "error": str(e)}
    
    def run_comprehensive_check(self) -> Dict[str, Any]:
        """Run comprehensive check of all TEC tools"""
        logger.info("Starting comprehensive TEC tools check")
        
        results = {
            "check_timestamp": datetime.now().isoformat(),
            "financial_check": self.daily_financial_check(),
            "evidence_processing": self.process_new_evidence(),
            "financial_status": self.get_financial_status(),
            "evidence_status": self.get_evidence_status()
        }
        
        # Summary status
        all_successful = all(
            r.get("status") not in ["failed", "error"] 
            for r in results.values() 
            if isinstance(r, dict) and "status" in r
        )
        
        results["overall_status"] = "success" if all_successful else "partial_failure"
        
        logger.info(f"Comprehensive check completed: {results['overall_status']}")
        return results
    
    def export_status_report(self, output_file: Optional[str] = None) -> str:
        """Export comprehensive status report to file"""
        import json
        
        if not output_file:
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            output_file = f"tec-status-report-{timestamp}.json"
        
        status = self.run_comprehensive_check()
        
        with open(output_file, 'w') as f:
            json.dump(status, f, indent=2)
        
        logger.info(f"Status report exported to: {output_file}")
        return output_file


def main():
    """CLI entry point for TEC tool integration"""
    import argparse
    
    parser = argparse.ArgumentParser(description="TEC Tool Integration")
    parser.add_argument("--subscription-id", default="89d36e9a-a518-4151-95b3-087ec1b88ec5")
    parser.add_argument("--daily-check", action="store_true", help="Run daily financial check")
    parser.add_argument("--process-evidence", action="store_true", help="Process evidence files")
    parser.add_argument("--comprehensive", action="store_true", help="Run comprehensive check")
    parser.add_argument("--export-report", action="store_true", help="Export status report")
    parser.add_argument("--case-id", help="Case ID for evidence processing")
    
    args = parser.parse_args()
    
    # Setup logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    integration = TECToolIntegration(args.subscription_id)
    
    if args.daily_check:
        result = integration.daily_financial_check()
        print(f"Financial check completed: {result['status']}")
        if result.get('anomalies_found', 0) > 0:
            print(f"Anomalies found: {result['anomalies_found']}")
            print(f"Total unexpected cost: ${result['total_unexpected_cost']:.2f}")
    
    elif args.process_evidence:
        result = integration.process_new_evidence(args.case_id)
        print(f"Evidence processing completed: {result['status']}")
        if result['status'] == 'completed':
            print(f"Events processed: {result['events_processed']}")
            print(f"Key issues: {', '.join(result['key_issues'])}")
    
    elif args.comprehensive:
        result = integration.run_comprehensive_check()
        print(f"Comprehensive check completed: {result['overall_status']}")
        
        # Print summary
        if result['financial_check'].get('anomalies_found', 0) > 0:
            print(f"Financial anomalies: {result['financial_check']['anomalies_found']}")
        
        if result['evidence_processing'].get('events_processed', 0) > 0:
            print(f"Evidence events: {result['evidence_processing']['events_processed']}")
    
    elif args.export_report:
        report_file = integration.export_status_report()
        print(f"Status report exported to: {report_file}")
    
    else:
        # Default: show status
        financial_status = integration.get_financial_status()
        evidence_status = integration.get_evidence_status()
        
        print("TEC Tool Integration Status:")
        print(f"Financial monitoring: {financial_status.get('status', 'unknown')}")
        print(f"Evidence processing: {evidence_status.get('status', 'unknown')}")
        
        if financial_status.get('status') == 'active':
            print(f"Recent cost: ${financial_status.get('recent_total_cost', 0):.2f}")
            print(f"Anomalies detected: {financial_status.get('total_anomalies', 0)}")
        
        if evidence_status.get('status') == 'active':
            print(f"Evidence files: {evidence_status.get('total_files', 0)}")
            print(f"Processed reports: {evidence_status.get('processed_reports', 0)}")


if __name__ == "__main__":
    main()