# https://www.codewars.com/kata/557dd2a061f099504a000088
def list_to_array(lst):
    ret = []
    ret.append(lst.value)
    while (lst.next):
        lst = lst.next
        ret.append(lst.value)

    return ret
