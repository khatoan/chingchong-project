# Python program to express n as sum of 1, 3, 5.
# Returns the number of  arrangements to form 'n'
def countWays(n):

    # base case
    if n < 0:
        return 0
    if n == 0:
        return 1

    return countWays(n - 1) + countWays(n - 3) + countWays(n - 5)


if __name__ == "__main__":
    n = 7
    print(countWays(n))
