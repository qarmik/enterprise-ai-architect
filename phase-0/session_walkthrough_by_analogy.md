# Session 7 Walkthrough by Analogy

## The sample CSV file

### Header row
```csv
date,account_id,transaction_type,amount,status,processing_time_ms
```

This is the label row, like the headings on a ledger page in an old bank archive.

- `date`: when the transaction happened.
- `account_id`: which account was involved.
- `transaction_type`: the kind of movement, like credit, debit, or transfer.
- `amount`: the money value.
- `status`: whether the transaction succeeded or failed.
- `processing_time_ms`: how long it took to process.

### Data rows

Each row is one transaction, like one entry in a clerk’s record book.  
The rows let the script later count totals, failures, and timing patterns.

## The script header

### Shebang
```python
#!/usr/bin/env python3
```

This tells the system to use Python 3 to run the script.  
It is like putting the correct seal on a dispatch so it is carried by the right courier.

### Docstring
```python
"""
transaction_log_analyser.py — Phase 0 Artifact P0-A1
Reads transaction logs, computes statistics, writes report.
Domain: Banking and regulated financial services.
"""
```

This is the title plaque on the file.  
It tells future readers what the script is for, like a plaque on a restored archive box.

## Imports

```python
import csv
import argparse
import logging
from pathlib import Path
```

These are the tools laid out on the clerk’s desk.

- `csv`: used to read the ledger.
- `argparse`: used to accept instructions from the command line.
- `logging`: used to leave official notes.
- `Path`: used to navigate the archive shelves cleanly.

## Logging setup

```python
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s — %(levelname)s — %(message)s'
)
logger = logging.getLogger(__name__)
```

This configures the script’s diary.

- `basicConfig(...)`: sets the format of the notes.
- `level=logging.INFO`: records normal important events.
- `format=...`: defines how each line should look.
- `getLogger(__name__)`: creates the note-writer.

Analogy: this is like assigning a court scribe who writes the time, rank, and message for every major event.

## Loading transactions

```python
def load_transactions(filepath: str) -> list[dict]:
```

This defines a function that reads the CSV file and returns a list of transaction dictionaries.  
It is like sending a clerk to fetch a bundle of indexed records from a cabinet.

### Path check
```python
path = Path(filepath)
if not path.exists():
    raise FileNotFoundError(f"File not found: {filepath}")
```

This checks whether the file exists.

Analogy: before opening a sealed archive chest, the clerk first checks whether the chest is even on the shelf.

### Read CSV
```python
transactions = []
with open(path, newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        transactions.append(row)
```

This creates a list, opens the file, reads each row as a dictionary, and stores it.

Analogy: the clerk copies each ledger entry into a fresh notebook, one row at a time.

### Log and return
```python
logger.info(f"Loaded {len(transactions)} transactions from {filepath}")
return transactions
```

This records how many entries were found and returns them.

Analogy: after counting the scrolls, the clerk writes, “I found 12 records,” and hands them over.

## Computing statistics

```python
def compute_statistics(transactions: list[dict]) -> dict:
```

This turns raw rows into useful numbers.  
It is like a treasury auditor turning a pile of receipts into a summary report.

### Empty input check
```python
if not transactions:
    raise ValueError("No transactions to analyse")
```

If there are no transactions, the function stops.

Analogy: if the archive box is empty, there is nothing to summarize.

### Count totals
```python
total = len(transactions)
failed = [t for t in transactions if t['status'] == 'FAILED']
success = [t for t in transactions if t['status'] == 'SUCCESS']
```

This counts all entries and separates them into failed and successful groups.

Analogy: the auditor sorts receipts into “approved” and “rejected” piles.

### Processing times
```python
processing_times = [
    int(t['processing_time_ms']) for t in transactions
]
processing_times.sort()
```

This converts timing values to numbers and sorts them.

Analogy: the clerk arranges delivery times from fastest to slowest.

### Percentile helper
```python
def percentile(data: list, pct: float) -> float:
    index = int(len(data) * pct / 100)
    return data[min(index, len(data) - 1)]
```

This finds a percentile value.

Analogy: if everyone is standing in a queue, this picks the person around the 50th, 95th, or 99th position.

### Count transaction types
```python
type_counts = {}
for t in transactions:
    tx_type = t['transaction_type']
    type_counts[tx_type] = type_counts.get(tx_type, 0) + 1
```

This counts credits, debits, and transfers.

Analogy: the auditor keeps a tally for each category of record.

### Find the top type
```python
top_type = max(type_counts, key=type_counts.get)
```

This finds the most frequent transaction type.

Analogy: the auditor asks which pile is tallest.

### Return summary
```python
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
```

This packages the findings into one dictionary.

Analogy: the auditor binds the findings into a single report dossier.

## Printing the report

```python
def print_report(stats: dict) -> None:
```

This prints the report in a readable format.

Analogy: this is the public reading of the audit results in the hall.

### Report header
```python
print("\n" + "=" * 50)
print("  TRANSACTION LOG ANALYSIS REPORT")
print("=" * 50)
```

This creates a framed title.

Analogy: a herald enters the chamber and announces the report with a banner.

### Summary lines
```python
print(f"  Total transactions:    {stats['total_transactions']}")
print(f"  Successful:            {stats['successful']}")
print(f"  Failed:                {stats['failed']}")
print(f"  Failure rate:          {stats['failure_rate_pct']}%")
print(f"  p50 processing time:   {stats['p50_processing_ms']} ms")
print(f"  p95 processing time:   {stats['p95_processing_ms']} ms")
print(f"  p99 processing time:   {stats['p99_processing_ms']} ms")
print(f"  Top transaction type:  {stats['top_transaction_type']}")
```

These print the headline findings.

Analogy: the scribe reads the main treasury facts aloud.

### Breakdown
```python
print("\n  Transaction type breakdown:")
for tx_type, count in stats['type_counts'].items():
    print(f"    {tx_type}: {count}")
print("=" * 50 + "\n")
```

This shows the category-wise counts.

Analogy: the clerk reads the tally for each type of record one by one.

## Main function

```python
def main():
```

This is the main entry gate of the program.

Analogy: all official work begins through this gate.

### Parse input
```python
parser = argparse.ArgumentParser(
    description='Analyse transaction logs'
)
parser.add_argument(
    'filepath',
    help='Path to transaction CSV file'
)
args = parser.parse_args()
```

This tells the script to expect a file path.

Analogy: the clerk asks the messenger which archive box to fetch.

### Run the steps
```python
transactions = load_transactions(args.filepath)
stats = compute_statistics(transactions)
print_report(stats)
```

This loads the file, computes the summary, and prints the report.

Analogy: fetch the records, audit them, then read the verdict aloud.

## Program entry check

```python
if __name__ == "__main__":
    main()
```

This makes the script run when executed directly.

Analogy: if the gate sign says today is the audit day, the chief clerk begins.

## The test file

### Imports
```python
import subprocess
import sys
import os
import pytest
```

These are the inspection team’s tools.

- `subprocess`: runs the script from a test.
- `sys` and `os`: help locate paths.
- `pytest`: provides the testing rulebook.

### Test: analyzer runs
```python
def test_analyser_runs_without_error():
```

This checks that the script runs without crashing.

Analogy: inspectors make sure the clerk can complete the route without falling.

### Test: output contains required fields
```python
def test_analyser_output_contains_required_fields():
```

This checks the report contains the expected labels.

Analogy: inspectors verify the report includes the required headings.

### Test: failure rate
```python
def test_compute_statistics_failure_rate():
```

This checks the math on a small sample.

Analogy: inspectors compare the accountant’s numbers against a mini ledger.

### Test: empty transactions raises error
```python
def test_empty_transactions_raises_error():
```

This checks that an empty list raises a `ValueError`.

Analogy: if the archive box is empty, the auditor must complain instead of inventing numbers.

## The CI workflow

### Trigger
```yaml
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
```

This tells GitHub Actions when to run.

Analogy: the watchtower rings the bell whenever a new message reaches the main road.

### Python setup
```yaml
- name: Set up Python
  uses: actions/setup-python@v5
  with:
    python-version: '3.12.1'
```

This installs the right Python version in CI.

Analogy: the central workshop receives the same measuring tools as the local office.

### Install dependencies
```yaml
- name: Install dependencies
  run: |
    python -m pip install --upgrade pip
    pip install pytest
    pip install -r requirements.txt
```

This installs what the tests need.

Analogy: before inspection, the team checks that lamps, paper, and ink are available.

### Run tests
```yaml
- name: Run tests
  run: python -m pytest phase-0/ -v
```

This runs the full test suite.

Analogy: the inspectors read every page of the archive audit under the same official rules.

## Debugged lines and what they meant

### `processing_times.sort():`
The extra colon had to be removed.  
Analogy: a clerk added punctuation where none belonged.

### `logging.basicCongig`
This had to become `logging.basicConfig`.  
Analogy: a royal title was misspelled, so the wrong official was called.

### `init(...)`
This had to become `int(...)`.  
Analogy: a number was being summoned by the wrong name.

### `processing_time` vs `processing_times`
The plural name had to be made consistent.  
Analogy: two shelf labels referred to the same bundle differently.

### `transactions_type`
This had to become `transaction_type`.  
Analogy: the drawer label used the wrong category name.

### `top_transaction_ms`
This had to become `top_transaction_type`.  
Analogy: the heading said “time” when it should have said “kind.”

### Missing `import pytest`
This had to be added.  
Analogy: the inspector arrived without the rulebook.

### Broken `git commit -m` quotes
This had to be canceled and retyped correctly.  
Analogy: the messenger began a proclamation but never finished the sentence.

## The overall lesson

Session 7 was mostly a story of tiny mismatches:
- wrong file name,
- wrong spelling,
- wrong indentation,
- wrong import,
- wrong shell quoting.

Each one was small, but together they made the work feel much harder than it really was. Once all the labels, paths, names, and entry points matched, the whole machine worked.