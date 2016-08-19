# https://www.codewars.com/kata/54ca3e777120b56cb6000710/train/python
def chained(functions):
    def apply(param):
        result = param
        for f in functions:
            result = f(result)
        return result
    return apply
