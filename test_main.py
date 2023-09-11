from main import add


def test_func_positive():
    result = add(3, 5)
    template = 8
    assert result == template


def test_func_negative():
    result = add(-2, -3)
    template = -5
    assert result == template


def test_func_pos_neg():
    result = add(1, -3)
    template = -2
    assert result == template


if __name__ == "__main__":
    test_func_positive()
    test_func_negative()
    test_func_pos_neg()
    print("All test passed")
