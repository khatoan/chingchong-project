# Python program to expressn as sum of 1, 3, 5.
# Returns the number of  arrangements to form 'n'
def countWays(n):
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        dp[i] = 0

        if i - 1 >= 0:
            dp[i] += dp[i - 1]
        if i - 3 >= 0:
            dp[i] += dp[i - 3]
        if i - 5 >= 0:
            dp[i] += dp[i - 5]

    return dp[n]


if __name__ == "__main__":
    n = 7
    print(countWays(n))
