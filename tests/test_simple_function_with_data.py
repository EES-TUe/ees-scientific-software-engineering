import json
from pathlib import Path

from ees_scientific_software_engineering.simple_function import multiply

DATA_PATH = Path(__file__).parent / "data"


def test_multiply_from_data():
    with open(DATA_PATH / "test_multiply.json") as f:
        data = json.load(f)
    assert multiply(data["x"], data["y"]) == data["expected"]
