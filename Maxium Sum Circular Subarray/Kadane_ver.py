def circularSubaraySum(nums: list):
    if not check_input(nums):
        return 0
    total_sum = nums[0]
    global_max = nums[0]
    local_max = nums[0]
    global_min = nums[0]
    local_min = nums[0]
    for i in range(1, len(nums)):
        # To fidn maxium sum subarray
        local_max = max(nums[i], local_max + nums[i])
        global_max = max(global_max, local_max)

        # To find minium sum subarray
        local_min = min(nums[i], local_min + nums[i])
        global_min = min(global_min, local_min)

        total_sum += nums[i]
    if global_min == total_sum:
        return global_max
    return max(global_max, total_sum - global_min)


def check_input(nums):
    if not isinstance(nums, list) or nums == None or nums == []:
        return False
    for i in nums:
        if not isinstance(i, int):
            return False
    return True


if __name__ == "__main__":
    nums = [5, -3, 5]
    print(circularSubaraySum(nums))
