# Problem: Climbing Stairs problem
# You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps.
# In how many distinct ways can you climb to the top?


def Iterative_count(n):
    if not isinstance(n, int) or n < 0:
        return 0
    dp = [0] * (n + 1)
    dp[0] = 1
    steps = [1, 2]
    for i in range(1, n + 1):
        for step in steps:
            if i - step >= 0:
                dp[i] += dp[i - step]

    return dp[n]


if __name__ == "__main__":
    n = 5
    print(countWays(n))
