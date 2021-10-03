from typing import List

class Solution:
    def minimumMoves(self, s: str) -> int:
        len_s = len(s)
        total_ops = 0
        i = 0
        while i < len_s:
            if s[i] == 'X':
                total_ops += 1
                i += 2
            i += 1
        return total_ops

sol = Solution()
cases = [
    {
        "input": "XXX",
        "expect": 1
    },
    {
        "input": "XXOX",
        "expect": 2
    },
    {
        "input": "OXOX",
        "expect": 1
    },
    {
        "input": "OOOOXOXOXXOXXXXXX",
        "expect": 4
    },
    {
        "input": "OOOO",
        "expect": 0
    },
]

for case in cases:
    result = sol.minimumMoves(case["input"])
    print(case["input"], result)
    assert result == case['expect']
