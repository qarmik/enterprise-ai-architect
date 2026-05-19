#!/usr/bin/env python3
"""
latency_calculator.py — Phase 0 Artifact P0-A2
Simulates inference latency distribution, computes percentiles,
and models GPU cost for enterprise inference planning.
Domain: AI infrastructure cost planning.
"""

import random
import math
import argparse
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s — %(levelname)s — %(message)s'
)
logger = logging.getLogger(__name__)


def generate_latency_samples(n: int = 10000) -> list[float]:
    """
    Generate realistic inference latency samples.
    Models a bimodal distribution: fast cached responses
    and slower full-inference responses.
    """
    random.seed(42)
    samples = []
    for _ in range(n):
        if random.random() < 0.7:
            latency = random.gauss(120, 30)
        else:
            latency = random.gauss(450, 80)
        samples.append(max(10.0, latency))
    logger.info(f"Generated {n} latency samples")
    return samples


def compute_percentiles(samples: list[float]) -> dict:
    """Compute key percentiles from latency samples."""
    if not samples:
        raise ValueError("No samples provided")

    sorted_samples = sorted(samples)
    n = len(sorted_samples)

    def pct(p: float) -> float:
        index = int(math.ceil(n * p / 100)) - 1
        return round(sorted_samples[max(0, index)], 2)

    return {
        'count': n,
        'min_ms': round(min(sorted_samples), 2),
        'max_ms': round(max(sorted_samples), 2),
        'mean_ms': round(sum(sorted_samples) / n, 2),
        'p50_ms': pct(50),
        'p95_ms': pct(95),
        'p99_ms': pct(99),
        'p99_9_ms': pct(99.9),
    }


def compute_gpu_cost_model(
    tokens_per_second: float,
    cost_per_hour: float,
    daily_requests: int,
    avg_tokens_per_request: int
) -> dict:
    """
    Simple GPU cost model for inference planning.
    Answers: how much does it cost to serve N requests/day?
    """
    tokens_per_day = daily_requests * avg_tokens_per_request
    gpu_hours_per_day = tokens_per_day / (tokens_per_second * 3600)
    daily_cost = gpu_hours_per_day * cost_per_hour
    monthly_cost = daily_cost * 30
    cost_per_1m_tokens = (cost_per_hour / tokens_per_second
                          / 3600 * 1_000_000)

    return {
        'tokens_per_day': int(tokens_per_day),
        'gpu_hours_per_day': round(gpu_hours_per_day, 3),
        'daily_cost_usd': round(daily_cost, 4),
        'monthly_cost_usd': round(monthly_cost, 2),
        'cost_per_1m_tokens_usd': round(cost_per_1m_tokens, 4),
    }


def print_latency_report(percentiles: dict) -> None:
    print("\n" + "="*50)
    print("  INFERENCE LATENCY ANALYSIS")
    print("="*50)
    print(f"  Samples:          {percentiles['count']:,}")
    print(f"  Min:              {percentiles['min_ms']} ms")
    print(f"  Mean:             {percentiles['mean_ms']} ms")
    print(f"  p50 (median):     {percentiles['p50_ms']} ms")
    print(f"  p95:              {percentiles['p95_ms']} ms")
    print(f"  p99:              {percentiles['p99_ms']} ms")
    print(f"  p99.9:            {percentiles['p99_9_ms']} ms")
    print(f"  Max:              {percentiles['max_ms']} ms")
    print("="*50)


def print_cost_report(cost: dict) -> None:
    print("\n" + "="*50)
    print("  GPU INFERENCE COST MODEL")
    print("="*50)
    print(f"  Tokens/day:       {cost['tokens_per_day']:,}")
    print(f"  GPU hours/day:    {cost['gpu_hours_per_day']}")
    print(f"  Daily cost:       ${cost['daily_cost_usd']}")
    print(f"  Monthly cost:     ${cost['monthly_cost_usd']}")
    print(f"  Cost/1M tokens:   ${cost['cost_per_1m_tokens_usd']}")
    print("="*50 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description='Inference latency and GPU cost calculator'
    )
    parser.add_argument('--samples', type=int, default=10000)
    parser.add_argument('--tokens-per-sec', type=float, default=180.0)
    parser.add_argument('--cost-per-hour', type=float, default=2.50)
    parser.add_argument('--daily-requests', type=int, default=10000)
    parser.add_argument('--avg-tokens', type=int, default=500)
    args = parser.parse_args()

    samples = generate_latency_samples(args.samples)
    percentiles = compute_percentiles(samples)
    print_latency_report(percentiles)

    cost = compute_gpu_cost_model(
        args.tokens_per_sec,
        args.cost_per_hour,
        args.daily_requests,
        args.avg_tokens
    )
    print_cost_report(cost)


if __name__ == "__main__":
    main()