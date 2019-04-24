def flatten_and_sort(matrix):
    new_matrix = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            new_matrix.append(matrix[row][col])
    new_matrix.sort()
    return(new_matrix)
