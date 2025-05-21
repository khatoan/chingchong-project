# Given an array arr[] of size N and an integer K, the task is to find the length of the largest subarray having the sum of its elements <= K, where K > 0
# Using sliding window technique
def max_subarr(a: list, k: int):
    if not check_input(a, k):
        return None
    left = curr = max_len = best_left = best_right = 0
    for right in range(len(a)):
        curr += a[right]
        while curr > k:
            curr -= a[left]
            left += 1
        if curr <= k:
            if right - left + 1 > max_len:
                max_len = right - left + 1
                best_left = left
                best_right = right
    if max_len == 0:
        return None
    sub = a[best_left : best_right + 1]
    return max_len, best_left, sub


def check_input(a: list, k: int):
    if not isinstance(a, list) and len(a) == 0:
        return False
    if not isinstance(k, int) or k <= 0:
        return False
    for i in a:
        if not isinstance(i, int):
            return False
        if i < 0:
            return False
    return True


if __name__ == "__main__":
    a = [3, 2, 1, 3, 1, 1]
    k = 5
    result = max_subarr(a, k)
    if result == None:
        print("No subarray found")
    else:
        max_len, best_left, sub = result
        print(f"Length of subarray: {max_len}")
        print(f"position: {best_left}")
        print(f"Subarray: {sub}")
