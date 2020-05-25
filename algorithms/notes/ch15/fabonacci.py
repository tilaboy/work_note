def fabon_b(n):
    if n < 3:
        return 1
    else:
        fab_seq = [1, 1]
        i = 3
        while i <= n:
            fab = fab_seq[-1] + fab_seq[-2]
            fab_seq.append(fab)
            i += 1

    print(fab_seq)


def fabon_rec(n, fab):
    if n in fab:
        return fab[n]
    if n < 3:
        return 1
    else:
        fab[n] = fabon_rec(n - 1, fab) + fabon_rec(n - 2, fab)
        return fab[n]

n = input()
fabon_b(int(n))
fab = dict()
print(fabon_rec(int(n), fab))
