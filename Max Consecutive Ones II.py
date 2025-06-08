# Given a binary string, find the maximum number of consecutive 1s in this string if you can flip at most one 0


def maxStr(s: str):
    if not checkinput(s):
        return "Invalid input"
    left = curr = ans = 0
    for right in range(len(s)):
        if s[right] == "0":
            curr += 1
        while curr > 1:
            if s[left] == "0":
                curr -= 1
            left += 1
        ans = max(ans, right - left + 1)
    return ans


def checkinput(s):
    if not isinstance(s, str) or len(s) == 0:
        return False
    if not all(c in "01" for c in s):
        return False
    return True


if __name__ == "__main__":
    s = "1101100111"
    print(maxStr(s))
