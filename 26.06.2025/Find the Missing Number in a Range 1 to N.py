def missing_number(arr, n):
    return n*(n+1)//2 - sum(arr)

arr = [1, 2, 4, 5, 6]
print(missing_number(arr, 6))
