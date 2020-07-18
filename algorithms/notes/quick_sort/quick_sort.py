
import random

def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot_index = random.randint(start, end)
    pivot_value = arr[pivot_index]
    arr[end], arr[pivot_index] = arr[pivot_index], arr[end]

    fast_index = slow_index = start
    while fast_index < end:
        if arr[fast_index] < pivot_value:
            arr[fast_index], arr[slow_index] = arr[slow_index], arr[fast_index]
            slow_index += 1
        fast_index += 1

    arr[end], arr[slow_index] = arr[slow_index], arr[end]
    quick_sort(arr, start, slow_index - 1)
    quick_sort(arr, slow_index + 1, end)

def local_gcd(a, b):
    if a % b == 0:
        return b
    else:
        return local_gcd(b, a % b)

print(local_gcd(117, 207))

nums1 = [1,2,3,4]
nums2 = [2,2,3,1,4]
nums3 = [4,7,2,8,4,9,1,6,3,5,3]
_quick_sort(nums1, 0, len(nums1) - 1)
_quick_sort(nums2, 0, len(nums2) - 1)

_quick_sort(nums3, 0, len(nums3) - 1)
print(nums1, nums2, nums3)
