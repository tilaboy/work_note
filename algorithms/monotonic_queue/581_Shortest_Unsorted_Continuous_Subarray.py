from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        mono_queue = list()
        nr_nums = len(nums)
        for i_num in range(nr_nums):
            num = nums[i_num]
            while mono_queue and num < mono_queue[-1][1]:
                index, value = mono_queue.pop()
            mono_queue.append((i_num, num))
        subarr_start = 0
        while subarr_start < len(mono_queue) and mono_queue[subarr_start][0] == subarr_start:
            subarr_start += 1
        if subarr_start == len(mono_queue):
            return 0

        mono_queue = list()
        for i_num in range(nr_nums - 1, -1, -1):
            num = nums[i_num]
            while mono_queue and num > mono_queue[-1][1]:
                index, value = mono_queue.pop()
            mono_queue.append((i_num, num))
        subarr_end = nr_nums - 1
        while subarr_end > 0 and mono_queue[nr_nums - 1 - subarr_end][0] == subarr_end:
            subarr_end -= 1
        return subarr_end - subarr_start + 1



sol = Solution()
cases = [
    {
        "input": [2,6,4,8,10,9,15],
        "expect": 5
    },
    {
        "input": [1, 2, 3, 4],
        "expect": 0
    },
    {
        "input": [1],
        "expect": 0
    },
]

for case in cases:
    result = sol.findUnsortedSubarray(case["input"])
    print(case["input"], result)
    assert result == case['expect']
