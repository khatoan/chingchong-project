# Return the nth Fibonacci number
def fibo(n, memo):
    if memo[n] != None:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibo(n - 1, memo) + fibo(n - 2, memo)
    return memo[n]


def fiboRecur(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a positive integer")
    memo = [None] * (n + 1)
    return fibo(n, memo)
