def op_copy(x, i, y, j):
    y[j] = x[i]
    return x, y

def op_replace(x, i, c, y, j):
    x[i] = c
    y[j] = c
    return x, y

def lcs(x, y):
    lcs_m = [[None] * (len(y) +  1) for _ in range(len(x) + 1)]
    track_m = [[None] * len(y) for _ in range(len(x))]

    for i in range(len(x) + 1):
        lcs_m[i][len(y)] = ''
    for i in range(len(y) + 1):
        lcs_m[len(x)][i] = ''

    for i in range(len(x) - 1, -1, -1):
        for j in range(len(y) -1, -1, -1):
            if x[i] == y[j]:
                lcs_m[i][j] = lcs_m[i+1][j+1] + x[i]
                track_m[i][j] = 'm'
            else:
                if len(lcs_m[i+1][j]) > len(lcs_m[i][j+1]):
                    lcs_m[i][j] = lcs_m[i+1][j]
                    track_m[i][j] = '^'
                else:
                    lcs_m[i][j] = lcs_m[i][j+1]
                    track_m[i][j] = '<'

    return lcs_m, track_m

def edit_dis(x, y):
    cs_m, track = lcs(x, y)
    rec_a = ['N'] * len(x)
    rec_b = ['N'] * len(y)

    i = 0
    j = 0

    # from x
    x_1 = x
    print("x_1:{}".format(x_1))
    print("y  :{}".format(y))
    shift = 0
    while i < len(x) and j < len(y):
        if track[i][j] == 'm':
            i += 1
            j += 1
        elif track[i][j] == '^':
            x_1 = x_1[:i+shift] + x_1[i+shift +1:]
            shift -= 1
            print('D x{} for y{}: {} => {}'.format(i, j, x[i], x_1) )
            i += 1
        else:
            x_1 = x_1[:i+shift] + y[j] + x_1[i+shift:]
            shift += 1
            print('A x{} from y{}: {} => {}'.format(i, j, y[j], x_1) )
            j += 1

    if i < len(x):
        while i < len(x):
            x_1 = x_1[:i+shift] + x_1[i+shift +1:]
            shift -= 1
            print('D x{} for y{}: {} => {}'.format(i, j, x[i], x_1) )
            i += 1
    if j < len(y):
        while j < len(y):
            x_1 = x_1[:i+shift] + y[j] + x_1[i+shift:]
            shift += 1
            print('A x{} from y{}: {} => {}'.format(i, j, y[j], x_1) )
            j += 1


Ops = {0: 'copy', 1: 'twiddle', 2: 'replace', 3: 'delete', 4: 'insert'}

def edit_dis_recu(x, y, i, j, best_cost, best_choice):
    #print("checking", i, j, x, y)

    if i == len(x):
        #print("delect all rest of y: {}".format(y[j:]))
        return 1 * (len(y) - j)
    if j == len(y):
        #print("delect all rest of x: {}".format(x[i:]))
        return 1 * (len(x) - i)

    costs = [float('inf')] * 5
    if x[i] == y[j]:
        costs[0] = 0 + edit_dis_recu(x, y, i+1, j+1, best_cost, best_choice)
    elif i + 1 < len(x) and j+1 < len(y) and \
        x[i] == y[j+1] and y[j] == x[i+1]:
            costs[1]= 1 + edit_dis_recu(x, y, i+2, j+2, best_cost, best_choice)
    else:
        costs[2] = 1 + edit_dis_recu(x, y, i+1, j+1, best_cost, best_choice)
        costs[3] = 1 + edit_dis_recu(x, y, i+1, j, best_cost, best_choice)
        costs[4] = 1 + edit_dis_recu(x, y, i, j+1, best_cost, best_choice)
    index, cost = min(enumerate(costs), key=lambda x:x[1])
    best_cost[i][j] = cost
    best_choice[i][j] = ("{} x{}({}) y{}({})".format(Ops[index], i, x[i], j, y[j]))
    #print(i, x[i], j, y[j], costs)
    return min(costs)



a = 'ABDECBSFAEDS'
b = 'ABCBNTEA'

costs_m = [[None] * len(b) for _ in range(len(a))]
choic_m = [[None] * len(b) for _ in range(len(a))]

print(edit_dis_recu(a, b, 0, 0, costs_m, choic_m))

for row in costs_m:
    print(row)
print()
for row in choic_m:
    print(row)
print()


cs_m, track = lcs(a, b)
for row in cs_m:
    print(row)
print()
for row in track:
    print(row)

i = 0
j = 0
rec_a = ['N'] * len(a)
rec_b = ['N'] * len(b)

while i < len(a) and j < len(b):
    if track[i][j] == 'm':
        rec_a[i] = j
        rec_b[j] = i
        i += 1
        j += 1
    elif track[i][j] == '^':
        i += 1
    else:
        j += 1
print(a)
print(rec_a)
print(b)
print(rec_b)


edit_dis(b, a)
