# [1, 2, [3, 4], [5[6, 7]], [8[9[10, 11]]]]


def sumtree(l):
    total = 0
    for x in l:
        if not isinstance(x, list):
            total += x
        else:
            total += sumtree(x)
    return total


l = [1, [2, [3, 4], 5], 6, [7, 8]]
print(sumtree(l))
print(sumtree([1, 2,[3, 4, [5, 6,], [7, 8, [9, 10]]]]))