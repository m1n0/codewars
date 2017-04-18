# https://www.codewars.com/kata/5287e858c6b5a9678200083c
def narcissistic(value):
    total = 0
    valStr = str(value)
    digits = len(valStr)
    for x in valStr:
            total += int(x) ** digits
    return total == value
