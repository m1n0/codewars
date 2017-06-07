# https://www.codewars.com/kata/525caa5c1bf619d28c000335
def isSolved(board):
    n = 3
    score = [0] * (2 * n + 2)
    finished = True
    for i, row in enumerate(board):
        for j, el in enumerate(row):
            if el == 0:
                finished = False
            else:
                val = 1 if el == 1 else -1
                score[i] += val
                score[n + j] += val
                if i == j:
                    score[2 * n] += val
                if (i == 0 and j == 3) or (i == 2 and j == 2) or (i == 3 and j == 0):
                    score[2 * n + 1] += val

    for i in score:
        if i >= n:
            return 1
        elif i <= -n:
            return 2
    if finished:
        return 0
    else:
        return -1
