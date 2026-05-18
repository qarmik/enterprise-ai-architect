#!/usr/bin/env python3
"""
transaction_log_analyser.py — Phase 0 Artifact P0-A1
Reads transaction logs, computes statistics, writes report.
Domain: Banking and regulated financial services.
"""

import csv
import argparse
import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s — %(levelname)s — %(message)s'
)
logger = logging.getLogger(__name__)


def load_transactions(filepath: str) -> list[dict]:
    """Load transactions from a CSV file."""
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {filepath}")

    transactions = []
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            transactions.append(row)

    logger.info(f"Loaded {len(transactions)} transactions from {filepath}")
    return transactions


def compute_statistics(transactions: list[dict]) -> dict:
    """Compute key statistics from transaction data."""
    if not transactions:
        raise ValueError("No transactions to analyse")

    total = len(transactions)
    failed = [t for t in transactions if t['status'] == 'FAILED']
    success = [t for t in transactions if t['status'] == 'SUCCESS']

    processing_times = [
        int(t['processing_time_ms']) for t in transactions
    ]
    processing_times.sort()

    def percentile(data: list, pct: float) -> float:
        index = int(len(data) * pct / 100)
        return data[min(index, len(data) - 1)]

    type_counts = {}
    for t in transactions:
        tx_type = t['transaction_type']
        type_counts[tx_type] = type_counts.get(tx_type, 0) + 1

    top_type = max(type_counts, key=type_counts.get)

    return {
        'total_transactions': total,
        'successful': len(success),
        'failed': len(failed),
        'failure_rate_pct': round(len(failed) / total * 100, 2),
        'p50_processing_ms': percentile(processing_times, 50),
        'p95_processing_ms': percentile(processing_times, 95),
        'p99_processing_ms': percentile(processing_times, 99),
        'top_transaction_type': top_type,
        'type_counts': type_counts,
    }


def print_report(stats: dict) -> None:
    """Print a formatted report to stdout."""
    print("\n" + "="*50)
    print("  TRANSACTION LOG ANALYSIS REPORT")
    print("="*50)
    print(f"  Total transactions:    {stats['total_transactions']}")
    print(f"  Successful:            {stats['successful']}")
    print(f"  Failed:                {stats['failed']}")
    print(f"  Failure rate:          {stats['failure_rate_pct']}%")
    print(f"  p50 processing time:   {stats['p50_processing_ms']} ms")
    print(f"  p95 processing time:   {stats['p95_processing_ms']} ms")
    print(f"  p99 processing time:   {stats['p99_processing_ms']} ms")
    print(f"  Top transaction type:  {stats['top_transaction_type']}")
    print("\n  Transaction type breakdown:")
    for tx_type, count in stats['type_counts'].items():
        print(f"    {tx_type}: {count}")
    print("="*50 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description='Analyse transaction logs'
    )
    parser.add_argument(
        'filepath',
        help='Path to transaction CSV file'
    )
    parser.add_argument(
        '--output',
        default='phase-0/reports',
        help='Directory for report output (default: phase-0/reports)'
    )
    args = parser.parse_args()

    transactions = load_transactions(args.filepath)
    stats = compute_statistics(transactions)
    print_report(stats)
    write_report(stats, args.output)

def write_report(stats: dict, output_path: str) -> None:
    """Write report to a timestamped file."""
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"transaction_report_{timestamp}.txt"
    full_path = Path(output_path) / filename

    Path(output_path).mkdir(parents=True, exist_ok=True)

    with open(full_path, 'w') as f:
        f.write("TRANSACTION LOG ANALYSIS REPORT\n")
        f.write("="*50 + "\n")
        f.write(f"Generated: {datetime.now().isoformat()}\n")
        f.write(f"Total transactions: {stats['total_transactions']}\n")
        f.write(f"Successful: {stats['successful']}'\n")
        f.write(f"Failed: {stats['failed']}\n")
        f.write(f"Failure rate: {stats['failure_rate_pct']}%\n")
        f.write(f"p50: {stats['p50_processing_ms']} ms\n")
        f.write(f"p95: {stats['p95_processing_ms']} ms\n")
        f.write(f"p99: {stats['p99_processing_ms']} ms\n")
        f.write(f"Top type: {stats['top_transaction_type']}\n")

    logger.info(f"Report written to {full_path}")
    print(f"Report saved: {full_path}")
       


if __name__ == "__main__":
    main()