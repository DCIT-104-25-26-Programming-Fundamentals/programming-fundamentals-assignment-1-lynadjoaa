def read_matrix(name):
    rows = int(input(f"Enter number of rows for Matrix {name}: "))
    cols = int(input(f"Enter number of columns for Matrix {name}: "))
    matrix = []
    for i in range(rows):
        row_input = input(f"Enter row {i+1}: ")
        row = list(map(int, row_input.split()))
        matrix.append(row)
    return matrix, rows, cols

def print_matrix(matrix):
    for row in matrix:
        for num in row:
            print(num, end=" ")
        print()

def transpose_matrix(matrix, rows, cols):
    transposed = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)
    return transposed

def add_matrices(mat1, mat2, rows, cols):
    result = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(mat1[i][j] + mat2[i][j])
        result.append(new_row)
    return result

def multiply_matrices(mat1, rows1, cols1, mat2, rows2, cols2):
    result = []
    for i in range(rows1):
        new_row = []
        for j in range(cols2):
            sum_val = 0
            for k in range(cols1):
                sum_val += mat1[i][k] * mat2[k][j]
            new_row.append(sum_val)
        result.append(new_row)
    return result

