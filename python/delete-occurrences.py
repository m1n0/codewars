# https://www.codewars.com/kata/554ca54ffa7d91b236000023/train/python
def delete_nth(order,max_e):
    elements = {}
    res = []
    for n in order:
        if n in elements:
            if elements[n] < max_e:
                elements[n] += 1
                res.append(n)
        else:
            elements[n] = 1
            res.append(n)

    return res
