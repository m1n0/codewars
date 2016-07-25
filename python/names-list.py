# https://www.codewars.com/kata/53368a47e38700bd8300030d
import numpy

def namelist(names):
    l = len(names)
    if (l <= 0):
        return ''

    people = []
    for i in range(0, len(names)):
        people.append(names[i]['name'])
    partition = numpy.split(people, [l - 1, l])
    if (len(partition[0]) > 0):
        return (' & '.join([', '.join(partition[0]), partition[1][0]]))
    return partition[1][0]
