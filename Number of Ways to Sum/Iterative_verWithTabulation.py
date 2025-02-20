# Python program to expressn as sum of 1, 3, 5.
# Returns the number of  arrangements to form 'n'
def countWays(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    numbers = [1, 3, 5]
    for i in range(1, n + 1):
        dp[i] = 0
        for num in numbers:
            if i - num >= 0:
                dp[i] += dp[i - num]

    return dp[n]


if __name__ == "__main__":
    n = 7
    print(countWays(n))
