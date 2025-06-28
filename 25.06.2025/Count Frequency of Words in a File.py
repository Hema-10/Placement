from collections import Counter

with open("sample.txt", "r") as file:
    words = file.read().lower().split()
    freq = Counter(words)

print(freq)
