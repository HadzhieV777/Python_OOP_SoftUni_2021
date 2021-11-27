# 09. Possible permutations
from itertools import permutations


def possible_permutations(sequence):
    for permutation in permutations(sequence):
        yield list(permutation)


[print(n) for n in possible_permutations([1, 2, 3])]
[print(n) for n in possible_permutations([1])]
