def lcs(str_a, i, str_b, j, rem):

    if i < 0 or j < 0:
        best_lcs = ''
    elif rem[i][j] != -1:
        return rem[i][j]
    elif str_a[i] == str_b[j]:
        best_lcs = lcs(str_a[:i], i-1, str_b[:j], j-1, rem) + str_a[i]
        #print('checking: {} at {} versus {} at {} : {} <=> {} => {}'.format(str_a[:i+1], i, str_b[:j+1], j, str_a[i], str_b[j], best_lcs))
        rem[i][j] = best_lcs
    else:
        lcs_1 = lcs(str_a[:i], i-1, str_b[:j+1], j, rem)
        lcs_2 = lcs(str_a[:i+1], i, str_b[:j], j-1, rem)
        if len(lcs_1) > len(lcs_2):
            best_lcs = lcs_1
        else:
            best_lcs = lcs_2
        rem[i][j] = best_lcs
        #print('checking: {} at {} versus {} at {} : {} <=> {} => {}'.format(str_a[:i+1], i, str_b[:j+1], j, str_a[i], str_b[j], best_lcs))

    return best_lcs


def lcs_bottom_up(str_a, str_b):
    rem = [[-1] * (len(str_a) + 1) for _ in range(len(str_b) + 1)]
    for j in range(len(str_a) + 1):
        rem[0][j] = ''
    for i in range(len(str_b) + 1):
        rem[i][0] = ''

    for j in range(1, len(str_a) + 1):
        for i in range(1, len(str_b)+1):
            if str_a[j - 1] == str_b [i - 1]:
                rem[i][j] = rem[i-1][j-1] + str_a[j - 1]
            else:
                if len(rem[i][j-1]) > len(rem[i-1][j]):
                    rem[i][j] = rem[i][j-1]
                else:
                    rem[i][j] = rem[i-1][j]

    return rem

x = 'ABCBDAB'
y = 'CBDCABA'

rem = [[-1] * len(y) for _ in range(len(x))]
print(x)
print(y)
print(lcs(x, len(x)-1, y, len(y) -1, rem))
for row in rem:
    print(row)

rem_mat = lcs_bottom_up(x, y)
for row in rem_mat:
    print(row)


a = '10010101'
b = '010110110'
rem = [[-1] * len(b) for _ in range(len(a))]
print(a)
print(b)
print(lcs(a, len(a)-1, b, len(b) -1, rem))
for row in rem:
    print(row)

print()
rem_mat = lcs_bottom_up(a, b)
for row in rem_mat:
    print(row)
