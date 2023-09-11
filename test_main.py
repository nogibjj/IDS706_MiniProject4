from main import add

def test_func(a, b):
    result = add(a, b)
    template = a+b
    assert result == template

if __name__ == "__main__":
    test_func(1, 2)
    test_func(3, 4)
    test_func(-2, -3)
    print("All test passed")