from user.calculator import divide

def test_divide():
    assert divide(6, 2) == 3
    assert divide(5, 2) == 2.5
    try:
        divide(5, 0)
        assert False  # Should not reach here
    except ZeroDivisionError:
        assert True
