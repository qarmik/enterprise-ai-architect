#!/usr/bin/env python3
"""Tests for api_client.py — uses mocking to avoid real API calls."""
import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))))

from unittest.mock import patch, MagicMock
from api_client import validate_schema, save_to_csv


MOCK_RESPONSE = {
    'result': 'success',
    'base_code': 'USD',
    'time_last_update_utc': 'Mon, 12 May 2026 00:00:00 +0000',
    'rates': {
        'INR': 83.5,
        'GBP': 0.79,
        'EUR': 0.92,
        'JPY': 155.2,
        'SGD': 1.34,
        'AED': 3.67,
    }
}


def test_validate_schema_passes_on_valid_data():
    validate_schema(MOCK_RESPONSE)


def test_validate_schema_fails_on_missing_field():
    bad_data = {'result': 'success', 'base_code': 'USD'}
    with pytest.raises(ValueError):
        validate_schema(bad_data)


def test_validate_schema_fails_on_non_success_result():
    bad_data = {**MOCK_RESPONSE, 'result': 'error'}
    with pytest.raises(ValueError):
        validate_schema(bad_data)


def test_save_to_csv_creates_file(tmp_path):
    filepath = save_to_csv(MOCK_RESPONSE, str(tmp_path))
    assert os.path.exists(filepath)


def test_save_to_csv_contains_inr_rate(tmp_path):
    filepath = save_to_csv(MOCK_RESPONSE, str(tmp_path))
    with open(filepath) as f:
        content = f.read()
    assert 'INR' in content
    assert '83.5' in content


@patch('api_client.requests.get')
def test_fetch_uses_correct_url(mock_get):
    mock_response = MagicMock()
    mock_response.json.return_value = MOCK_RESPONSE
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    from api_client import fetch_exchange_rates
    fetch_exchange_rates('USD')
    mock_get.assert_called_once()
    call_url = mock_get.call_args[0][0]
    assert 'USD' in call_url