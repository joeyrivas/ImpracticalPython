"""For a total number of columns, find all unique column arrangements.

Builds a list of lists containing all possible unique arrangements of
individual column numbers including negative values for route direction
(read up column vs. down).

Input:
-total number of columns

Returns:
-list of lists of unique column orders including negative values for
route cipher encryption direction

"""
from itertools import permutations, product

# build list of lists of column number combinations
# itertools product compute the cartesian product of input iterables
def perms(columns):
    """Take number of columns integer & generate pos & neg permutations."""
    results = []
    for perm in permutations(columns):
        for signs in product([-1, 1], repeat=len(columns)):
            results.append([i * sign for i, sign in zip(perm, signs)])
    return results
