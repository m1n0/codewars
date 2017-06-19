# http://www.codewars.com/kata/rudimentary-pivot-table
def pivot(two_dimensional_array, index_to_pivot):
    pivot_dict = {}

    for record in two_dimensional_array:
        pivot_row = record[index_to_pivot]

        if pivot_row in pivot_dict:
            pivot_dict[pivot_row] = add_rows(pivot_dict[pivot_row], extract_row(record, index_to_pivot))
        else:
            pivot_dict[pivot_row] = extract_row(record, index_to_pivot)

    return sorted(pivot_dict.values(), key=lambda x: x[index_to_pivot])


def extract_row(row, index_to_pivot):
    out = []
    for i, val in enumerate(row):
        if i != index_to_pivot:
            res_val = '-'
            try:
                res_val = int(val)
            except ValueError:
                pass
            try:
                res_val = float(val)
            except ValueError:
                pass
        out.append(res_val)
    return out


def add_rows(row_1, row_2):
    out = []
    for i, val in enumerate(row_1):
        if isinstance(val, int) or isinstance(val, float):
            out.append(row_1[i] + row_2[i])
        else:
            out.append(val)
    return out


report = [
    ["Item 1", "Black", "123"],
    ["Item 1", "Red", "34"],
    ["Item 3", "Black", "4747"],
    ["Item 4", "Red", "35"]
]
print(pivot(report, 0))
