# https://www.codewars.com/kata/difference-between-two-collections
def diff(a, b):
    return sorted(list(set([c for c in a if c not in b] + [c for c in b if c not in a])))