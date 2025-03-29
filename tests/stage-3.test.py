from user.calculator import multiply

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(0, 10) == 0
    assert multiply(-2, 4) == -8
