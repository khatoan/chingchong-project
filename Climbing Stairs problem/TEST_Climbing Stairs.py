from Recursive_ver import countWays
from Recursive_ver import Recursive_count
from Iterative_ver import Iterative_count


def test_countWays():
    assert countWays(3) == 3, "Test case 1 failed"
    assert countWays(5) == 8, "Test case 2 failed"
    assert countWays(2) == 2, "Test case 3 failed"
    assert countWays(1) == 1, "Test case 4 failed"
    assert countWays(0) == 1, "Test case 5 failed"
    assert countWays(None) == 0, "Test case 6 failed"
    assert countWays("a") == 0, "Test case 7 failed"
    print("All test cases passed for countWays")


def test_Iterative_count():
    assert Iterative_count(3) == 3, "Test case 1 failed"
    assert Iterative_count(5) == 8, "Test case 2 failed"
    assert Iterative_count(2) == 2, "Test case 3 failed"
    assert Iterative_count(1) == 1, "Test case 4 failed"
    assert Iterative_count(0) == 1, "Test case 5 failed"
    assert Iterative_count(None) == 0, "Test case 6 failed"
    assert Iterative_count("a") == 0, "Test case 7 failed"
    print("All test cases passed for Iterative_count")


test_Iterative_count()
test_countWays()
