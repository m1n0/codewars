# https://www.codewars.com/kata/554c8a93e466e794fe000001
def point_vs_vector(point, vector):
    xC, yC = point
    [xA, yA], [xB, yB] = vector

    cross = (xB - xA) * (yC - yA) - (yB - yA) * (xC - xA)
    return -1 if cross > 0 else 1 if cross < 0 else 0