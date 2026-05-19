#!/usr/bin/env python3
"""Tests for latency_calculator.py"""
import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))))

from latency_calculator import (
    generate_latency_samples,
    compute_percentiles,
    compute_gpu_cost_model,
)


def test_generates_correct_sample_count():
    samples = generate_latency_samples(1000)
    assert len(samples) == 1000


def test_all_latencies_are_positive():
    samples = generate_latency_samples(500)
    assert all(s > 0 for s in samples)


def test_percentiles_are_ordered():
    samples = generate_latency_samples(10000)
    p = compute_percentiles(samples)
    assert p['p50_ms'] <= p['p95_ms']
    assert p['p95_ms'] <= p['p99_ms']
    assert p['p99_ms'] <= p['p99_9_ms']


def test_empty_samples_raises_error():
    with pytest.raises(ValueError):
        compute_percentiles([])


def test_cost_model_returns_expected_keys():
    cost = compute_gpu_cost_model(
        tokens_per_second=180.0,
        cost_per_hour=2.50,
        daily_requests=10000,
        avg_tokens_per_request=500
    )
    assert 'monthly_cost_usd' in cost
    assert 'cost_per_1m_tokens_usd' in cost
    assert cost['monthly_cost_usd'] > 0


def test_cost_scales_with_requests():
    cost_low = compute_gpu_cost_model(180.0, 2.50, 1000, 500)
    cost_high = compute_gpu_cost_model(180.0, 2.50, 10000, 500)
    assert cost_high['monthly_cost_usd'] > cost_low['monthly_cost_usd']