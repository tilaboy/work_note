from typing import List

#   2       4               8 16
# 0 1 0 0 0 1 0 0 0 0 0 0 0 1 0 0
# 0 1 0 0 1 0 0 0 0 1 0 0 0 0 0 1

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # dp[i][M] where 1 < x <= length: the maximal stones get by current play at i, with M
        # if nr_piles - i < 2 * M: dp[i][M] = sum(piles[i:])
        # else:
        # dp[i][M] = max( sum(piles[i:]) -  dp[i+x][max(x, M)]) for x in 1..2M
        len_piles = len(piles)
        max_M = len_piles
        dp = [[0] * (max_M + 1) for _ in range(len_piles)]
        nr_piles = 0
        for i in range(len_piles - 1, -1, -1):
            nr_piles += piles[i]
            for M in range(1, max_M + 1):
                if 2 * M >= len_piles - i:
                    dp[i][M] = nr_piles
                else:
                    for x in range(1, 2 * M + 1):
                        #print(i, x, M, i + x, max_M, max(M, x))
                        dp[i][M] = max(dp[i][M], nr_piles - dp[i + x][max(M, x)])
        #for i in range(len_piles):
        #    print(dp[i])
        return dp[0][1]




sol = Solution()
cases = [
    {
        "input": [2,7,9,4,4],
        "expect": 10
    },
    {
        "input": [1,2,3,4,5,100],
        "expect": 104
    },
    {
        "input": [1] * 10,
        "expect": 6
    },
]

for case in cases:
    result = sol.stoneGameII(case["input"])
    print(case["input"], result)
    #assert result == case['expect']
