'''
suffix arr:

defination:
- banana => banana, anana, nana, ana, na, a
- to clear the boudary, add unique sign to the end: '$'
  banana => banana$, anana$, nana$, ana$, na$, a$
- sort the string, suffix arr P = [6, 5, 3, 1, 0, 4, 2]
  6 $
  5 a$
  3 ana$
  1 anana$
  0 banana$
  4 na$
  2 nana$

how to get:
- sort the extended one:
  6 $banana
  5 a$banan
  3 ana$ban
  1 anana$b
  0 banana$
  4 na$bana
  2 nana$ba


- sort n * n * log(n)
- sort while using previous sort info: nlog(n) + nlog(n) * log(n)
k = 0, sort s[0], nlog(n)
   $ 6 0
   a 1 1
   a 3 1
   a 5 1
   b 0 2
   n 2 3
   n 4 3
k = 1, sort s[0] + s[1], nlog(n)
    ba 2 1 => 3
    an 1 3 => 2
    na 3 1 => 4
    an 1 3 => 2
    na 3 1 => 4
    a$ 1 0 => 1
    $b 0 2 => 0

k = 2, sort s[0, 1] +  s[2, 3], nlog(n)
    bana 3 4 => 4
    anan 2 2 => 3
    nana 4 4 => 6
    ana$ 2 1 => 2
    na$b 4 0 => 5
    a$ba 1 3 => 1
    $ban 0 2 => 0

- improvment, radix sort: nlog(n) + n * log(n)

- More improvement:
  - radix sort, first last digit, then sencond last, then ..., first digit
  - extend back, e.g. ba => a$ba, ba is the last digit, already sort in step k, only sort the new digit in step k + 1, and add to new bucket


How to use:
- find substring:
  find lenth p substring in string of length n, build suffix_tree in n*log(n), binary search in sorted suffix tree log(n) * p

-
'''

import sys
import time
import random
#from functools import lru_cache

long_str = 'agbccnegdeaf' * 4000
random_str = ''.join([chr(random.randint(97,122)) for i in range(30000)])

sa_cases = [
    'banana',
    'ababba',
    'abcdefghi',
    'aaaaaaaaab',
    #long_str,
    random_str
]

def power_search(value):
    left, right = 0, 2
    while 2** right < value:
        left = right
        right *= 2
    while left <= right:
        mid = left + (right - left) // 2
        score = 2 ** mid
        if score == value:
            return mid
        elif score < value:
            left = mid + 1
        else:
            right = mid - 1
    return mid if score > value else mid + 1



def quick_sort(arr, start=0, end=None):
    #print(arr[start:end+1])
    if end is None:
        end = len(arr) - 1
    if start < end:
        i_pivot = partition_arr(arr, start, end)
        quick_sort(arr, start, i_pivot - 1)
        quick_sort(arr, i_pivot + 1, end)

def partition_arr(arr, start, end):
    last_small, i_pivot, pivot = start - 1, end, arr[end][0]
    for i_cur in range(start, end + 1):
        if arr[i_cur][0] <= pivot:
            last_small += 1
            arr[last_small], arr[i_cur] = arr[i_cur], arr[last_small]
    return last_small

def suffix_array_sort(string):
    string = string + '$'
    all_suffices = [string[i:] + string[:i] for i in range(len(string))]
    return sorted(range(len(all_suffices)), key=all_suffices.__getitem__)


def suffix_array_standard(string):
    string = string + '$'
    len_s = len(string)
    p, c = [0] * len_s,  [0] * len_s
    dist, k = 0, 0
    while dist < len_s:
        arr = [ele for ele in string] if k == 0 else [
            (c[i], c[(i+dist) % len_s])
            for i in range(len_s)
        ]
        #p = sorted(range(len_s), key=arr.__getitem__)
        arr_to_sort = [(ele, i_ele) for i_ele, ele in enumerate(arr)]
        quick_sort(arr_to_sort, 0, len_s - 1)
        p = [ele[1] for ele in arr_to_sort]
        c[p[0]] = 0
        for i in range(1, len_s):
            if arr[p[i]] != arr[p[i-1]]:
                c[p[i]] = c[p[i-1]] + 1
            else:
                c[p[i]] = c[p[i-1]]
        if c[p[i]] == len_s - 1:
            break
        k += 1
        dist = 1 << (k - 1)
    return p

def radix_sort(values):
    nr_digits = len(values[0])
    nr_ele = 0
    i = nr_digits - 1
    buckets = dict()
    max_v = 0
    for i_value, value in enumerate(values):
        if value[i] > max_v:
            max_v = value[i]
        if value[i] in buckets:
            buckets[value[i]].append(i_value)
        else:
            buckets[value[i]] = [i_value]
    i -= 1
    while i >= 0:
        new_buckets = dict()
        next_max_v = 0
        for value in range(max_v + 1):
            if value not in buckets:
                continue
            for i_value in buckets[value]:
                if values[i_value][i] > next_max_v:
                    next_max_v = values[i_value][i]
                if values[i_value][i] in new_buckets:
                    new_buckets[values[i_value][i]].append(i_value)
                else:
                    new_buckets[values[i_value][i]] = [i_value]
        buckets = new_buckets
        max_v = next_max_v
        i -= 1
    return [i_value for i in range(max_v + 1) if i in buckets for i_value in buckets[i]]


#print(radix_sort([(2, 1),(3, 4),(4, 2),(2,2),(3, 2), (4, 1), (3, 3), (2, 4)]))
#print(radix_sort([(115, 110),(109, 148),(115, 209),( 115, 109),(112, 211)]))

def score_seq(i_values, values):
    score, prev_value, scores = -1, None, dict()
    for i_c in i_values:
        if prev_value != values[i_c]:
            prev_value, score = values[i_c], score + 1
        scores[i_c] = score
    return scores, score


def suffix_array_radix(string):
    string = string + '$'
    len_s = len(string)
    p, c = [0] * len_s,  [0] * len_s
    dist, k = 0, 0
    while dist < len_s:
        if k == 0:
            arr = [ch for ch in string]
            p = sorted(range(len_s), key=arr.__getitem__)
        else:
            arr = [(c[i], c[(i+dist) % len_s]) for i in range(len_s)]
            count, pos, s_p = [0] * len_s, [0] * len_s, [0] * len_s
            for i in range(len_s):
                count[arr[i][1]] += 1
            for i in range(1, len_s):
                pos[i] = pos[i-1] + count[i-1]
            for i in range(len_s):
                score = arr[i][1]
                s_p[pos[score]] = i
                pos[score] += 1
            count, pos = [0] * len_s, [0] * len_s
            for i in range(len_s):
                count[arr[i][0]] += 1
            for i in range(1, len_s):
                pos[i] = pos[i-1] + count[i-1]
            for i in s_p:
                score = arr[i][0]
                p[pos[score]] = i
                pos[score] += 1
        c[p[0]] = 0
        for i in range(1, len_s):
            if arr[p[i]] != arr[p[i-1]]:
                c[p[i]] = c[p[i-1]] + 1
            else:
                c[p[i]] = c[p[i-1]]
        if c[p[i]] == len_s - 1:
            break
        k += 1
        dist = 1 << (k - 1)
    return p


def suffix_array_radix_improve(string):
    string = string + '$'
    len_s = len(string)
    c = [0] * len_s
    dist, k = 0, 0
    while dist < len_s:
        if k == 0:
            arr = [ch for ch in string]
            p = sorted(range(len_s), key=arr.__getitem__)
            c[0] = 0
            for i in range(1, len_s):
                if arr[p[i]] != arr[p[i-1]]:
                    c[p[i]] = c[p[i-1]] + 1
                else:
                    c[p[i]] = c[p[i-1]]
        else:
            count, pos, p_new = [0] * len_s, [0] * len_s, [0] * len_s
            for i in range(len_s):
                count[c[i]] += 1
            for i in range(1, len_s):
                pos[i] = pos[i-1] + count[i-1]
            for i in p:
                new_i = (i-dist) % len_s
                score = c[new_i]
                p_new[pos[score]] = new_i
                pos[score] += 1
            # c     = 0, 1, 1, 2, 3, 3, 4, 4, 4, 4, 5
            # count = 1, 2, 1, 2, 4, 1, 0, 0, 0, 0, 0
            # pos   = 0, 1, 3, 4, 6, 10, 11, 11, 11, 11, 11
            # print(f'{p}, {c}, {count}, {pos}')

            p = p_new

            new_c = [0] * len_s
            for i in range(1, len_s):
                cur = (c[p[i]], c[(p[i] + dist) % len_s])
                prev = (c[p[i - 1]], c[(p[i - 1] + dist) % len_s])
                if cur != prev:
                    new_c[p[i]] = new_c[p[i-1]] + 1
                else:
                    new_c[p[i]] = new_c[p[i-1]]
            c = new_c
        if c[p[i]] == len_s - 1:
            break
        k += 1
        dist = 1 << (k - 1)
    return p

# to avoid recuraion limitation error
sys.setrecursionlimit(15000)

p_start = time.time()
p_python = [suffix_array_sort(string) for string in sa_cases]
print("python duration: {}".format(time.time() - p_start))
for method in [suffix_array_standard, suffix_array_radix, suffix_array_radix_improve]:
    start = time.time()
    p = [method(string) for string in sa_cases]
    print("{} duration: {}".format(method.__name__, time.time() - start))
    assert  p == p_python
