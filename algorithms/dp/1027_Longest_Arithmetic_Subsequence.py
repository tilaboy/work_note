from typing import List

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        # dp[(j, i)] the max of sequence include i
        # dp[(j, i)] = dp[(k, j)] + 1 if k < j < i and nums[i] - nums[j] == nums[j] - nums[k]
        num_index_map = dict()
        for i_num, num in enumerate(nums):
            if num in num_index_map:
                num_index_map[num].append(i_num)
            else:
                num_index_map[num] = [i_num]
        nr_nums = len(nums)
        dp = [[0] * nr_nums for _ in range(nr_nums)]
        best_las = 0
        for j in range(nr_nums - 1):
            for i in range(j + 1, nr_nums):
                diff = nums[i] - nums[j]
                target = nums[j] - diff
                candidate = num_index_map.get(target, None)
                if candidate is not None:
                    if len(candidate) == 1:
                        k = candidate[0]
                    else:
                        left, right = 0, len(candidate) - 1
                        while left <= right:
                            mid = left + (right - left) // 2
                            if candidate[mid] == j:
                                right = mid - 1
                                break
                            elif candidate[mid] > j:
                                right = mid - 1
                            else:
                                left = mid + 1
                        k = candidate[right]
                    if k > -1 and k < j:
                        dp[i][j] = dp[j][k] + 1
                        best_las = max(best_las, dp[i][j])
                        #print(f'({k} {nums[k]}) => ({j} {nums[j]})=> ({i} {nums[i]}) || {dp[i][j]}' )
        return best_las + 2

sol = Solution()
cases = [
    {
        "input": [3,6,9,12],
        "expect": 4
    },
    {
        "input": [44,46,22,68,45,66,43,9,37,30,50,67,32,47,44,11,15,4,11,6,20,64,54,54,61,63,23,43,3,12,51,61,16,57,14,12,55,17,18,25,19,28,45,56,29,39,52,8,1,21,17,21,23,70,51,61,21,52,25,28],
        "expect": 6
    },
]

for case in cases:
    result = sol.longestArithSeqLength(case["input"])
    print(case["input"], result)
    assert result == case['expect']
