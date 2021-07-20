cases = [
    {
        "input": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],
        "queries": [(0,5), (6,10), (0,15)],
    }
]


def bi_tr(arr):
    n = len(arr)
    bi_tree = [0] * (n + 1)
    for i, v in enumerate(arr):
        x = i + 1
        while x <= n:
            bi_tree[x] += v
            x += x & -x
    return bi_tree

def prefix_query(i, bi_tree):
    prefix_sum = 0
    x = i + 1
    while x > 0:
        prefix_sum += bi_tree[x]
        x -= x & -x
    print(i, prefix_sum)
    return prefix_sum

for case in cases:
    bi_tree = bi_tr(case['input'])
    print(bi_tree)
    for query in case['queries']:
        sum_start = prefix_query(query[0] - 1, bi_tree)
        sum_end = prefix_query(query[1], bi_tree)
        assert  sum_end - sum_start == sum(case['input'][query[0]:query[1]+1])
