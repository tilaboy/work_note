from typing import List

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        to_fill = mean * (m + n) - sum(rolls)
        estimate = to_fill / n
        if estimate > 6 or estimate < 1:
            result = []
        else:
            average_n = to_fill // n
            to_allocate = to_fill % n
            result = [average_n + 1 if i < to_allocate else average_n for i in range(n)]
        return result

sol = Solution()
cases = [
    {
        "rolls": [3,2,4,3],
        "mean": 4,
        "n": 2,
        "expect": [6,6]
    },
    {
        "rolls": [1,5,6],
        "mean": 3,
        "n": 4,
        "expect": [2,3,2,2]
    },
    {
        "rolls": [1,2,3,4],
        "mean": 6,
        "n": 4,
        "expect": []
    },
    {
        "rolls": [1],
        "mean": 3,
        "n": 1,
        "expect": [5]
    },
]

for case in cases:
    result = sol.missingRolls(case["rolls"], case["mean"], case["n"])
    #print(case["input"], result)
    assert sorted(result) == sorted(case['expect'])
