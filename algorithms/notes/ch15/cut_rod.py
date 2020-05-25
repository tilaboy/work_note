sep = {
    0:0,
    1:1,
    2:5,
    3:8,
    4:9,
    5:10,
    6:17,
    7:17,
    8:20,
    9:22,
    10:24
}

def cut_rod_recur(n, price, split):
    cost = -1
    best_k = 0
    if n in price:
        return price[n]

    for k in range(n//2 + 1):
        if k == 0:
            cost_k = sep[n]
        else:
            cost_k = cut_rod_recur(k, price, split) + cut_rod_recur(n-k, price, split)
        if cost < cost_k:
            cost = cost_k
            best_k = k

        # print("k {} in n {}: {} {}".format(k, n, cost_k, cost))
    price[n] = cost
    split[n] = best_k
    return cost


def cut_rod_recur_book(prices, rem, splits, n):
    if n in rem:
        return rem[n]

    if n == 0:
        best_price = 0
        best_split = 0
    else:
        best_price = -1
        best_split = -1
        for i in range(1, n+1):
            price = prices[i] + cut_rod_recur_book(prices, rem, splits, n - i)
            if price > best_price:
                best_price = price
                best_split = i
    rem[n] = best_price
    splits[n] = best_split
    return best_price


def print_cut_split_recur(prices, n):
    local_optimal = { 0:0 }
    local_split = dict()
    best_price = cut_rod_recur_book(prices, local_optimal, local_split, n)
    splits = list()
    while n > 0:
        split = local_split[n]
        splits.append(split)
        n = n - split
    return best_price, splits




def split_search(n, split, k_points):
    k = split[n]
    if k == 0 or k == n:
        return 0
    else:
        split_search(k, split, k_points)
        k_points.append(k)
        split_search(n-k, split, k_points)


def cut_rod(prices, n):
    local_optimal = { 0:0 }
    local_split = dict()
    for i in range(1, n+1):
        best_price = -1
        best_split = -1
        for k in range(1, i+1):
            price = prices[k] + local_optimal[i-k]
            if price > best_price:
                best_price = price
                best_split = k
        local_optimal[i] = best_price
        local_split[i] = best_split
    return best_price, local_optimal, local_split

def print_cut_split(prices, n):
    best_price, local_optimal, local_split = cut_rod(prices, n)
    splits = list()
    while n > 0:
        split = local_split[n]
        splits.append(split)
        n = n - split
    #print(best_price, splits)
    return best_price, splits

#n = int(input())
for n in range(1, 11):
    remembered_cost = dict()
    print("final cost {}: {}".format(n, print_cut_split(sep, n)))


for n in range(1, 11):
    remembered_cost = dict()
    print("final cost {}: {}".format(n, print_cut_split_recur(sep, n)))
