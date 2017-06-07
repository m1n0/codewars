# https://www.codewars.com/kata/mumbling/train/python
def accum(s):
    return "-".join([c.upper() + c.lower() * i for i, c in enumerate(s)])

print(accum("ZpglnRxqenU"))
