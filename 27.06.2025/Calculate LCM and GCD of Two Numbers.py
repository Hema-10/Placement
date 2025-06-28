import math

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

print(lcm(15, 20))  # 60
