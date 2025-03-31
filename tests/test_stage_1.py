# tests/test_stage_1.py

import sys
import os
import pytest

# Dynamically add the path to the student's submission folder
sys.path.insert(0, os.path.abspath('../student'))

try:
    from calculator import add
except ImportError:
    pytest.fail("❌ Could not import 'add' from calculator.py. Make sure the file exists and defines a function named 'add'.")

def test_add_positive_numbers():
    result = add(2, 3)
    assert result == 5, f"❌ Expected add(2, 3) to return 5, but got {result}"

def test_add_zero():
    result = add(0, 0)
    assert result == 0, f"❌ Expected add(0, 0) to return 0, but got {result}"

def test_add_negative():
    result = add(-1, -1)
    assert result == -2, f"❌ Expected add(-1, -1) to return -2, but got {result}"

def test_add_mixed():
    result = add(-3, 7)
    assert result == 4, f"❌ Expected add(-3, 7) to return 4, but got {result}"
