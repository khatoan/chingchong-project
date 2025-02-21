"""
You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top? 
"""


def Recursive_count(n, memo):

    # base case
    if n == 0:
        return 1
    if n == 1:
        return 1

    # If value is memoized
    if memo[n] != -1:
        return memo[n]

    # Memoize the state
    memo[n] = Recursive_count(n - 1, memo) + Recursive_count(n - 2, memo)

    return memo[n]


def countWays(n):
    if not isinstance(n, int) or n < 0:
        return 0
    memo = [-1] * (n + 1)
    return Recursive_count(n, memo)


if __name__ == "__main__":
    n = 100
    print(countWays(n))
