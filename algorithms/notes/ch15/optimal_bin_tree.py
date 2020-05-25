
def weight(p, q, i, j):
    return sum(p[i:j+1]) + sum(q[i-1:j+1])

def op_bt(p, q, start, end, e_m, w_m):
    best_prob = 10000
    if e_m[start][end] > 0:
        return e_m[start][end]
    elif end < start:
        best_prob = q[end]
    else:
        for k in range(start, end+1):
            if w_m[start][end] < 0:
                w_m[start][end] = weight(p, q, start, end)

            prob = op_bt(p, q, start, k-1, e_m, w_m) + op_bt(p, q, k+1, end, e_m, w_m) + w_m[start][end]
            #print(start, end, w, prob)
            if prob < best_prob:
                best_prob = prob

    e_m[start][end] = best_prob
    return best_prob



def op_bt_bu(p, q):
    prob_m = [[-1] * len(x) for _ in range(len(x) + 1)]
    weig_m = [[-1] * len(x) for _ in range(len(x) + 1)]
    root_m = [[-1] * len(x) for _ in range(len(x) + 1)]

    for i in range(1, len(x) + 1):
        prob_m[i][i-1] = q[i-1]

    for l in range(0, len(x) - 1):
        for i in range(1, len(x) - l):
            j = i + l
            weig_m[i][j] = weight(p, q, i, j)
            best_prob = 10000
            local_root = -1
            for k in range(i, j+1):
                prob = prob_m[i][k-1] + prob_m[k+1][j] + weig_m[i][j]
                #print(i, j, k, prob)

                if prob < best_prob:
                    best_prob = prob
                    prob_m[i][j] = prob
                    root_m[i][j] = k

    return prob_m, weig_m, root_m

def print_obt(root_m, i, j, p):
    if i > j:
        print("d{}".format(j))
    else:
        k = root_m[i][j]
        print ("{}: {}".format(k, p))
        print_obt(root_m, i, k-1, k)
        print_obt(root_m, k+1, j, k)

x = [0.00, 0.15, 0.10, 0.05, 0.10, 0.20]
y = [0.05, 0.10, 0.05, 0.05, 0.05, 0.10]

#prob_m = [[-1] * len(x) for _ in range(len(x) + 1)]
#weig_m = [[-1] * len(x) for _ in range(len(x))]
#print(op_bt(x, y, 1, 5, prob_m, weig_m))
#print()

prob_m, weig_m, root_m = op_bt_bu(x, y)

for row in prob_m:
    print(row)
print()
for row in weig_m:
    print(row)
print()
for row in root_m:
    print(row)

print_obt(root_m, 1, 5, None)
