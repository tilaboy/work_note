from q2_1_2 import check_time
import random

def insert_sort_increase(arr):
    for index_to_sort in range(1,len(arr)):
        to_sort = arr[index_to_sort]
        new_index_to_sort = index_to_sort
        index_to_compare = index_to_sort - 1

        while index_to_compare >= 0 and arr[index_to_compare] > arr[new_index_to_sort]:
            arr[new_index_to_sort] = arr[index_to_compare]
            arr[index_to_compare] = to_sort
            new_index_to_sort = index_to_compare
            index_to_compare -= 1

    return arr


def insert_sort_quick(arr):
    for index_to_sort in range(1,len(arr)):
        to_sort = arr[index_to_sort]
        new_index_to_sort = index_to_sort
        index_to_compare = index_to_sort - 1

        # looking for the right position to insert
        if to_sort > arr[index_to_sort - 1]:
            pass
        elif to_sort < arr[0]:
            arr[1:index_to_sort+1] = arr[0:index_to_sort]
            arr[0] = to_sort
        else:
            position_to_insert = quick_lookup(arr, 0, index_to_sort-1, index_to_sort)
            arr[position_to_insert + 1: index_to_sort + 1] = arr[position_to_insert:index_to_sort]
            arr[position_to_insert] = to_sort

    return arr

# [2,3,1,4] 4 => mid = 1; [2,3], [1,4] => (0=>2;2=>4)
# [2,3,1] 4 => mid = 1; [2, 3], [1] => (0=>1;1=>3)
def quick_lookup(arr, start, end, index_to_sort):
    mid = start + int((end - start)/2)

    if arr[mid] == arr[index_to_sort]:
        return mid
    elif arr[mid] > arr[index_to_sort]:
        if start == mid:
            return mid
        else:
            return quick_lookup(arr, start, mid, index_to_sort)
    else:
        if mid + 1 == end:
            return end
        else:
            return quick_lookup(arr, mid + 1, end, index_to_sort)


def quick_search(arr, start, end, value):
    #[1, 4, 7, 9, 11], 3 =>  1, 4, 7 => 1, 4 =>
    #[1, 4, 6, 7, 9, 11], 3 => 1, 4, 6 => 1, 4 =>
    # [1, 4, 7, 9, 11, 13, 15, 17], 3 => 1, 4, 7, 9 => 1, 4
    if end == start:
        if arr[start] == value:
            return start
        elif arr[end] == value:
            return end
        else:
            return None
    else:
        mid = start + int((end - start)/2)
        if arr[mid] == value:
            return mid
        elif arr[mid] > value:
            #print(arr, start, arr[start], mid, arr[mid])
            return quick_search(arr, start, mid, value)
        else:
            #print(arr, mid+1, arr[mid+1], end, arr[end])
            return quick_search(arr, mid + 1, end, value)


def insert_sort_decrease(arr):
    for index_to_sort in range(1,len(arr)):
        to_sort = arr[index_to_sort]
        new_index_to_sort = index_to_sort
        index_to_compare = index_to_sort - 1
        while index_to_compare >= 0 and arr[index_to_compare] < arr[new_index_to_sort]:
            arr[new_index_to_sort] = arr[index_to_compare]
            arr[index_to_compare] = to_sort
            new_index_to_sort = index_to_compare
            index_to_compare -= 1

    return arr


def min_sort(arr):
    for i in range(len(arr) - 1):
        # get the index of min value in [1:]
        min_index = i
        min_value = arr[i]
        for j in range(i, len(arr)):
            if arr[j] < min_value:
                min_value = arr[j]
                min_index = j
        first_value = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = first_value
    return arr

# [2,3,1,4] => [2,3], [1,4] => (0=>2;2=>4)
# [2,3,1] => [2], [3,1] => (0=>1;1=>3)


def merge_sort(arr, start, end):
    if end > start + 1:
        # split half
        mid = start + int(( end - start ) / 2 )
        merge_sort(arr, start, mid)
        merge_sort(arr, mid, end)
        merge_sorted(arr, start, mid, end)

def merge_sorted(arr, start, mid, end):
    arr_1 = arr[start:mid]
    arr_2 = arr[mid:end]
    shift = 0
    while arr_1 and arr_2:
        if arr_1[0] >= arr_2[0]:
            element = arr_2.pop(0)
        else:
            element = arr_1.pop(0)
        arr[start + shift] = element
        shift += 1

    arr[start+shift:end] = arr_1[:] if arr_1 else arr_2[:]

def swap_elements(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def partition_arr(arr, start, end):
    pivot = arr[end]
    j = start - 1
    for i in range(start, end + 1):
        if arr[i] <= pivot:
            j = j + 1
            swap_elements(arr, i, j)
            #print(arr)
    return j

def partition_hoare(arr, start, end):
    x = arr[start]
    i = start - 1
    j = end + 1
    #print(arr)
    #print("pivot: {}".format(x))
    while True:
        #print("round")
        while arr[j - 1] > x:
            j = j - 1

        while arr[i + 1] < x:
            i = i + 1

        if i + 1 < j - 1:
            #print("swap {} [{}] <=> {} [{}]".format(i + 1, arr[i+1], j-1, arr[j-1]))
            swap_elements(arr, i+1 ,j-1)
            #print(arr)
        else:
            #print("reaching end", arr)
            return j

def partition_random(arr, start, end):
    pivot_index = random.randint(start, end)
    swap_elements(arr, pivot_index, end)
    return partition_arr(arr, start, end)

def partition_tail_recursive(arr, start, end):
    while start < end:
        tem_arr = arr[:]
        print(start, end)
        pivot = partition_arr(arr, start, end)
        print("pivot", pivot, tem_arr, "=>", arr, "\t", arr[start:end+1])
        partition_tail_recursive(arr, start, pivot - 1)
        start = pivot + 1

def partition_skip_equal_2(arr, start, end):
    pivot = arr[end]
    swap_elements(arr, start, end)
    i = start - 1
    k = start
    print("start: ", arr)
    for j in range(start+1, end):
        print(arr)
        if arr[j] > pivot:
            i = i + 1
            k = i + 2
            swap_elements(arr, i, j)
            print('\tlarge_i', arr)

            swap_elements(arr, k, j)
            print('\tlarger_k', arr)

        if arr[j] == pivot:
            k = k + 1
            swap_elements(arr, j, k)

            print('equal: ', arr)
    print(i+1, k+1)
    #swap_elements(arr, i+1, end)


def partition_skip_equal(arr, start, end):
    pivot = arr[end]
    j = start - 1
    k = end
    for i in range(start, end + 1):
        if arr[i] == pivot and i < k:
            k = k - 1
            swap_elements(arr, i, k)
        if arr[i] <= pivot:
            j = j + 1
            swap_elements(arr, i, j)
            #print(arr)
        print(i, j, k, arr)
    return j - ( end - k ), j


def quick_sort(arr, start, end, func):
    if start < end:
        mid = func(arr, start, end)
        quick_sort(arr, start, mid - 1, func)
        quick_sort(arr, mid + 1, end, func)


def test_quick_sort(partition_func):
    arr = [42, 31, 41, 47, 59, 47, 26, 41, 58, 60, 47]
    #print("partition at: ", partition_hoare(arr, 0, len(arr) - 1))
    #(j, k) = partition_skip_equal(arr, 0, len(arr) - 1)
    #print(arr, j, k)
    #quick_sort(arr, 0, len(arr) -1, partition_func)
    #print("sorted:", arr)
    partition_skip_equal_2(arr, 0, len(arr) - 1)
    print(arr)



@check_time
def sort_array_eval_merge(arr):
    merge_sort(arr, 0, len(arr))

@check_time
def sort_array_eval_insert(arr):
    insert_sort_increase(arr)

@check_time
def sort_array_eval_quick_insert(arr):
    insert_sort_quick(arr)

@check_time
def sort_array_eval_min(arr):
    min_sort(arr)

@check_time
def sort_array_eval_quick(arr):
    quick_sort(arr, 0, len(arr) -1, partition_arr)

def sort_array_test():
    arr1 = [5, 2, 4, 6, 1, 3]
    arr2 = [31, 41, 59, 26, 41, 58]
    #print(insert_sort_increase(arr1))
    #print(insert_sort_increase(arr2))
    #print(insert_sort_decrease(arr1))
    #print(insert_sort_decrease(arr2))

    #merge_sort(arr1, 0, len(arr1))
    #print(arr1)
    #merge_sort(arr2, 0, len(arr2))
    #print(arr2)

    print(insert_sort_quick(arr1))
    print(insert_sort_quick(arr2))


def test():
    sort_array_test()

    arr3 = [random.randint(0, 20000) for i in range(100000000)]


    arr_merge = arr3[:]
    arr_insert = arr3[:]
    arr_insert_quick = arr3[:]
    arr_min = arr3[:]
    arr_quick = arr3[:]

    #sort_array_eval_insert(arr_insert)
    #sort_array_eval_min(arr_min)
    sort_array_eval_quick_insert(arr_insert_quick)
    sort_array_eval_merge(arr_merge)
    sort_array_eval_quick(arr_quick)

    assert arr_merge == arr_insert
    assert arr_min == arr_insert
    assert arr_min == arr_insert_quick
    assert arr_min == arr_quick


test_quick_sort(partition_arr)
