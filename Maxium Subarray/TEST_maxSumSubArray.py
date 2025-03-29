from maxSumSubArray import maxSumSubArray

nums_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums_2 = [1]
nums_3 = [5, 4, -1, 7, 8]
nums_4 = []
nums_5 = None


def Test_maxSumSubArray():
    assert maxSumSubArray(nums_1) == 6, "Test case 1 failed"
    assert maxSumSubArray(nums_2) == 1, "Test case 2 failed"
    assert maxSumSubArray(nums_3) == 23, "Test case 3 failed"
    assert maxSumSubArray(nums_4) == 0, "Test case 4 failed"
    assert maxSumSubArray(nums_5) == 0, "Test case 5 failed"
    print("All test cases passed for maxSumSubArray")


Test_maxSumSubArray()
