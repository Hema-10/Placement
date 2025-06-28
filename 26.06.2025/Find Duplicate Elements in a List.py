from collections import Counter

arr = [1, 2, 3, 2, 4, 5, 1]
duplicates = [item for item, count in Counter(arr).items() if count > 1]
print(duplicates)
