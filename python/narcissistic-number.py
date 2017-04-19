# https://www.codewars.com/kata/5287e858c6b5a9678200083c
import time

def narcissistic(value):
    total = 0
    valStr = str(value)
    digits = len(valStr)
    for x in valStr:
            total += int(x) ** digits
    return total == value

def narcissisticFunctional(value):
    power = len(str(value))
    return value == reduce(lambda x, y : x + y, [int(i) ** power for i in str(value)])

def narcissisticFunctionalOptimised(value):
    power = len(str(value))
    valStr = str(value)
    return value == reduce(lambda x, y : x + y, [int(i) ** power for i in valStr])

start_time = time.time()
narcissistic(125287394239244)
print("--- %s seconds ---" % (time.time() - start_time)) # ~0.000022888183593s

start_time = time.time()
narcissisticFunctional(125287394239244)
print("--- %s seconds ---" % (time.time() - start_time)) # ~0.000671863555908s

start_time = time.time()
narcissisticFunctionalOptimised(125287394239244)
print("--- %s seconds ---" % (time.time() - start_time)) # ~0.000024080276489s
