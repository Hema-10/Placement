from itertools import permutations

def all_perms(s):
    return [''.join(p) for p in permutations(s)]

print(all_perms("abc"))
