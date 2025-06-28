def flatten(lst):
    flat = []
    for item in lst:
        if isinstance(item, list):
            flat.extend(flatten(item))
        else:
            flat.append(item)
    return flat

print(flatten([1, [2, [3, 4], 5], 6]))  # [1, 2, 3, 4, 5, 6]
