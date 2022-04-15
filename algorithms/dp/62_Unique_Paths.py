from typing import List

# https://leetcode.com/problems/unique-paths/

def up_recur(m, n):
    if m == 1 or n == 1:
        return 1
    return up_recur(m-1, n) + up_recur(m, n-1)

def up_recur_with_mem(m, n, seen):
    if m == 1 or n == 1:
        return 1
    if (m, n) not in seen:
        seen[(m, n)] = up_recur(m-1, n) + up_recur(m, n-1)
    return seen[(m, n)]


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return up_recur_with_mem(m, n, {})

sol = Solution()
cases = [
    {
        "m": 3,
        "n": 7,
        "expect": 28
    },
    {
        "m": 3,
        "n": 2,
        "expect": 3
    },
    {
        "m": 7,
        "n": 3,
        "expect": 28
    },
    {
        "m": 3,
        "n": 3,
        "expect": 6
    },
]

for case in cases:
    result = sol.uniquePaths(case["m"], case["n"])
    print(case["m"], case["n"], result)
    assert result == case['expect']
