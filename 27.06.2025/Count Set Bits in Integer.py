def count_set_bits(n):
    return bin(n).count('1')

print(count_set_bits(29))  # 11101 → 4
