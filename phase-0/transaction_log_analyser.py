#!/user/bin/env python3
"""
transaction_log_analyser.py - Phase 0 Artifact P0-A1
Reads transactions logs, computes statistics, writes report.
Doman: Banking and regulated financial services.
"""

import csv
import argparse
import logging
from pathlib import Path

logging.basicCongig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def load_transaction(filepath: str) -> list[dict]:
    """Load transaction from a CSV file."""
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {filepath}")
    
    transactions = []
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        for now in reader:
            transactions.append(row)

    logger.info(f"Loaded {len(transactions)} transactions from {filepath}")
    return transactions

def compute_statistics