import random
from math import sqrt

def quick_sort(s, i, j):
    if i >= j:
        return
    else:
        pivot = random.randint(i, j)
        s[pivot], s[j] = s[j], s[pivot]

        pos_to_switch = i
        for index in range(i, j):
            if s[index][0] < s[j][0]:
                s[index], s[pos_to_switch] = s[pos_to_switch], s[index]
                pos_to_switch += 1
        s[pos_to_switch], s[j] = s[j], s[pos_to_switch]
        quick_sort(s, i, pos_to_switch-1)
        quick_sort(s, pos_to_switch+1, j)

def optimal_path(seq):
    dist = 0
    start = seq[0]
    for ele in seq[1:]:
        dist += sqrt((ele[0] - start[0])**2 + (ele[1] - start[1])**2)
        start = ele
    return dist

def bitonic_tour(s):
    quick_sort(s, 0, len(s) - 1)
    print(s)
    start = s.pop(0)
    end = s.pop()
    print(s)
    best_distance = 10000

    for k in range(len(s)):

        fore_seq = [ele for ele in s if ele[1] >= s[k][1]]
        fore_dis = optimal_path([start] + fore_seq + [end])
        back_seq = [ele for ele in s if ele[1] < s[k][1]]
        back_dis = optimal_path([start] + back_seq + [end])
        distance = fore_dis + back_dis
        if distance < best_distance:
            best_distance = distance
            best_seq = [start] + fore_seq + [end] + back_seq[::-1] + [start]
        print(s[k], distance, fore_seq, back_seq[::-1])

    return best_distance, best_seq


x=[(0, 6), (2, 3), (6, 1), (1, 0), (5, 4), (7, 5), (8, 2)]
best_distance, best_seq = bitonic_tour(x)
print(best_distance)
print(best_seq)

def insert_sort(s):
    nr = len(s)
    for i in range(1, nr):
        to_insert = s[i]
        j = i - 1
        while to_insert < s[j] and j >= 0:
            s[j+1] = s[j]
            j = j -1
        s[j + 1] = to_insert


def merge_sorted(a, b):
    i = 0
    j = 0
    c = list()
    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            c.append(b[j])
            j = j + 1
        else:
            c.append(a[i])
            i = i + 1
    if i == len(a):
        c = c + b[j:]
    else:
        c = c + a[i:]
    return c

def merge_sort(s, i, j):
    if i == j:
        return [s[i]]

    k = i + (j-i)//2

    s_fh = merge_sort(s, i, k)
    s_sh = merge_sort(s, k+1, j)

    return merge_sorted(s_fh, s_sh)
