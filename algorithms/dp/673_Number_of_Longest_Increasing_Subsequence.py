from typing import List

def LIS_dp(nums):
    nr_nums = len(nums)
    dp = [(1, 1)] * nr_nums
    for i in range(1, nr_nums):
        for j in range(i):
            if nums[i] > nums[j]:
                j_max, j_count = dp[j]
                length_sub_seq = j_max + 1
                if length_sub_seq > dp[i][0]:
                    dp[i] = (length_sub_seq, j_count)
                elif length_sub_seq == dp[i][0]:
                    dp[i] = (dp[i][0], dp[i][1] + j_count)

    lis = 0
    lis_count = 0
    for i in range(nr_nums):
        if dp[i][0] > lis:
            lis, lis_count = dp[i]
        elif dp[i][0] == lis:
            lis_count += dp[i][1]
    return lis_count


def LIS_greedy(nums):
    nr_nums = len(nums)
    tails = list()
    tails.append([(nums[0], 1)])
    largest_length_index = 0
    for num in nums[1:]:
        if num > tails[-1][-1][0]:
            new_count = 0
            for prev_large, count in tails[-1]:
                if num > prev_large:
                    new_count += count
            tails.append([(num, new_count)])
        else:
            for i in range(len(tails)):
                if num <= tails[i][-1][0]:
                    break
            # two situations:
            # - num is new: check all i - 2, count lower than num
            # - num is already in tails[i - 1]: still do the same
            new_count = 0
            if i - 1 >= 0:
                for prev_large, count in tails[i - 1]:
                    if num > prev_large:
                        new_count += count
            else:
                new_count = 1
            tails[i].append((num, new_count))
        print(tails)
    return sum([count for num,count in tails[-1]])


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        return LIS_greedy(nums)

sol = Solution()
cases = [
    {
        "input": [1,3,5,4,7],
        "expect": 2
    },
    {
        "input": [1,1,1,2,2,2,3,3,3],
        "expect": 27
    },
    {
        "input": [2,2,2,2,2],
        "expect": 5
    },
]

for case in cases:
    result = sol.findNumberOfLIS(case["input"])
    print(case["input"], result)
    assert result == case['expect']
