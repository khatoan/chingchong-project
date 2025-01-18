from canStopRecursive import CanstopRecursive
from canStopIterative import canStopIterative
from canStopRecursiveWithMemo import canStopRecursiveWithMemo

runway_1 = [True, True, True, True, True]
runway_2 = [True, False, True, True, False]
runway_3 = [True, False, False, False, False]
runway_4 = []
runway_5 = [True, False, 1, False, True]
runway_6 = None


def test_canStopRecursive():
    assert CanstopRecursive(runway_1, 2, 0) == True, "Test case 1 failed"
    assert CanstopRecursive(runway_2, 2, 0) == True, "Test case 2 failed"
    assert CanstopRecursive(runway_3, 2, 0) == False, "Test case 3 failed"
    assert CanstopRecursive(runway_4, 2, 0) == False, "Test case 4 failed"
    assert CanstopRecursive(runway_5, 2, 0) == False, "Test case 5 failed"
    assert CanstopRecursive(runway_6, 2, 0) == False, "Test case 6 failed"
    assert CanstopRecursive(runway_1, None, 1) == False, "Test case 7 failed"
    assert CanstopRecursive(runway_1, 2, None) == False, "Test case 8 failed"
    assert CanstopRecursive(runway_1, 2, 10) == False, "Test case 9 failed"
    assert CanstopRecursive(runway_1, "a", "b") == False, "Test case 10 failed"
    print("All test cases passed for canStopRecursive")


def test_canStopIterative():
    assert canStopIterative(runway_1, 2, 0) == True, "Test case 1 failed"
    assert canStopIterative(runway_2, 2, 0) == True, "Test case 2 failed"
    assert canStopIterative(runway_3, 2, 0) == False, "Test case 3 failed"
    assert canStopIterative(runway_4, 2, 0) == False, "Test case 4 failed"
    assert canStopIterative(runway_5, 2, 0) == False, "Test case 5 failed"
    assert canStopIterative(runway_6, 2, 0) == False, "Test case 6 failed"
    assert canStopIterative(runway_1, None, 1) == False, "Test case 7 failed"
    assert canStopIterative(runway_1, 2, None) == False, "Test case 8 failed"
    assert canStopIterative(runway_1, 2, 10) == False, "Test case 9 failed"
    assert canStopIterative(runway_1, "a", "b") == False, "Test case 10 failed"
    print("All test cases passed for canStopIterative")


def test_canStopRecursiveWithMemo():
    assert canStopRecursiveWithMemo(runway_1, 2, 0) == True, "Test case 1 failed"
    assert canStopRecursiveWithMemo(runway_2, 2, 0) == True, "Test case 2 failed"
    assert canStopRecursiveWithMemo(runway_3, 2, 0) == False, "Test case 3 failed"
    assert canStopRecursiveWithMemo(runway_4, 2, 0) == False, "Test case 4 failed"
    assert canStopRecursiveWithMemo(runway_5, 2, 0) == False, "Test case 5 failed"
    assert canStopRecursiveWithMemo(runway_6, 2, 0) == False, "Test case 6 failed"
    assert canStopRecursiveWithMemo(runway_1, None, 1) == False, "Test case 7 failed"
    assert canStopRecursiveWithMemo(runway_1, 2, None) == False, "Test case 8 failed"
    assert canStopRecursiveWithMemo(runway_1, 2, 10) == False, "Test case 9 failed"
    assert canStopRecursiveWithMemo(runway_1, "a", "b") == False, "Test case 10 failed"
    print("All test cases passed for canStopRecursiveWithMemo")


test_canStopIterative()
test_canStopRecursive()
test_canStopRecursiveWithMemo()
