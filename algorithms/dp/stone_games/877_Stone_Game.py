from typing import List

class Solution:
    def stoneGame(self, piles: List[int]) -> int:
        # dp[i, j] = different from current players for stones from i to j: = nr_stone_a - nr_stone_b
        # dp[i - 1, j] = nr_stone_b - nr_stone_a + piles[i] = piles[i - 1] - dp[i, j]
        # dp[i - 2, j] = nr_stone_a + piles[i - 1] - (nr_stone_b + piles[i]) = piles[i - 2] - dp[i - 1, j]
        nr_piles = len(piles)
        dp = [[0] * nr_piles for _ in range(nr_piles)]
        for i in range(nr_piles):
            dp[i][i] = piles[i]

        for i in range(nr_piles - 2, -1, -1):
            for j in range(i + 1, nr_piles):
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
        for i in range(nr_piles):
            print(dp[i])
        return dp[0][nr_piles - 1] > 0


sol = Solution()
cases = [
    {
        "input": [5,3,4,5],
        "expect": True
    },
    {
        "input": [3,7,2,3],
        "expect": True
    },
]

for case in cases:
    result = sol.stoneGame(case["input"])
    print(case["input"], result)
    assert result == case['expect']
