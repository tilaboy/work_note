import random
import math

def k_quantiles(arr, start, end, k):
    if k <= 1:
        return arr[start:end+1]
    elif k % 2 == 0:
        q = int((end - start) / 2)
        print('splitting:', k, q, start, end)

        position = seek_kth(arr, start, end, q)
        upper = k_quantiles(arr, start, position-1, k/2)
        lower = k_quantiles(arr, position+1, end, k/2)
        print(upper, [arr[position]], lower)
    else:
        # odd
        k1 = int(k/2)
        k2 = int((k+1)/2)
        q = int((end - start + 1) * k1 / k)
        print('splitting:', k, k1, k2, q, start, end)
        position = seek_kth(arr, start, end, q)
        upper = k_quantiles(arr, start, position-1, k1)
        lower = k_quantiles(arr, position+1, end, k2)
        print(upper, [arr[position]], lower)

def insert_sort(arr):
    for i in range(1, len(arr)):
        to_switch = i
        j = i - 1
        while arr[to_switch] < arr[j] and j >= 0:
            arr[to_switch], arr[j] = arr[j], arr[to_switch]
            to_switch = j
            j -= 1

def mid_from_insert_sort(arr):
    insert_sort(arr)
    mid = int((len(arr) - 1)/2)
    return arr[mid]

def mid_by_5(arr):
    #print(arr)
    if len(arr) <= 5:
        return mid_from_insert_sort(arr)
    else:
        medians = []

        for index in range(0, len(arr), 5):
            if index + 5 < len(arr):
                medians.append(mid_from_insert_sort(arr[index:index+5]))
            else:
                medians.append(mid_from_insert_sort(arr[index:len(arr)]))
        #print('mdeidans:', medians)
        return mid_by_5(medians)

def partition_by_median(arr, start, end, median):
    position = start
    for index in range(start, end):
        if arr[index] == median:
            arr[index], arr[end] = arr[end], arr[index]

        if arr[index] < median:
            arr[index], arr[position] = arr[position], arr[index]
            position += 1

    arr[position], arr[end] = arr[end], arr[position]
    #print(median, position, arr[start:position], arr[position+1:end+1])
    return position

def seek_kth(arr, start, end, k):
    if start == end:
        return start
    median = mid_by_5(arr[start:end+1])
    position = partition_by_median(arr, start, end, median)
    print("found median: {} at pisition {}, for k={}, {} split into {} and {}".format(
          median, position - start, k, arr[position], arr[start:position], arr[position+1:end+1]))
    if position - start == k:
        print("found: {} => {}".format(position - start, arr[position]))
        return position
    elif k < position - start:
        print("go 1 : {} to {} => {}".format(start, position - 1, arr[start:position]))
        return seek_kth(arr, start, position - 1, k)
    else:
        print("go 2 : {} to {} => {}".format(position + 1, end, arr[position+1:end+1]))
        return seek_kth(arr, position + 1, end, k - (position - start + 1))


def get_arr():
    arr = [42, 31, 41, 46, 59, 45, 26, 43, 38, 56, 29, 54, 34, 44,
           58, 60, 47, 23, 33, 51, 35, 57, 37, 55, 52, 24, 36, 30]
    return arr

test_arr = get_arr()
print(len(test_arr), test_arr)
k_quantiles(test_arr, 0, len(test_arr) - 1, 5)
