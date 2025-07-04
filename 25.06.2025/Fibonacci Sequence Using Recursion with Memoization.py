from functools import lru_cache

@lru_cache(None)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print([fib(i) for i in range(10)])
