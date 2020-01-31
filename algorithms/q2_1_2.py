import time
import random

def check_time(func):
    def wrapper(*args):
        t1 = time.time()
        result = func(*args)
        t2 = time.time()
        print("spend {:.4} s".format(t2- t1))
        return result
    return wrapper

@check_time
def n_lookup(v, arr):
    for i in range(len(arr)):
        if v == arr[i]:
            return i
    return None

@check_time
def quick_lookup(v, arr):
    return lookup_fast(v, arr, 0, len(arr) - 1)

def lookup_fast(v, arr, lower=0, upper=0):
    #if v < arr[lower] or v > arr[upper]:
    #    return None

    if lower == upper:
        if lower == v:
            return lower
        else:
            return None

    distance = upper - lower

    if distance < 2:
        if arr[lower] == v:
            return lower
        elif arr[upper] == v:
            return upper
        else:
            return None

    mid_index = int(distance / 2 + lower)
    #print('check mid_index: {}'.format(mid_index))
    if arr[mid_index] == v:
        return mid_index
    elif arr[mid_index] > v:
        return lookup_fast(v, arr, lower, mid_index)
    else:
        return lookup_fast(v, arr, mid_index, upper)


def lookup_element():
    #arr3 = [5, 41, 2, 58, 11, 16, 13, 4, 39, 7, 15, 53, 48, 24, 20, 26, 54, 55, 42, 23, 6, 59, 21, 1, 3]
    arr3 = [random.randint(0, 100000) for i in range(50000)]
    print(n_lookup(10062, arr3))
    print(n_lookup(50034, arr3))
    print(n_lookup(80021, arr3))

    arr3_sort = sorted(arr3)

    print(quick_lookup(10062, arr3_sort))
    print(quick_lookup(50034, arr3_sort))
    print(quick_lookup(80021, arr3_sort))

# a => [1, 0, 1]
# b => [1, 1, 0]
# c = a + b = [1, 0, 1, 1]
# pop a, pop b, c[i] = a[i] + b[i] + shift
def add_binary(a, b):
    len_a = len(a)
    len_b = len(b)
    shift = 0
    c = []
    for i in range(max(len_a, len_b)):
        a_i = a.pop() if a else 0
        b_i = b.pop() if b else 0
        c_i = a_i + b_i + shift

        c.insert(0, c_i % 2)
        shift = 1 if c_i > 1 else 0

    if shift > 0:
        c.insert(0, shift)
    return c

def add_two_binary_array():
    a = [1, 0, 1, 1, 1, 1]
    b = [1, 1, 0]
    print(add_binary(a, b))

#add_two_binary_array()
