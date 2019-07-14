fib_memo = {}

def fib(n):

    if n in fib_memo:
        return fib_memo[n]
    else:
        fib_memo[n] = n if n < 2 else fib(n-1)+fib(n-2)
        return fib_memo[n]

print(fib(40))
