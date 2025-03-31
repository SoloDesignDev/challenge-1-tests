import sys
import os
import pytest

# Add student repo path to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../student')))

try:
    from calculator import add
except ImportError:
    pytest.fail("❌ Could not import 'add' from calculator.py. Make sure the file exists and defines a function named 'add'.")

def test_add_positive():
    result = add(2, 3)
    assert result == 5, f"❌ Expected add(2, 3) to return 5, but got {result}"

def test_add_zeros():
    result = add(0, 0)
    assert result == 0, f"❌ Expected add(0, 0) to return 0, but got {result}"

def test_add_negatives():
    result = add(-1, -1)
    assert result == -2, f"❌ Expected add(-1, -1) to return -2, but got {result}"

def test_add_mixed_signs():
    result = add(-5, 5)
    assert result == 0, f"❌ Expected add(-5, 5) to return 0, but got {result}"

def test_add_large_numbers():
    result = add(100000, 200000)
    assert result == 300000, f"❌ Expected add(100000, 200000) to return 300000, but got {result}"

def test_add_type_error():
    try:
        add("2", "3")
    except TypeError:
        pass  # This is expected
    else:
        pytest.fail("❌ Expected add('2', '3') to raise a TypeError, but it did not.")

def test_summary():
    print("✅ All functional tests ran. If there are no ❌ errors above, your function passed! 🎉")
