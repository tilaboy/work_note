def matrix_trace(matrix, size):
    sum = 0
    for index in range(size):
        sum += matrix[index][index]
    return sum

def getPermutations(array):
    if len(array) == 1:
        yield array
    else:
        for i in range(len(array)):
            perms = getPermutations(array[:i] + array[i+1:])
            for p in perms:
                yield [array[i], *p]


def generate(m_size, top_left_number):
    rows_counter = 0
    matrix = []
    for rows in range(1, m_size + 1):
        latin_number = top_left_number + (rows - 1)
        if latin_number > m_size:
            latin_number = 1 + rows_counter
            rows_counter += 1
        row_counter = 0
        row = []
        for row_i in range(1, m_size + 1):
            row.append(latin_number)
            latin_number += 1
            if latin_number > m_size:
                latin_number = 1 + row_counter
                row_counter += 1
        matrix.append(row)
    return matrix

def row_pertub_match(matrix, m_size, m_trace):
    for permutation in getPermutations(list(range(m_size))):
        perm_matrix = [matrix[row] for row in permutation]
        if matrix_trace(perm_matrix, m_size) == m_trace:
            return perm_matrix

def transpose_m(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

def column_pertub_match(matrix, m_size, m_trace):
    t_matrix = transpose_m(matrix)
    for permutation in getPermutations(list(range(m_size))):
        perm_matrix = [t_matrix[row] for row in permutation]
        perm_matrix = transpose_m(perm_matrix)
        if matrix_trace(perm_matrix, m_size) == m_trace:
            return perm_matrix


total_case = int(input())

for case_i in range(total_case):
    m_size, m_trace = map(int, input().split(" "))
    for number in range(1, m_size + 1):
        matrix = generate(m_size, number)
        if matrix_trace(matrix, m_size) == m_trace:
            print('Case #{}: POSSIBLE'.format(case_i +1))
            for row in matrix:
                print(" ".join([str(ele) for ele in row]))
            break
        r_matrix = row_pertub_match(matrix, m_size, m_trace)
        if r_matrix:
            print('Case #{}: POSSIBLE'.format(case_i +1))
            for row in r_matrix:
                print(" ".join([str(ele) for ele in row]))
            break
        c_matrix = column_pertub_match(matrix, m_size, m_trace)
        if c_matrix:
            print('Case #{}: POSSIBLE'.format(case_i +1))
            for row in c_matrix:
                print(" ".join([str(ele) for ele in row]))
            break

    else:
        print('Case #{}: IMPOSSIBLE'.format(case_i +1))
