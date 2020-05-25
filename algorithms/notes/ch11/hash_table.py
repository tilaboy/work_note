def probing(k, i, m, method=1):
    if method == 1:
        return (k + i) % m
    elif method == 2:
        return (k + i + 3 * i * i) % m

    elif method == 3:
        h2 = k % (m -1)
        return (k + i * h2) % m

def hash_insert(table, k):
    i = 0

arr = [10, 22, 31, 4, 15, 28, 17, 88, 59]
for method in range(1, 4):
    hash_table = []
    for ele in arr:
        i = 0
        pos = probing(ele, i, 11, method)
        while pos in hash_table:
            i = i + 1
            pos = probing(ele, i, 11, method)
        hash_table.append(pos)
        print(method, ele, pos, i)
    print(ele)
    print(hash_table)
