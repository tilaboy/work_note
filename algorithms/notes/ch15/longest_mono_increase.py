def add_element(ele, sets):
    sets = [each_set + [ele] for each_set in sets]
    return sets


def lmi(arr, i):
    if i == 0:
        return [[arr[i]], []]
    else:
        longest_mi = lmi(arr, i-1)
        #print(i, longest_mi)
        return longest_mi + [ mi + [arr[i]]
                             for mi in longest_mi
                             if mi == [] or arr[i] > mi[-1]
                             ]
def _find(arr, value):
    for i in range(len(arr)):
        if arr[i] > value:
            break
    return i


def lmi_quick(arr):
    b_arr = [10000] * len(arr)
    c_arr = [0] * len(arr)

    l = 1

    for i in range(len(arr)):
        print("checking: {} at {}".format(arr[i], i), end=' ')
        if arr[i] < b_arr[0]:
            b_arr[0] = arr[i]
            c_arr[0] = arr[i]
            print("arr[{}]={}, b_arr={}, c_arr={}".format(i, arr[i], b_arr, c_arr))
        else:
            j = _find(b_arr, arr[i]);
            b_arr[j] = arr[i];
            c_arr[j] = arr[i];
            print("j={}, l={}, b_arr={}, c_arr={}".format(j, l, b_arr, c_arr))
            if j > l:
                l = j;

    print(arr)
    print(b_arr)
    print(c_arr)


x= [5, 7, 10, 12, 8]
#x=[5,7,6,8]
sets = lmi(x, len(x) - 1)
print(x)
print(sorted(sets, key=lambda x:len(x)))
lmi_quick(x)
