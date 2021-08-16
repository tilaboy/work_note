from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        sorted_nums, len_nums = sorted(nums), len(nums)
        half, is_odd = len_nums // 2, len_nums % 2
        result = list()
        for i in range(half):
            result.append(sorted_nums[i+half])
            result.append(sorted_nums[i])
        if is_odd:
            result.append(sorted_nums[-1])
        return result


sol = Solution()
cases = [[1,2,3,4,5], [6,2,0,9,7], [1,2,3,4,5,6], [1], []]

for case in cases:
    result = sol.rearrangeArray(case)
    print(f"{case} => {result}")
    for i in range(1, len(case) - 1):
        if result[i] == (result[i-1] + result[i+1])/2:
            print(f"error at {i}, {result[i]}")
