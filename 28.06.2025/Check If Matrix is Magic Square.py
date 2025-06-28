def is_magic_square(matrix):
    n = len(matrix)
    s = sum(matrix[0])
    for row in matrix:
        if sum(row) != s: return False
    for col in zip(*matrix):
        if sum(col) != s: return False
    if sum(matrix[i][i] for i in range(n)) != s: return False
    if sum(matrix[i][n-i-1] for i in range(n)) != s: return False
    return True

magic = [[2,7,6],[9,5,1],[4,3,8]]
print(is_magic_square(magic))  # True
