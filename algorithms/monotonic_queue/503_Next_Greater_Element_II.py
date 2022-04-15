from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        mono_queue = list()
        next_high = [-1] * len(nums)
        for i_num, num in enumerate(nums):
            while mono_queue and nums[mono_queue[-1]] < num:
                i_prev_num = mono_queue.pop()
                next_high[i_prev_num] = num
            mono_queue.append(i_num)

        for i_num, num in enumerate(nums):
            while mono_queue and nums[mono_queue[-1]] < num:
                i_prev_num = mono_queue.pop()
                next_high[i_prev_num] = num
            if not mono_queue:
                break
        return next_high


sol = Solution()
cases = [
    {
        "input": [1,2,3,4,3],
        "expect": [2,3,4,-1,4]
    },
    {
        "input": [1,2,1],
        "expect": [2,-1,2]
    },
]

for case in cases:
    result = sol.nextGreaterElements(case["input"])
    print(case["input"], result)
    assert result == case['expect']
