from typing import List
from unittest import TestCase

def binarySearch_tm1(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    print('check for {} in {}'.format(target, nums))

    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        print("check: {}, {}, {}".format(left, mid, right))
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        print("updat: {}, {}, {}".format(left, mid, right))

    # End Condition: left > right
    return -1

def binarySearch_tm2(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    print('check for {} in {}'.format(target, nums))

    if len(nums) == 0:
        return -1

    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        print("check: {}, {}, {}".format(left, mid, right))
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid
        print("updat: {}, {}, {}".format(left, mid, right))

    # End Condition: left > right
    return -1

def binarySearch_tm3(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid
        else:
            right = mid

    # Post-processing:
    # End Condition: left + 1 == right
    if nums[left] == target: return left
    if nums[right] == target: return right
    return -1


def binarySearch(nums, target):
    return binarySearch_tm3(nums, target)


def sort_on_height(people):
    def helper(arr, left, right):
        pivot = arr[right]
        index_to_replace = left
        for index in range(left, right):
            if arr[index][0] <= pivot[0]:
                if arr[index][0] == pivot[0] and arr[index][1] > pivot[1]:
                    continue
                arr[index], arr[index_to_replace] = arr[index_to_replace], arr[index]
                index_to_replace += 1
        arr[index_to_replace], arr[right] = arr[right], arr[index_to_replace]
        return index_to_replace

    def quick_search(people, left, right):
        if left >= right:
            return
        pivot_index = helper(people, left, right)
        quick_search(people, left, pivot_index - 1)
        quick_search(people, pivot_index + 1, right)

    quick_search(people, 0, len(people) - 1)

def searchRange(nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums) - 1
    i = 0
    while right >= left and nums[right] != nums[left]:
        i += 1
        mid = left + (right - left) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            print(left, right, mid, nums[left:right+1])
            # mid is target, might be in the middle
            # search for right and left boundaries
            while nums[right] > target and left < right:
                right -= 1
            while nums[left] < target and left < right:
                left += 1
    if left <= right and nums[right] == nums[left] == target:
        return [left, right]
    else:
        return [-1, -1]


target_range = searchRange([3, 4, 5, 6, 6, 7, 7, 9], 8)
#print(target_range)

arr = [-5, -3, -2, 1, 2, 5, 9, 10, 13, 18]

#print(binarySearch(arr, 5))
#print(binarySearch(arr, 1))
#print(binarySearch(arr, 0))
#print(binarySearch(arr, 11))
#print(binarySearch(arr, 3))
#print(binarySearch(arr, 18))


def smedian(x:List[int]) -> int:
    is_odd = len(x) % 2
    median_pos = (len(x) + is_odd)// 2
    median_index = median_pos - 1
    return x[median_index] if is_odd else (x[median_index] + x[median_index + 1]) / 2

def binary_median(nums1:List[int], nums2:List[int]) -> int:
    l_nums1, l_nums2 = len(nums1), len(nums2)
    is_odd = (l_nums1 + l_nums2) % 2
    median_index = (l_nums1 + l_nums2 + 1) // 2 - 1

    if l_nums1 < l_nums2:
        nums1, nums2, l_nums1, l_nums2 = nums2, nums1, l_nums2, l_nums1

    #if l_nums2 == 0:
    #    return smedian(nums1)

    left, right = median_index + 1 - l_nums2 - 1, median_index
    print(left, right, nums1, nums2, l_nums1, l_nums2)
    while left <= right:
        mid_1 = left + (right - left) // 2
        mid_2 = median_index + 1 - (mid_1 + 1) - 1
        print('check: l:{} r:{} m1:{} m2:{}'.format(left, right, mid_1, mid_2))
        # check: l:0 r:0 m1:0 m2:-1
        if l_nums2 == 0:
            break
        elif mid_2 < l_nums2 - 1 and nums1[mid_1] > nums2[mid_2 + 1]:
            print("update right: {} => {}".format(right, mid_1 - 1))
            right = mid_1 - 1
        elif mid_1 < l_nums1 - 1 and nums2[mid_2] > nums1[mid_1 + 1]:
            print("update left: {} => {}".format(left, mid_1 + 1))
            left = mid_1 + 1
        else:
            print('matched: {} {}'.format(mid_1, mid_2))
            break

    print("mid_1: {}, mid_2: {}".format(mid_1, mid_2))
    if mid_1 < 0:
        left_cand = nums2[mid_2]
    elif mid_2 < 0:
        left_cand = nums1[mid_1]
    else:
        left_cand = max(nums1[mid_1], nums2[mid_2])
    print('left cand: {}'.format(left_cand))
    if is_odd:
        return left_cand

    if mid_2 == l_nums2 - 1:
        right_cand = nums1[mid_1 + 1]
    elif mid_1 == l_nums1 - 1:
        right_cand = nums2[mid_2 + 1]
    else:
        right_cand = min(nums1[mid_1 + 1], nums2[mid_2 + 1])
    print('righ cand: {}'.format(right_cand))
    return (right_cand + left_cand) / 2

class TestBinaryMedian(TestCase):
    def test_one_array_median(self):
        self.assertEqual(smedian([1]), 1, 'single value')
        self.assertEqual(smedian([1,4, 5]), 4, 'odd')
        self.assertEqual(smedian([1,4, 5, 10]), 4.5, 'even')

    def test_two_array_median(self):
        self.assertEqual(binary_median([2,5,6,7],[3,4,8,9]), 5.5, 'same size 1')
        self.assertEqual(binary_median([1,5,6,8],[2,3,4,7]), 4.5, 'same size 2')
        self.assertEqual(binary_median([2,3,4],[1]), 2.5, 'long right')
        self.assertEqual(binary_median([1,3],[2]), 2, 'simple odd')
        self.assertEqual(binary_median([1],[2]), 1.5, 'simple even 1')
        self.assertEqual(binary_median([2],[1]), 1.5, 'simple even 2')
        self.assertEqual(binary_median([2],[]), 2, 'one side empty, 1')
        self.assertEqual(binary_median([2,3],[]), 2.5, 'one side empty, 2')
        self.assertEqual(binary_median([1,2,3,4],[5,6,7,8]), 4.5, 'no inters even 1')
        self.assertEqual(binary_median([5,6,7,8],[1,2,3,4]), 4.5, 'no inters even 1.5')
        self.assertEqual(binary_median([1,2,3,4],[5,6,7]), 4, 'no inter odd 1')
        self.assertEqual(binary_median([1,2,3,4],[5,6]), 3.5, 'no inter even 2')
        self.assertEqual(binary_median([1,2,3],[5,6,7,8]), 5, 'no inter odd 2')
        self.assertEqual(binary_median([1],[2,3]), 2, 'short no intersection, larger')
        self.assertEqual(binary_median([1,2],[3]), 2, 'short no intersection, smaller')
        self.assertEqual(binary_median([3],[-2,-1]), -1, 'neg numbers')
        self.assertEqual(binary_median([1,2],[1,2,3]), 2, 'duplicate numbers')
