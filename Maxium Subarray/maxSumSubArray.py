# Given an integer array nums, find the subarray with the largest sum, and return its sum.
def maxSumSubArray(nums):
    if not check_input(nums):
        return 0
    global_max = nums[0]
    local_max = nums[0]
    for i in range(1, len(nums)):
        local_max = max(nums[i], local_max + nums[i])
        global_max = max(global_max, local_max)
    return global_max


def check_input(nums):
    if not isinstance(nums, list) or nums == None or nums == []:
        return False
    for i in nums:
        if not isinstance(i, int):
            return False
    return True


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maxSumSubArray(nums))
