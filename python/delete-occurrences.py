# https://www.codewars.com/kata/554ca54ffa7d91b236000023/train/python
def delete_nth(order,max_e):
    res = []
    for n in order:
        if res.count(n) < max_e: res.append(n)
    return res
