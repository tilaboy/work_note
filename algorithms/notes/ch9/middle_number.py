import random
import math

def exchange(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def partition_arr(arr, start, end):
    position = random.randint(start, end)
    exchange(arr, position, end)
    pivot = arr[end]

    position = start
    for index in range(start, end):
        if arr[index] < pivot:
            exchange(arr, index, position)
            position += 1
    exchange(arr, position, end)
    #print(pivot, position, arr[start:position], arr[position+1:end+1])
    return position

def quick_sort(arr, start, end):
    if start < end:
        pivot = partition_arr(arr, start, end)
        quick_sort(arr, start, pivot-1)
        quick_sort(arr, pivot+1, end)

def get_nth(arr, nth):
    return random_select(arr, 0, len(arr) - 1, nth)

def get_nth_no_recur(arr, nth):
    start = 0
    end = len(arr) - 1
    while start != end:
        q = partition_arr(arr, start, end)
        k = q - start + 1

        if nth == k:
            return arr[q]

        elif nth < k:
            end = q - 1
        else:
            start = q + 1
            nth = nth - k
    return arr[start]

def random_select(arr, start, end, i):
    if start == end:
        return arr[start]

    q = partition_arr(arr, start, end)
    k = q - start + 1

    if i == k:
        return arr[q]

    elif i < k:
        return random_select(arr, start, q - 1, i)
    else:
        return random_select(arr, q+1, end, i - k)


def sec_min(arr):
    start = 0
    len_arr = len(arr)
    end = len_arr - 1
    depth = math.log(len_arr, 2)
    records = {}
    minimum = _seek_sec_min(arr, start, end, records)
    return arr[minimum], records[minimum]

def _seek_sec_min(arr, start, end, records):
    if end - start <= 1:
        if arr[end] > arr[start]:
            records[start] = [arr[end]]
            return start
        else:
            records[end] = [arr[start]]
            return end

    mid = start + int((end - start) / 2)
    #print("###", start, mid, end)

    upper_min = _seek_sec_min(arr, start, mid, records)
    lower_min = _seek_sec_min(arr, mid + 1, end, records)

    if arr[upper_min] < arr[lower_min]:
        records[upper_min].append(arr[lower_min])
        return upper_min
    else:
        records[lower_min].append(arr[upper_min])
        return lower_min

def insert_sort(arr):
    for index in range(1, len(arr)):
        to_sort = index
        # if index == 0, loop will be skipped
        for sub_index in range(index - 1, -1, -1):
            if arr[to_sort] < arr[sub_index]:
                # swap to_sort and sub_index, update to_sort to sub_index
                temp = arr[to_sort]
                arr[to_sort] = arr[sub_index]
                arr[sub_index] = temp
                to_sort = sub_index
            else:
                break

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
        print('mdeidans:', medians)
        return mid_by_5(medians)

def partition_by_median(arr, start, end, median):
    position = start
    for index in range(start, end):
        if arr[index] == median:
            exchange(arr, index, end)
            break

    for index in range(start, end):
        if arr[index] < median:
            exchange(arr, index, position)
            position += 1

    exchange(arr, position, end)
    #print(median, position, arr[start:position], arr[position+1:end+1])
    return position

def select_kth(arr, start, end, k):
    if start == end:
        return arr[start]
    median = mid_by_5(arr[start:end+1])
    position = partition_by_median(arr, start, end, median)
    print("found median: {} at pisition {}, for k={}, check {}".format(median, position - start, k, arr[start:end+1]))
    if position - start == k - 1:
        print("found: {} => {}".format(position - start, arr[position]))
        return (arr[position])
    elif k - 1 < position - start:
        print("go 1 : {} to {} => {}".format(start, position - 1, arr[start:position]))
        return select_kth(arr, start, position - 1, k)
    else:
        print("go 2 : {} to {} => {}".format(position + 1, end, arr[position+1:end+1]))
        return select_kth(arr, position + 1, end, k - position + start - 1)


def get_arr():
    arr = [42, 31, 41, 46, 59, 45, 26, 43, 38, 56, 29, 54, 34, 44,
           58, 60, 47, 23, 33, 51, 35, 57, 37, 55, 52, 24, 36, 30]
    return arr


test_arr = get_arr()
print(select_kth(test_arr, 0, len(test_arr) - 1, 16))
quick_sort(test_arr, 0 , len(test_arr) - 1)
print(test_arr)
