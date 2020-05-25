from q2_1_2 import check_time
import random
import numpy as np


def get_matrix_shape(A):
    shape = []

    while (isinstance(A, list)):
        shape.append(len(A))
        A=A[0]
    return shape

@check_time
def maxtrix_multi(A, B):
    A_shape = get_matrix_shape(A)
    B_shape = get_matrix_shape(B)

    assert A_shape == B_shape
    assert len(A_shape) == 2
    assert len(B_shape) == 2
    assert A_shape[1] == B_shape[0]
    C = [
            [0 for row_i in range(A_shape[0])]
            for column_i in range(B_shape[1])
        ]

    for row_index in range(A_shape[0]):
        for column_index in range(B_shape[1]):
            for element_index in range(A_shape[1]):
                C[row_index][column_index] += A[row_index][element_index] * B[element_index][column_index]
    return C







A = [[2, 3, 5, 7], [5, 1, 2, 7], [1, 4, 2, 5], [5, 7, 2, 6]]
B = [[8, 1, 2, 5], [3, 7, 4, 1], [9, 6, 2, 8], [2, 7, 6, 5]]

C= maxtrix_multi(A, B)
print(C)
A_np = np.array(A)
B_np = np.array(B)

C_np = np.matmul(A_np, B_np)
print(C_np.tolist())
