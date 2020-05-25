def two_array_median(a, b):
    if len(a) == 1:
        return min(a[0], b[0])

    m = median_index(len(a))
    i = m + 1
    if a[m] < b[m]:
        print(m, a[-i:], b[:i])
        return two_array_median(a[-i:], b[:i])
    else:
        print(m, a[:i], b[-i:])

        return two_array_median(a[:i], b[-i:])

def median_index(n):
    if n % 2:
        return n // 2
    else:
        return n // 2 - 1


arr1 = [42, 31, 41, 46, 59, 45, 26, 43, 38, 56, 29, 54, 34, 44]
arr2 = [58, 60, 47, 23, 33, 51, 35, 57, 37, 55, 52, 24, 36, 30]

print(two_array_median(arr1, arr2))

arr = sorted(arr1+arr2)

print(arr[int(len(arr)/2)], arr)
