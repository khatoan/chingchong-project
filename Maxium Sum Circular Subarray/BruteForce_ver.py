def circularSubaraySum_BruteForce(nums: list):
    if not check_input(nums):
        return 0
    gloabl_max = nums[0]
    n = len(nums)
    for i in range(n):
        curr_Sum = 0
        for j in range(n):
            index = (i + j) % n
            curr_Sum += nums[index]
            gloabl_max = max(gloabl_max, curr_Sum)
    return gloabl_max


def check_input(nums):
    if not isinstance(nums, list) or nums == None or nums == []:
        return False
    for i in nums:
        if not isinstance(i, int):
            return False
    return True


if __name__ == "__main__":
    nums = [5, -3, 5]
    print(circularSubaraySum_BruteForce(nums))
