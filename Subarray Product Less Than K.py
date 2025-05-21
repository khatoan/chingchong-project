# Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.
# https://leetcode.com/problems/subarray-product-less-than-k/description/


# Using sliding window
def count_sublist(a: list, k: int):
    if not check_input(a, k):
        return "Invalid input"
    ans = left = 0
    curr = 1
    if k <= 1:
        return 0
    for right in range(len(a)):
        curr *= a[right]
        while curr >= k:
            curr //= a[left]
            left += 1
        ans += right - left + 1
    return ans


def check_input(a: list, k: int):
    if not isinstance(a, list) or len(a) == 0 or not isinstance(k, int):
        return False
    if not all(isinstance(i, int) for i in a):
        return False
    return True


if __name__ == "__main__":
    nums = [10, 5, 2, 6]
    k = 100
    print(count_sublist(nums, k))
