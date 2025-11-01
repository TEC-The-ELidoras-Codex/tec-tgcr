import sys
import os
import pytest
# ensure src is importable when running tests without installing package
ROOT = os.path.dirname(os.path.dirname(__file__))
SRC = os.path.join(ROOT, "src")
if SRC not in sys.path:
    sys.path.insert(0, SRC)
from resonance_notebook import ingest


def test_find_and_load_latest_ingest():
    p = ingest.find_latest_ingest()
    if p is None:
        pytest.skip("No ingest JSON present in data/digital_assets/brand/ingests")
    data = ingest.load_ingest(p)
    assert isinstance(data, dict)
    assert "metadata" in data
    assert "content" in data
    stats = ingest.summary_stats(data)
    assert isinstance(stats.get("words"), int)
    assert isinstance(stats.get("chars"), int)
