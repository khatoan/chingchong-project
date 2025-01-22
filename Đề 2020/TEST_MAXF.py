from MAXF import main_2


def test_functions():
    assert main_2(5, [4, 6, 9, 2, 1]) == (4, 6), "Test case 1 failed"
    assert main_2(5, [1, 2, 1, 10, 20]) == (1, 2), "Test case 2 failed"
    assert main_2(3, [4, 4, 4]) == -1, "Test case 3 failed"
    print("All test cases passed")


test_functions()
