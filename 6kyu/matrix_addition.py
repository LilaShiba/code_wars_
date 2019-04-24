def matrix_addition(a, b):
    for x in range(len(a)):
        for y in range(len(a[0])):
            a[x][y] = a[x][y] + b[x][y]
    return a
