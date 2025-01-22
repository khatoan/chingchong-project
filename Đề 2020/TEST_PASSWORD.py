from PASSWORD import file_input, file_output, find_password


def test_functions():
    assert find_password(5, 12) == 93000, "Test case 1 failed"
    assert find_password(5, 10) == 91000, "Test case 2 failed"
    assert find_password(3, 28) == -1, "Test case 3 failed"
    assert find_password(1, 0) == 0, "Test case 4 failed"
    assert find_password(0, 0) == -1, "Test case 5 failed"
    assert find_password(2, 18) == 99, "Test case 6 failed"
    print("All test cases passed")


test_functions()
