#!/usr/bin/env python3
"""
api_client.py — Phase 0 Artifact P0-A3
Fetches exchange rate data from a free public API.
Validates schema, saves to timestamped CSV.
Domain: Financial data ingestion pipeline.
"""

import csv
import json
import logging
import argparse
import time
from datetime import datetime
from pathlib import Path

import requests

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s — %(levelname)s — %(message)s'
)
logger = logging.getLogger(__name__)

BASE_URL = "https://open.er-api.com/v6/latest"
MAX_RETRIES = 3
RETRY_DELAY_SECONDS = 2

REQUIRED_FIELDS = ['result', 'base_code', 'rates', 'time_last_update_utc']


def fetch_exchange_rates(
    base_currency: str = "USD",
    retries: int = MAX_RETRIES
) -> dict:
    """
    Fetch exchange rates with retry logic.
    Uses exponential backoff on failure.
    """
    url = f"{BASE_URL}/{base_currency}"

    for attempt in range(1, retries + 1):
        try:
            logger.info(
                f"Fetching rates for {base_currency} "
                f"(attempt {attempt}/{retries})"
            )
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            logger.info("Fetch successful")
            return data

        except requests.exceptions.Timeout:
            logger.warning(f"Timeout on attempt {attempt}")
        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP error: {e}")
            raise
        except requests.exceptions.ConnectionError:
            logger.warning(f"Connection error on attempt {attempt}")

        if attempt < retries:
            delay = RETRY_DELAY_SECONDS * (2 ** (attempt - 1))
            logger.info(f"Retrying in {delay}s...")
            time.sleep(delay)

    raise RuntimeError(
        f"Failed to fetch data after {retries} attempts"
    )


def validate_schema(data: dict) -> None:
    """Validate that required fields are present."""
    missing = [f for f in REQUIRED_FIELDS if f not in data]
    if missing:
        raise ValueError(f"Missing required fields: {missing}")
    if data.get('result') != 'success':
        raise ValueError(
            f"API returned non-success result: {data.get('result')}"
        )
    logger.info("Schema validation passed")


def save_to_csv(data: dict, output_dir: str = "phase-0/data") -> str:
    """Save rates to a timestamped CSV file."""
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"exchange_rates_{data['base_code']}_{timestamp}.csv"
    filepath = Path(output_dir) / filename

    rates = data['rates']
    target_currencies = ['INR', 'GBP', 'EUR', 'JPY', 'SGD', 'AED']

    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            'fetched_at', 'base_currency',
            'target_currency', 'rate',
            'last_updated_utc'
        ])
        for currency in target_currencies:
            if currency in rates:
                writer.writerow([
                    datetime.now().isoformat(),
                    data['base_code'],
                    currency,
                    rates[currency],
                    data['time_last_update_utc']
                ])

    logger.info(f"Saved to {filepath}")
    return str(filepath)


def main():
    parser = argparse.ArgumentParser(
        description='Fetch and store exchange rate data'
    )
    parser.add_argument(
        '--base', default='USD',
        help='Base currency (default: USD)'
    )
    parser.add_argument(
        '--output', default='phase-0/data',
        help='Output directory'
    )
    args = parser.parse_args()

    data = fetch_exchange_rates(args.base)
    validate_schema(data)
    filepath = save_to_csv(data, args.output)

    print(f"\nExchange rates fetched successfully.")
    print(f"Base currency: {data['base_code']}")
    print(f"Saved to: {filepath}")
    print(f"Last updated: {data['time_last_update_utc']}\n")


if __name__ == "__main__":
    main()