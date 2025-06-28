import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"Execution Time: {end - start:.5f} seconds")
        return res
    return wrapper

@timer
def compute():
    total = sum(i**2 for i in range(10**6))
    return total

compute()
