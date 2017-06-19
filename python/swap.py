# https://www.codewars.com/kata/572edd4cd59ee714b90004e6
def swap(matrix, row1, row2, *columns):
    for i in columns:
        matrix[row1][i], matrix[row2][i] = matrix[row2][i], matrix[row1][i]
    return matrix