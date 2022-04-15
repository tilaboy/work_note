from typing import List
import random

# f(i) = the longest increase sequence ends at i - 1
# f(0) = 0
# f(i) = max(f(j) + 1 for all j < n and f[j] < f[i])
def lis_dp_bottom_up(nums):
    def dp_func(i, seen):
        nonlocal nums
        if i not in seen:
            best = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    score = dp_func(j, seen) + 1
                    if score > best:
                        best = score
            seen[i] = best
        return seen[i]

    nr_nums = len(nums)
    seen = dict()
    lis = 0
    for i in range(nr_nums):
        local_lis = dp_func(i, seen)
        if local_lis > lis:
            lis = local_lis
        #print(i, nums[i], local_lis, lis)
    return lis

def lis_top_down(nums):
    nr_nums = len(nums)
    dp = [1] * nr_nums
    result = 1
    for i in range(1, nr_nums):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
        result = max(result, dp[i])
    return result

def lis_greedy(nums):
    tails = [nums[0]]
    for num in nums[1:]:
        if num > tails[-1]:
            tails.append(num)
        else:
            # search for tail[i] which
            # = num
            # > num with tail[i-1] < num
            left, right = 0, len(tails) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if tails[mid] == num:
                    break
                elif tails[mid] < num:
                    left = mid + 1
                else:
                    right = mid - 1
            # end: left > right
            # when left == right:
            # if nums[mid] < target, left = left + 1 so nums[left] > target
            # if nums[mid] > target, right = right - 1, so nums[left] > target
            #print(f'\t{num} {tails} {left} = {tails[left]}, {right} = {tails[right]}')
            if left > right:
                tails[left] = num
    return len(tails)


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return lis_greedy(nums)

random.seed(42)
sol = Solution()
cases = [
    {
        "input": [10,9,2,5,3,7,101,18],
        "expect": 4
    },
    {
        "input": [0,1,0,3,2,3],
        "expect": 4
    },
    {
        "input": [2,9,7,4,5,3],
        "expect": 3
    },
    {
        "input": [7,7,7,7,7,7,7],
        "expect": 1
    },
    {
        "input": [random.randint(0, 5000) for _ in range(1000)],
        "expect": 60
    }
]

for case in cases:
    result = sol.lengthOfLIS(case["input"])
    print(case["input"], result)
    assert result == case['expect']
