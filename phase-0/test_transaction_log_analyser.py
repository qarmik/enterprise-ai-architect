#!/usr/bin/env python3
"""Tests for transaction_log_analyser.py"""
import subprocess
import sys
import os
import pytest

def test_analyser_runs_without_error():
    """Analyser must run without crashing on valid input."""
    result = subprocess.run(
        [
            sys.executable,
            "phase-0/transaction_log_analyser.py",
            "phase-0/sample_transactions.csv"
        ],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, (
        f"Analyser failed with:\n{result.stderr}"
    )


def test_analyser_output_contains_required_fields():
    """Report must contain key statistical fields."""
    result = subprocess.run(
        [
            sys.executable,
            "phase-0/transaction_log_analyser.py",
            "phase-0/sample_transactions.csv"
        ],
        capture_output=True,
        text=True
    )
    output = result.stdout
    assert "TRANSACTION LOG ANALYSIS REPORT" in output
    assert "Total transactions" in output
    assert "Failure rate" in output
    assert "p50 processing time" in output
    assert "p95 processing time" in output
    assert "p99 processing time" in output


def test_compute_statistics_failure_rate():
    """Failure rate calculation must be correct."""
    transactions = [
        {'status': 'SUCCESS', 'processing_time_ms': '100',
         'transaction_type': 'CREDIT'},
        {'status': 'SUCCESS', 'processing_time_ms': '200',
         'transaction_type': 'DEBIT'},
        {'status': 'FAILED', 'processing_time_ms': '300',
         'transaction_type': 'TRANSFER'},
        {'status': 'SUCCESS', 'processing_time_ms': '150',
         'transaction_type': 'CREDIT'},
    ]
    import sys, os
    sys.path.insert(0, os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))))
    from transaction_log_analyser import compute_statistics
    stats = compute_statistics(transactions)
    assert stats['total_transactions'] == 4
    assert stats['failed'] == 1
    assert stats['failure_rate_pct'] == 25.0


def test_empty_transactions_raises_error():
    """Empty transaction list must raise ValueError."""
    import sys, os
    sys.path.insert(0, os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))))
    from transaction_log_analyser import compute_statistics
    with pytest.raises(ValueError):
        compute_statistics([])