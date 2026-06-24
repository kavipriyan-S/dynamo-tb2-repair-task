import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")

def test_criterion_1_valid_json():
    """1. Generate a valid JSON summary report at /app/report.json."""
    assert REPORT_PATH.exists(), "no report.json found"
    try:
        json.loads(REPORT_PATH.read_text())
    except json.JSONDecodeError:
        assert False, "report.json is not valid JSON"

def test_criterion_2_total_requests():
    """2. 'total_requests': An integer representing the total number of log entries (6)."""
    data = json.loads(REPORT_PATH.read_text())
    assert "total_requests" in data, "Missing key: total_requests"
    assert data["total_requests"] == 6, f"Expected 6 total_requests, got {data['total_requests']}"

def test_criterion_3_unique_ips():
    """3. 'unique_ips': An integer representing the total number of unique client IP addresses (3)."""
    data = json.loads(REPORT_PATH.read_text())
    assert "unique_ips" in data, "Missing key: unique_ips"
    assert data["unique_ips"] == 3, f"Expected 3 unique_ips, got {data['unique_ips']}"

def test_criterion_4_top_path():
    """4. 'top_path': A string representing the most frequently requested path ('/index.html')."""
    data = json.loads(REPORT_PATH.read_text())
    assert "top_path" in data, "Missing key: top_path"
    assert data["top_path"] == "/index.html", f"Expected top_path /index.html, got {data['top_path']}"