# Return the nth Fibonacci number
def fibo(n, memo):
    if memo[n] != None:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fibo(n - 1, memo) + fibo(n - 2, memo)
    return memo[n]


def fiboRecur(n):
    memo = [None] * (n + 1)
    return fibo(n, memo)
