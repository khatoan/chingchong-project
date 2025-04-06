from Kadane_ver import circularSubaraySum
from BruteForce_ver import circularSubaraySum_BruteForce

nums_1 = [1, -2, 3, -2]
nums_2 = [5, -3, 5]
nums_3 = [-3, -2, -3]
nums_4 = []
nums_5 = None
nums_6 = [2, 3, "-2", -1]


def test_circularSubaraySum():
    assert circularSubaraySum(nums_1) == 3, "Test case 1 failed"
    assert circularSubaraySum(nums_2) == 10, "Test case 2 failed"
    assert circularSubaraySum(nums_3) == -2, "Test case 3 failed"
    assert circularSubaraySum(nums_4) == 0, "Test case 4 failed"
    assert circularSubaraySum(nums_5) == 0, "Test case 5 failed"
    assert circularSubaraySum(nums_6) == 0, "Test case 6 failed"
    print("All test cases passed by circularSubaraySum!")


def test_circularSubaraySum_BruteForce():
    assert circularSubaraySum_BruteForce(nums_1) == 3, "Test case 1 failed"
    assert circularSubaraySum_BruteForce(nums_2) == 10, "Test case 2 failed"
    assert circularSubaraySum_BruteForce(nums_3) == -2, "Test case 3 failed"
    assert circularSubaraySum_BruteForce(nums_4) == 0, "Test case 4 failed"
    assert circularSubaraySum_BruteForce(nums_5) == 0, "Test case 5 failed"
    assert circularSubaraySum_BruteForce(nums_6) == 0, "Test case 6 failed"
    print("All test cases passed by circularSubaraySum_BruteForce!")


test_circularSubaraySum()
test_circularSubaraySum_BruteForce()
