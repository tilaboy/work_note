
# 100 x 10, 10 x 20, 20 x 50, 50 x 5
dims = [100, 10, 20, 50, 5, 30, 200, 40, 60]

# if ((1,2),(3,4)) = > (100x20) x (20x5) => 100 x 5
def cost(i, k, j):
    return dims[i] * dims[j] * dims[k]

def ma_mul_cost (dims, i, j, costs, splits):
    min_cost = 2**256
    min_posi = 0
    if costs[i][j] > 0:
        min_cost = costs[i][j]
    elif i == j:
        min_cost = costs[i][i]
    else:
        for k in range(i, j):
            # cost,
            mm_cost = ma_mul_cost(dims, i, k, costs, splits) + ma_mul_cost(dims, k+1, j, costs, splits) + cost(i-1, k, j)
            if min_cost > mm_cost:
                min_cost = mm_cost
                min_posi = k
        costs[i][j] = min_cost
        splits[i][j] = min_posi

    return min_cost


def matrix_mul_recur(dims):
    costs = [[0] * len(dims) for i in range( len(dims))]
    splits = [[0] * len(dims) for i in range( len(dims))]
    for i in range(len(dims)):
        costs[i][i] = 0
    best = ma_mul_cost(dims, 1, len(dims) - 1, costs, splits)
    print(best)
    for row in costs:
        print(row)
    for row in splits:
        print(row)

    n = len(dims) - 2
    best_splits(1, len(dims) - 1, splits)

def best_splits(i, j, splits):
    k = splits[i][j]
    if k == 0:
        return
    else:
        print(k)
        best_splits(i, k, splits)

        best_splits(k+1, j, splits)


def matrix_mul_bottom_up(dims):
    costs = [ [0] * len(dims) for i in range(len(dims))]
    splits = [ [0] * (len(dims)) for i in range(len(dims))]

    for i in range(len(dims)):
        costs[i][i] = 0

    for l in range(1, len(dims) - 1):
        for i in range(1, len(dims) - l):
            j = i + l
            best_price = 2**256
            best_split = -1
            for k in range(i, j):
                local_cost = costs[i][k] + costs[k+1][j] + cost(i-1, k, j)
                if local_cost < best_price:
                    best_price = local_cost
                    best_split = k
            costs[i][j] = best_price
            splits[i][j] = best_split
    return costs, splits


costs, splits = matrix_mul_bottom_up(dims)
for row in costs:
    print(row)

print('')
for row in splits:
    print(row)

def print_seq(splits, i, j):
    if i == j:
        print ("A{}".format(i), end='')
    else:
        print("(", end='')
        print_seq(splits, i, splits[i][j])
        print_seq(splits, splits[i][j] + 1, j)
        print(")", end='')
print_seq(splits, 1, len(dims) - 1)
print()




matrix_mul_recur(dims)
