# https://www.codewars.com/kata/mumbling/train/python
def accum(s):
    return "-".join([c.upper() + c.lower() * i for i, c in enumerate(s)])

def accum_traditional(s):
    groups = []
    for i, c in enumerate(s):
        groups.append((c + c * i).capitalize())
    return "-".join(groups)

print(accum("ZpglnRxqenU"))
print(accum_traditional("ZpglnRxqenU"))
