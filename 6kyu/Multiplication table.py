"""
Your task, is to create N×N multiplication table, of size provided in parameter.

For example, when given size is 3:

1 2 3
2 4 6
3 6 9
For the given example, the return value should be:

[[1,2,3],[2,4,6],[3,6,9]]
"""

def multiplication_table(size: int) -> list[list]:
    res = []
    for i in range(1, size+1):
        row = []
        for j in range(1, size+1):
            row.append(j*i)
        res.append(row)

    return res
