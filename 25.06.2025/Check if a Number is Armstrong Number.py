def is_armstrong(n):
    power = len(str(n))
    return n == sum(int(digit) ** power for digit in str(n))

print(is_armstrong(153))
