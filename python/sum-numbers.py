# https://www.codewars.com/kata/54df2067ecaa226eca000229
from functools import reduce

def f(n):
    if isinstance(n, int) and n > 0:
        return reduce(lambda x, y : x + y, range(0, n + 1))
