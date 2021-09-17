from typing import List

# [a b c ... x y z] => all_sum
# sort(all_sum)
# all_sum[-1] = sum(all positive)
# all_sum[0] = sum(all negative) if < 0 else a
# all_sum[-2] =
#    1. sum(0: positive) - min(positive)
#    2. sum(0: positive) + max(negative)
# all_sum[-3] =
#    1. (-2 is positive[0])
#       sum(1: positive) + max(negative)
#       sum(1: positive) - positive[-2]
#
#    2. sum(all positive) - min(positive)
#
#
# max(all_sum) =>
# min(all_sum) =>

def ra_recur(n, sums, min_v, guessed):
    max_sum = sums[-1]
    sec_max_sum = sum[-2]

    if min_v < 0:
        ra_recur()
    min_p = max_sum - sec_max_sum


class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        sorted_sums = sorted(sums)
        len_sums = len(sorted_sums)
        min_v, max_v = sums[0], sums[-1]
        nr_max, nr_min = 0, 0
        i = 0
        while sorted_sums[i] == min_v:
            i += 1
        nr_min = i
        i = len_sums - 1
        while sorted_sums[i] == min_v:
            i += 1
        nr_min = i

        for ele in sums:
            if ele == max_v:
                nr_max += 1
            if ele > max_v:
                max_v = ele
                nr_max = 1
            if ele == min_v:
                nr_min += 1
            if ele < min_v:
                min_v = ele
                nr_min = 1
        print("max, min:", nr_max, nr_min)
        if min_v < 0:
            assert nr_max == nr_min
        else:
            assert nr_max == nr_min - 1
        nr_guessed = nr_max - 1
        guessed = [0] * nr_guessed



sol = Solution()
cases = [
    {
        "sums": [-3,-2,-1,0,0,1,2,3],
        "n": 3,
        "expect": [-3, 1, 2]
    },
    {
        "sums": [0,0,0,0],
        "n": 2,
        "expect": [0,0]
    },
    {
        "sums": [0,0,5,5,4,-1,4,9,9,-1,4,3,4,8,3,8],
        "n": 4,
        "expect": [-1,0,4,5]
    },
    {
        "sums": [-3,-2,-1,0,1,2,2,3,3,4,4,5,6,7,8,9],
        "n": 4,
        "expect": [-2,-1,4,5]
    },
]

for case in cases:
    result = sol.recoverArray(case["input"])
    print(case["input"], result)
    assert result == case['expect']
