cases = [
    [5, 1, 'ABCAA'],
    [4, 2, 'ABAA'],
    [9, 1, 'ABCDEDCBA'],
    [10, 1, 'ABCDEFDCBA'],
    [6, 2, 'CABABC'],
    [1, 0, 'A']
]


def get_goodness(str, n):
    half = n // 2
    goodness = 0
    for i in range(half):
        if str[i] != str[n-i-1]:
            goodness += 1
    print(str, goodness)
    return goodness

for n, k, str in (cases):
    goodness = get_goodness(str, n)
    if k > goodness:
        required = k - goodness
    else:
        required = 0
    print("Case #{}: {}".format(str, required))
