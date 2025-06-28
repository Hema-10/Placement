def is_rotation(a, b):
    return len(a) == len(b) and b in a + a

print(is_rotation("abcd", "cdab"))  # True
