def read_matrix(size):
    matrix = []
    for row_i in range(size):
        line = list(map(int, input().split(" ")))
        matrix.append(line)
    return matrix

def matrix_trace(matrix, size):
    sum = 0
    for index in range(size):
        sum += matrix[index][index]
    return sum

def has_repeated_elements(arr):
    seen = list()
    has_repeated = False
    for element in arr:
        if element in seen:
            has_repeated = True
            break
        else:
            seen.append(element)
    return has_repeated

total_cases = int(input())

for case_i in range(total_cases):
    matrix_size = int(input())
    matrix = read_matrix(matrix_size)
    dia_sum = matrix_trace(matrix, matrix_size)
    repeated_row = 0
    repeated_column = 0
    for row_i in range(matrix_size):
        if has_repeated_elements(matrix[row_i]):
            repeated_row += 1
        column = [row[row_i] for row in matrix]
        if has_repeated_elements(column):
            repeated_column += 1

    print("Case #{}: {} {} {}".format(case_i + 1, dia_sum, repeated_row, repeated_column))
