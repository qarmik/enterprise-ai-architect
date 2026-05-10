#!/usr/bin/env python3
"""
test-hello.py -Tests for hello.py
Rule: every artifact has a companion test file.
"""
import subprocess
import sys

def test_hello_runs_without_error():
    """hello.py must execute without raising an exception."""
    result = subprocess.run(
        [sys.executable, "phase-0/hello.py"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, (
        f"hello.py exited with code{result.returncode}\n"
        f"stderr: {result.stderr}"
    )
def test_hello_outpout_contains_required_fields():
    """Output must contain the four required fields."""
    result = subprocess.run(
        [sys.executable,"phase-0/hello.py"],
        capture_output=True,
        text=True
    )
    output = result.stdout
    assert "Enterprise AI Systems Architect" in output
    assert "42 months" in output
    assert "Banking" in output
    assert "2029" in output 
