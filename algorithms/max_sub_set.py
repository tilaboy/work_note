from q2_1_2 import check_time
import random

@check_time
def brutal_search(arr):
    length = len(arr)
    max_sum = 0
    sub_set = []
    for i in range(length):
        local_max = 0
        for j in range(i, length):
            local_max += arr[j]
            if local_max > max_sum:
                max_sum = local_max
                sub_set = [i, j]
    return max_sum, sub_set


@check_time
def divid_and_concor(arr):
    return split_search(arr, 0, len(arr) - 1)

def split_search(arr, start, end):
    if start == end:
        return arr[start], [start, end]

    mid = start + int((end - start)/2)
    left_max, left_max_range = split_search(arr, start, mid)
    right_max, right_max_range = split_search(arr, mid+1, end)
    cross_max, cross_max_range = cross_search(arr, start, mid, end)
    if left_max > right_max:
        if left_max > cross_max:
            return left_max, left_max_range
        else:
            return cross_max, cross_max_range
    else:
        if right_max > cross_max:
            return right_max, right_max_range
        else:
            return cross_max, cross_max_range


def cross_search(arr, start, mid, end):
    left_max = local_max = arr[mid]
    left_max_pos = mid
    for i in range(mid - 1, start - 1, -1):
        local_max += arr[i]
        if local_max > left_max:
            left_max = local_max
            left_max_pos = i
    right_max = local_max = arr[mid + 1]
    right_max_pos = mid + 1
    for i in range(mid + 2 , end + 1, 1):
        local_max += arr[i]
        if local_max > right_max:
            right_max = local_max
            right_max_pos = i
    #print(start, mid, end, "max:", right_max + left_max, [left_max_pos, right_max_pos], arr[left_max_pos:right_max_pos+1])
    return right_max + left_max, [left_max_pos, right_max_pos]


#    [a, b, c, d]
# => [a, b, c] + cross[d]
@check_time
def linear_search(arr):
    max_till_end = arr[0]
    max_till_end_range = [0,1]

    max_inside = arr[0]
    max_inside_range =[0,1]

    for index in range(1, len(arr)):
        if arr[index] > max_till_end + arr[index]:
            max_till_end = arr[index]
            max_till_end_range = [index, index + 1]
        else:
            max_till_end = max_till_end + arr[index]
            max_till_end_range[1] = index

        if max_till_end > max_inside:
            max_inside = max_till_end
            max_inside_range = max_till_end_range[:]

    return max_inside, max_inside_range



def check_on_random_set():
    changes = [random.randint(-20000, 20000) for i in range(10000)]
    b_max_sum, b_sub_set = brutal_search(changes)
    print(b_max_sum, b_sub_set)
    d_max_sum, d_sub_set = divid_and_concor(changes)
    print(d_max_sum, d_sub_set)
    l_max_sum, l_sub_set = linear_search(changes)
    print(l_max_sum, l_sub_set)

    assert b_max_sum == d_max_sum
    assert b_sub_set == d_sub_set
    assert l_sub_set == d_sub_set
    assert l_max_sum == d_max_sum




changes = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
max_sum, sub_set = brutal_search(changes)
print(max_sum, sub_set)
max_sum, sub_set = divid_and_concor(changes)
print(max_sum, sub_set)
max_sum, sub_set = linear_search(changes)
print(max_sum, sub_set)

check_on_random_set()
