matrix = [[1, 2, 3], [4, 5, 6]]
transpose = [list(row) for row in zip(*matrix)]
print(transpose)
